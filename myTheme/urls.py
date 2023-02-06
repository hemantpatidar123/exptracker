"""myTheme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myApp import views as v1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.renderPage),
    path('signUp',v1.signUp),
    path('signup_save',v1.signup_save),
    path('login_Data',v1.login_Data),
    path('showExpPage',v1.showExpPage),
    path('save_Expence',v1.save_Expence),
    path('ShowIncomePage',v1.ShowIncomePage),
    path('save_income',v1.save_income),
    path('showExp',v1.showExp),
    path('showIncome',v1.showIncome),
    path('Deshboard',v1.Deshboard),
    path('logout',v1.logout)

]
