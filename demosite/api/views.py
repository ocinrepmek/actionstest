from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    cmd = "git status"
    ret = os.system(cmd)
    return HttpResponse("Unsecure page with command execution: " + str(ret))