from ...views import addressViews
from ..indexRoutes import routerEntities

routerEntities.register('address', addressViews.AddressViewSet)