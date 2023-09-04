from django.shortcuts import render, redirect, get_object_or_404

def dashboard(request):
    return render(request, 'myfolio/index.html')

def public_archive(request):
    return render(request, 'public/profiles/archive.html')

def public_timeline(request):
    return render(request, 'public/profiles/timeline.html')