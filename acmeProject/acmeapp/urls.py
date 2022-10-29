from django.contrib import admin
from django.urls import path 
from acmeapp.views import *

urlpatterns = [ 
    #login page
    path("register/",register,name="register"),
    path("login/",Login,name="login"),
    path("logout/",Logout,name="logout"),

    path("",home,name="base.html"),
    path("createuser/",createuser,name="createuser.html"),
    path("ticket/", ticket,name="ticket.html"),
    path("add_dep/",AddPostView.as_view(),name="dep_add.html"),
    path("edit_dep/<int:pk>/",UpdatePostView.as_view(),name="dep_edit.html"),
    path("delete/<int:pk>",DeletePostView.as_view(),name="dep_del.html")

]