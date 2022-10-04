from ...views import loginViews, logoutViews
from rest_framework import routers

# Router
routerV1 = routers.DefaultRouter()

routerV1.register('login', loginViews.login, basename='login')
routerV1.register('logout', logoutViews.logout, basename='logout')