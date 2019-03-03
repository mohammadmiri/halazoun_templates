from django.shortcuts import render


def template_1(request):
    return render(request, 'custom_templates/template_1.html')
