from django.http import JsonResponse
from model.model import Model



def generate(_, path):
    model = Model.load('model/')
    return JsonResponse({line : model.query(line) for line in path.split('/')})
