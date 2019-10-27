from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from . import models
from .models import InputForm
from functools import reduce
import copy
import time

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        form = InputForm()
    return render(request, 'Home.html', {'form': form})

def present_output(form):
    st = time.time()
    n = form.r
    if (n > 0):
        t = copy.copy(n) #Copy the 'n' value to use further
        def fibonacci(t):
            return reduce(lambda x, _: x+[x[-1]+x[-2]], range(t-2), [1, 1]) #Get the list of fibonacci series in an array
        ans = fibonacci(t) 
        Duration = time.time() - st
        Message = "In Fibonacci Series, %d is the value in the position %d & Time Taken = %f" % (ans[n-1],n,Duration) #Display the nth value in the series & Response Time
        return HttpResponse("<h2>%s</h2>" % Message)
    else:
        return HttpResponse("<h2>Enter a number greater than 0</h2>")
    