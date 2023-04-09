from ...views import authorViews, genreViews, bookViews, bookInstanceViews,usersViews
from rest_framework import routers

# Router
routerEntities = routers.DefaultRouter()

routerEntities.register('author', authorViews.AuthorViewSet)
routerEntities.register('genre', genreViews.GenreViewSet)
routerEntities.register('book', bookViews.BookViewSet)
routerEntities.register('bookInstance', bookInstanceViews.BookInstanceViewSet)
# routerEntities.register(r'user/(?P<username>)', usersViews.users, basename='user')
