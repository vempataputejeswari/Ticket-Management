from django.contrib import admin
from movie_tutorials.models import Movie_Tutorials,Theater,ticket,booking,All,movie_details
# Register your models here.

admin.site.register(Movie_Tutorials)
admin.site.register(Theater)
admin.site.register(ticket)
admin.site.register(booking)
admin.site.register(movie_details)

