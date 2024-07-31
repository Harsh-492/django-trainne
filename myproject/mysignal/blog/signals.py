from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created

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



@receiver(pre_init,sender=User)
def at_beging_init(sender,*args,**kwargs):
    print("Pre init signal !!!")
    print("Sender : ",sender)
    print(f"Args : {args}")
    print(f'kwargs : {kwargs}')


@receiver(post_init,sender=User)
def at_end_init(sender,*args,**kwargs):
    print("Post init signal !!!")
    print("Sender : ",sender)
    print(f"Args : {args}")
    print(f'kwargs : {kwargs}')


@receiver(request_started)
def at_beging_request(sender,environ,**kwargs):
    print("At Beginning request signal !!!")
    print("Sender : ",sender)
    print(f"Args : {environ}")
    print(f'kwargs : {kwargs}')

@receiver(request_finished)
def at_end_request(sender,**kwargs):
    print("At End request signal !!!")
    print("Sender : ",sender)
    print(f"kwargs : {kwargs}")

@receiver(got_request_exception)
def at_req_exception(sender,request,**kwargs):
    print("At End request exception !!!")
    print("Sender : ",sender)
    print("Request : ",request)
    print(f"kwargs : {kwargs}")

@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("Before Install App !!!")
    print("Sender : ",sender)
    print("App_Config : ",app_config)
    print("Verbosity : ",verbosity)
    print("Interactive : ",interactive)
    print("Using : ",using)
    print("Plan : ",plan)
    print("apps : ",apps)
    print(f"kwargs : {kwargs}")


@receiver(post_migrate)
def after_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("After Install App !!!")
    print("Sender : ",sender)
    print("App_Config : ",app_config)
    print("Verbosity : ",verbosity)
    print("Interactive : ",interactive)
    print("Using : ",using)
    print("Plan : ",plan)
    print("apps : ",apps)
    print(f"kwargs : {kwargs}")

@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
    print("connection databases !!!")
    print("Sender : ",sender)
    print("connection : ",connection)
    print(f"Kwargs : {kwargs}")