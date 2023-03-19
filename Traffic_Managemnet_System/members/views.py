from django.http import HttpResponse
from django.template import loader

def homepage(request):
  template = loader.get_template('Homepage.html')
  return HttpResponse(template.render())

def admin(request):
  template = loader.get_template('login.html')
  template = loader.get_template('registration.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())


def registration(request):
  template = loader.get_template('registration.html')
  return HttpResponse(template.render())