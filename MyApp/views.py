# example/views.py
from datetime import datetime
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
import networkx as nx
import numpy as np
from functools import reduce
import math
from itertools import chain, combinations


def index(request):
    template = loader.get_template("MyApp/index.html")


    graph_data = {
            "nodes": [
                {"id": 1, "name": "a1"},
                {"id": 2, "name": "a2"},
                # Add more nodes as needed
            ],
            "links": [
                {"source": 1, "target": 2},
                # Add more links as needed
            ],
    }

    context = {
            'graph_data': json.dumps(graph_data),
    }

    return HttpResponse(template.render(context, request))

def compute(request):
    if request.method == 'POST':
        text = request.POST.get('input_text', '')  # Get the text from the POST data
        selected_semantics = request.POST.get("semantics")


        console_text = "Computation started.\n"
        text = text.replace('\n', '').replace('\r', '')
        text = text.replace(" ", "")
        text_split = text.split(".")

        arguments = set()
        console_text += "Parsing started.\n"
        #Parsing of the arguments
        for t in text_split:
            if t[:4] == "arg(":
                arguments.add(t[4:-1])

        console_text += str(len(arguments)) + " arguments found:\n"
        for arg in arguments:
            console_text += "- "+arg+"\n"

        attacks = set()
        for t in text_split:
            if t[:4] == "att(":
                att_split = t[4:-1].split(",")
                if (att_split[0] in arguments) and (att_split[1] in arguments):
                    attacks.add((att_split[0],att_split[1]))
                else:
                     console_text += "Problem with parsing an attack. You may have declared an attack before declaring an argument.\n"

        console_text += str(len(attacks)) + " attacks found:\n"
        for (a,b) in attacks:
            console_text+= "- "+a + " attacks "+ b+"\n"


        index_dict = { i: a for (i,a) in enumerate(arguments)}
        arg_dict = { a: i for (i,a) in enumerate(arguments)}

        #We create the graph to send to the view
        # gdata_input = {
        #     "nodes": [{"id": arg_dict[a], "name": a} for a in arguments],
        #     "links": [{"source": arg_dict[a], "target": arg_dict[b]} for (a,b) in attacks],
        # }


        console_text += "Computing semantics using the semantics: "+selected_semantics+". \n"
        G = nx.DiGraph()
        G.add_nodes_from(range(len(arguments)))
        G.add_edges_from([(arg_dict[a],arg_dict[b]) for (a,b) in attacks])
        set_degrees(G,sem=selected_semantics)
        set_Shapley_measure(G,sem=selected_semantics)

        information_arg = [{"arg": index_dict[i],
                       "degree": round(G.nodes[i]["degree"],3)} for i in range(len(arguments))]

        gdata_input = convert_to_dot(G)

        response_data = {'console': console_text,
                         'graph_data': gdata_input,
                         'information_arg': information_arg}
        return JsonResponse(response_data)  # Return the result as JSON
    return render(request, "MyApp/index.html")



def set_degrees(G, sem="cat", epsilon=0.0001):

    num_nodes = G.number_of_nodes()
    current_degrees = np.array([1 for i in range(num_nodes)])
    list_nodes = list(G.nodes())

    error = 100

    while error >= epsilon:
        temp_degrees = np.array([])

        for i in range(num_nodes):
            att_i = [x for x in G.predecessors(list_nodes[i])]



            if att_i == []:
                temp_degrees = np.append(temp_degrees,1)
            else:
                index_attackers = [np.where(np.array(list_nodes)==z)[0] for z in att_i]
                att_i = reduce(np.union1d, index_attackers)

                if sem == "cat":
                    temp_degrees = np.append(temp_degrees,1 / (1 + sum([current_degrees[j] for j in att_i])))
                elif sem == "max":
                    temp_degrees = np.append(temp_degrees,1 / (1 + max([current_degrees[j] for j in att_i])))
                elif sem == "card":
                    temp_degrees = np.append(temp_degrees,1 / (1 + len(att_i)+ sum([current_degrees[j] for j in att_i])/len(att_i)))


        ## We calculate the error
        error = np.linalg.norm(temp_degrees - current_degrees)

        current_degrees = temp_degrees



    nx.set_node_attributes(G,{list_nodes[i]: deg for (i,deg) in enumerate(current_degrees)}, name="degree")
    return G


def copy_graph_without_X(G,X):
    G2 = nx.DiGraph()
    for g in G.nodes():
        G2.add_node(g)

    for (u,v) in G.edges():
        if(not ((u,v) in X)):
            G2.add_edge(u,v)
    return G2


def set_Shapley_measure(G, sem):
    list_edges = list(G.edges())
    list_intensity = []


    for e in list_edges:
        attackers = [x for x in G.predecessors(e[1])] #We get the list of attackers of the attacked argument
        n = len(attackers)

        #print("EDGE:",e)

        if (n == 1):
            #If there is only one attack, the contrib. is 1 - degree
            list_intensity.append(1-G.nodes[e[1]]["degree"])
        else:
            #If there are multiple attacks, we need to consider subsets of attacks
            #print("attackers",attackers)
            Y = [ y for y in attackers if y != e[0]]
            total = 0
            for X in (list(powerset(Y))):
                sizeX = len(X)
                X_edges = [(x, e[1]) for x in X]

                #print("X",X_edges)

                A1 = copy_graph_without_X(G,X_edges)
                set_degrees(A1, sem)
                deg_A1 = A1.nodes[e[1]]["degree"]


                X_edges.append((e[0],e[1]))
                A2 = copy_graph_without_X(G,X_edges)
                set_degrees(A2, sem)
                #print("A2",A2.nodes(data=True), A2.edges())
                #print(A2.nodes[e[1]]["degree"])
                deg_A2 = A2.nodes[e[1]]["degree"]

                total += math.factorial(sizeX) * math.factorial(n-sizeX-1) / math.factorial(n) * (deg_A2-deg_A1)
            list_intensity.append(total)

    nx.set_edge_attributes(G, {list_edges[i] : list_intensity[i] for i in range(len(list_edges))}, name="attack_intensity")

def convert_to_dot(G):
    if(not nx.is_empty(G)):
        result= "digraph G {"
        for a in G.nodes:
            result+= str(a)+" [xlabel="+str(round(G.nodes[a]["degree"],3))+"];"
        for (i,j) in G.edges:
            result+= str(i)+" -> "+str(j)+" [label="+str(round(G[i][j]["attack_intensity"],3))+"];"
        return result+"}"
