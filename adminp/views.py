from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
  return render(request, 'adminp/dashboard.html')
  
def login_view(request):
  return render(request, 'adminp/login.html')