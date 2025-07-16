from django.urls import path
from accounts import views
urlpatterns = [
    path("login/",views.login_page,name="login_page"),
    path("register/",views.register,name="register"),
    path('send_otp/<email>/' , views.send_otp, name='send_otp'),
    path('verify-otp/<email>/' , views.verify_otp, name='verify_otp'),
    path("verify-account/<token>",views.verify_email_token,name="verify_email_token"),
    path('login-vendor/' , views.login_vendor, name='login_vendor'),
    path('register-vendor/' , views.register_vendor, name='register_vendor'),
    path('dashboard/', views.dashboard , name="dashboard"),
    path('add-hotel/', views.add_hotel , name="add_hotel"),
    path('delete_image/<id>/' , views.delete_image , name="delete_image"),
    path('<slug>/upload_images/' , views.upload_images , name="upload_images"),
    path('<slug>/edit_hotel/' , views.edit_hotel , name="edit_hotel"),
    path('logout/' , views.logout_view , name="logout_view"),
    path('hotel/<slug:slug>/bookings/', views.hotel_bookings, name='hotel-bookings'),
  
]
