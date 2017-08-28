from django.shortcuts import render

def become(request):
    template = 'become/become.html'
    return render(request, template)
