from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core import serializers

from immoScenario.models import ImmoScenario


def load_scenario(request, scenario_id):
    scenario = get_object_or_404(ImmoScenario, pk=scenario_id)
    json_scenario = serializers.serialize('json', [scenario])
    return HttpResponse(json_scenario, content_type="text/json-comment-filtered")


def save_scenario(request, scenario_id):
    response = "You're saving at scenario %s."
    return HttpResponse(response % scenario_id)


def create_scenario(request):
    scenario = ImmoScenario.objects.create()
    scenario.save()
    json_scenario = serializers.serialize('json', [scenario])
    return HttpResponse(json_scenario, content_type="text/json-comment-filtered")


def all_scenarios(request):
    scenarios = ImmoScenario.objects.all()
    json_scenarios = serializers.serialize('json', scenarios, fields=('title', 'created_date'))
    return HttpResponse(json_scenarios, content_type="text/json-comment-filtered")
