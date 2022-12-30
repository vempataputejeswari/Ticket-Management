from rest_framework import serializers 
from movie_tutorials.models import Movie_Tutorials
 
 
class Movie_TutorialsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Movie_Tutorials
        fields = ('title_name',
                  'language',
                  'airing_date',
                  'casts'
                  'genre'
                  'language'
                  'movie_name'
                  'ticket_id'
                  'seat_no'
                  'cinema_name'
                  'show_time')