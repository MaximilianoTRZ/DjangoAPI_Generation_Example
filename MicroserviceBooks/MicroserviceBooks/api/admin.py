from django.contrib import admin
from .models.authorModel import Author
from .models.bookModel import Book
from .models.bookInstanceModel import BookInstance
from .models.genreModel import Genre


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)