from django.http import JsonResponse


def generate(request):
    return JsonResponse({'message': 'hello'})
