# views.py

from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

class SetSessionView(View):
    def get(self, request):
        request.session['name'] = 'Harsh'
        request.session['city'] = 'Ahmedabad'
        request.session.set_expiry(20)  # Session expires after 20 seconds
        return render(request, 'student/setsession.html')


class GetSessionView(View):
    def get(self, request):
        if 'name' in request.session and 'city' in request.session:
            name = request.session.get('name')
            city = request.session.get('city')
            mykeys = request.session.keys()
            myitems = request.session.items()
            request.session.modified = True
            return render(request, 'student/getsession.html', {
                'name': name,
                'city': city,
                'mykeys': mykeys,
                'myitems': myitems,
            })
        else:
            return HttpResponse('Session Expired')


class DeleteSessionView(View):
    def get(self, request):
        # Flushes the entire session data
        request.session.flush()
        # Clears expired sessions
        request.session.clear_expired()
        return render(request, 'student/delsession.html')
