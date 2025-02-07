from django.shortcuts import render, get_object_or_404
from .models import SomeModel

def some_model_list(request):
    models = SomeModel.objects.all()
    return render(request, 'another_app/some_model_list.html', {'models': models})

def some_model_detail(request, model_id):
    model = get_object_or_404(SomeModel, id=model_id)
    return render(request, 'another_app/some_model_detail.html', {'model': model})
