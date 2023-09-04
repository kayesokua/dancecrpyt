from django.shortcuts import render, redirect, get_object_or_404

def about(request):
    return render(request, 'about/index.html')