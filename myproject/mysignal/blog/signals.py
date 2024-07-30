from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete


#2ed method to connect to the server
@receiver(user_logged_in,sender=User)    # THis is standard way to connect # User- its modle name you can give your modle name like my modle i Student so i give you sender=Student 
def login_success(sender,request,user,**kwargs):
    print("Login Signal !!!")
    print("Sender : ",sender)
    print('Request : ',request)
    print("User : ",user)
    print("Passowrd : ",user.password)
    print(f'kwargs : {kwargs}')

# 1st method to connect to the server
# user_logged_in.connect(login_success,sender=User)


@receiver(user_logged_out,sender=User)    # THis is standard way to connect
def logout_success(sender,request,user,**kwargs):
    print("Logout signal !!!")
    print("Sender : ",sender)
    print('Request : ',request)
    print("User : ",user)
    print("Passowrd : ",user.password)
    print(f'kwargs : {kwargs}')
# user_logged_out.connect(logout_success,sender=User)



@receiver(user_login_failed)    # THis is standard way to connect
def login_failed(sender,credentials,request,**kwargs):
    print("Login Failed signal !!!")
    print("Sender : ",sender)
    print('Request : ',request)
    print("Creadential : ",credentials)
    print(f'kwargs : {kwargs}')
# user_login_failed.connect(login_failed)

@receiver(pre_save,sender=User)
def at_beging_save(sender,instance,**kwargs):
    print("Pre save signal !!!")
    print("Sender : ",sender)
    print("Instance : ",instance)
    print(f'kwargs : {kwargs}')



@receiver(post_save,sender=User)
def at_end_save(sender,instance,created,**kwargs):
    if created:
        print("Post save signal !!!")
        print("New Created")
        print("Sender : ",sender)
        print("Instance : ",instance)
        print("Created : ",created)
        print(f'kwargs : {kwargs}')
    else:
        print("Post save signal !!!")
        print("Updated")
        print("Sender : ",sender)
        print("Instance : ",instance)
        print("Created : ",created)
        print(f'kwargs : {kwargs}')



@receiver(pre_delete,sender=User)
def at_beging_delete(sender,instance,**kwargs):
    print("Pre delete signal !!!")
    print("Sender : ",sender)
    print("Instance : ",instance)
    print(f'kwargs : {kwargs}')


@receiver(post_delete,sender=User)
def at_end_delete(sender,instance,**kwargs):
    print("Post delete signal !!!")
    print("Sender : ",sender)
    print("Instance : ",instance)
    print(f'kwargs : {kwargs}')
