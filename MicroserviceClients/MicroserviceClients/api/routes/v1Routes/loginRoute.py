from ...views import loginViews
from ..indexRoutes import routerV1

routerV1.register('login', loginViews.login, basename='login')

