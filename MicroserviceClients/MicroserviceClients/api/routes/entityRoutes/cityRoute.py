from ...views import cityViews
from ..indexRoutes import routerEntities

routerEntities.register('city', cityViews.CityViewSet)