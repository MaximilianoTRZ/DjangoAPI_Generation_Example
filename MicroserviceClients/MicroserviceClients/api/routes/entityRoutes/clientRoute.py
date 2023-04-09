from ...views import clientViews
from ..indexRoutes import routerEntities

routerEntities.register('client', clientViews.ClientViewSet)