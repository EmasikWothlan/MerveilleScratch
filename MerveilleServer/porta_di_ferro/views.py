from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def porta_di_ferro(request):
    if request.method == 'POST':
        if request.POST.get('invite-code') == 'K9BZgtQT6CST2u':
            response = HttpResponseRedirect('/')
            response.set_signed_cookie('username', request.POST.get('username'), salt='SyntaxError')
            response.set_signed_cookie('logged-in', 'yes', salt='IndentationError')
            return response
    else:
        try:
            if request.get_signed_cookie('logged-in', salt='IndentationError') == 'yes':
                username = request.get_signed_cookie('username', salt='SyntaxError')
                return render(request, 'front_page.html', {'username': username})
        except KeyError:
            return render(request, 'porta_di_ferro.html')


def leave(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('logged-in')
    response.delete_cookie('username')
    return response
