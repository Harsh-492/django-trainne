from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("Loggged Successfully")
    print("Sender : ",sender)
    ip = request.META.get('REMOTE_ADDR')
    print("Ip : ",ip)
    request.session['ip'] = ip