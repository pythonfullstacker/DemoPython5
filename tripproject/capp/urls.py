from. import views
from django.urls import path


from .views import profile
app_name = 'capp'  # This defines the namespace for this URLs module

urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/', views.profile, name='profile'),
    path('movie/<int:movie_id>/',views.detail, name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('home/',views.home,name='home')


    ]