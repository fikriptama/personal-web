from django.urls import path
from . import views

#add urls atau linkan ke urls

urlpatterns = [
    path('', views.home, name='main page'),
    path('contact', views.kontak, name='kontak' ),
    path('resume', views.resume, name='resume'),
    path('projects', views.project),
    path('signup',views.register, name='register'),
    path('login', views.masuk, name='login'),
    path('logout', views.out)
]
