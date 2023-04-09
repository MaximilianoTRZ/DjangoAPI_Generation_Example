from ...views import loginViews, logoutViews, loginAutoViews
from rest_framework import routers
from django.urls import path

# Router
routerV1 = routers.DefaultRouter()

routerV1.register('login', loginViews.login, basename='login')
routerV1.register('login/auto', loginAutoViews.loginAuto, basename='loginAuto')
routerV1.register('logout', logoutViews.logout, basename='logout')