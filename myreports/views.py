from django.shortcuts import render, redirect, get_object_or_404

def reports_dashboard(request):
    return render(request, 'myreports/index.html')