from django.urls import path
from . import views

urlpatterns = [

    path('signup/', views.CustomSignupView.as_view(), name='signup'),
    path('login/', views.CustomUserLoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),


#    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', views.CustomPasswordResetView.as_view(), name='password_reset_done'),  # Custom view or template view can be used for password reset done
#     path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', views.CustomPasswordResetView.as_view(), name='password_reset_complete'),  # Custom 
]
