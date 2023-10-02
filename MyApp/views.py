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
        # Perform any processing on the text if needed
        response_data = {'result': text}
        return JsonResponse(response_data)  # Return the result as JSON
    return render(request, "MyApp/index.html")