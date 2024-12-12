from django.shortcuts import render
from django.views.generic import TemplateView

def function_template(request):
    return render(request,'second_task/function_template.html')

class class_render(TemplateView):
    template_name = 'second_task/class_template.html'