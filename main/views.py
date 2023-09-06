from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Winoto Hasyim',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)