from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())


def scholarship_details(request):
    template = loader.get_template('scholarship-details.html')
    return HttpResponse(template.render())


def scholarships(request):
    template = loader.get_template('scholarships.html')
    return HttpResponse(template.render())


def universities(request):
    template = loader.get_template('universities.html')
    return HttpResponse(template.render())


def university_details(request):
    template = loader.get_template('university-details.html')
    return HttpResponse(template.render())