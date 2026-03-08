"""
URL configuration for abid1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  app1 import views 
# from forms import PrincipalMessage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signupPage,name='signup'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('home/', views.home,name='home'),
    path('form/',views.form,name='form'),
    path('table/',views.table,name='table'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('princi/',views.princi,name='principle'),
    path('aboutprincipal/',views.aboutprincipal,name='aboutprincipal'),
    path('principal_form/',views.principal_view,name='principal_form'),
    path('T_form/',views.cant_teacher,name='T_form'),
    path('T_table/',views.T_table,name='T_table'),
    path('U_form/<int:id>',views.up_teacher,name='U_form'),
    path('T_delete/<int:id>',views.T_delete,name='T_delete')

    
]
