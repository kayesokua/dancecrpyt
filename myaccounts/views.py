from django.shortcuts import render

# Create your views here.
def account_signup(request):
    return render(request, 'public/accounts/sign_up.html')

def account_sign_in(request):
    return render(request, 'public/accounts/sign_in.html')

def account_personal_settings(request):
    return render(request, 'myaccounts/personal_settings.html')

def account_security_settings(request):
    return render(request, 'myaccounts/security_settings.html')