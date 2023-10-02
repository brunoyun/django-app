# example/views.py
from datetime import datetime
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json

def index(request):
    template = loader.get_template("MyApp/index.html")


    graph_data = {
            "nodes": [
                {"id": 1, "name": "Node 1"},
                {"id": 2, "name": "Node 2"},
                # Add more nodes as needed
            ],
            "links": [
                {"source": 1, "target": 2},
                # Add more links as needed
            ],
    }

    context = {
            "athlete": 3,
            'graph_data': json.dumps(graph_data),
    }

    return HttpResponse(template.render(context, request))

def compute(request):
    if request.method == 'POST':
        text = request.POST.get('input_text', '')  # Get the text from the POST data
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
            console_text += arg+"\n"

        attacks = set()
        for t in text_split:
            console_text += "DEBUG: " + t +" "+ t[:4]+"\n"
            if t[:4] == "att(":
                console_text += "FOUND att"+"\n"
                att_split = t[4:-1].split(",")
                console_text += att_split[0]+" "+att_split[1]+"\n"
                if (att_split[0] in arguments) and (att_split[1] in arguments):
                    console_text += "BOTH args found\n"
                    attacks.add((att_split[0],att_split[1]))
                else:
                     console_text += "Problem with parsing an attack. You may have declared an attack before declaring an argument.\n"

        console_text += str(len(attacks)) + " attacks found:\n"
        for (a,b) in attacks:
            console_text+= a + " attacks "+ b

        response_data = {'console': console_text}
        return JsonResponse(response_data)  # Return the result as JSON
    return render(request, "MyApp/index.html")