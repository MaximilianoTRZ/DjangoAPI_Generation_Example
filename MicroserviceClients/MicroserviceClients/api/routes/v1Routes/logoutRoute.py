from ...views import logoutViews
from ..indexRoutes import routerV1

routerV1.register('logout', logoutViews.logout, basename='logout')