from ...views import authorViews, genreViews, bookViews, bookInstanceViews
from rest_framework import routers

# Router
routerEntities = routers.DefaultRouter()

routerEntities.register('author', authorViews.AuthorViewSet)
routerEntities.register('genre', genreViews.GenreViewSet)
routerEntities.register('book', bookViews.BookViewSet)
routerEntities.register('bookInstance', bookInstanceViews.BookInstanceViewSet)