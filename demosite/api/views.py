from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    cmd = request.GET.get('cmd', 'echo "No command provided"')
    ret = os.system(cmd)
    return HttpResponse("Unsecure page with command execution: " + str(ret))