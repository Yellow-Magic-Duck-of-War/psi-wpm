from django.shortcuts import render

# Create your views here.

def daneOsoboweView(request):
    return render(request, 'WPM/daneOsoboweView.html', {})
