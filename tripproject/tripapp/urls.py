from. import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo')
    # path('about/',views.about,name='about'),
    # path('contact',views.contact,name='contact')
# path('register/',views.register,name='register')
]