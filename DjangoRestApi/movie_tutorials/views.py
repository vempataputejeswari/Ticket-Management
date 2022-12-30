from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_tutorials.models import Movie_Tutorials
from .serializers import Movie_TutorialsSerializer


@api_view(['GET', 'POST'])
def movie_tutorials_list(request):
    """
    List all code movie_tutorials, or create a new tutorials.
    """
    if request.method == 'GET':
        movie_tutorials = Movie_Tutorials.objects.all()
        serializer = Movie_TutorialsSerializer(movie_tutorials, many=True)
        return Response( {'title_name':'love_today',
                  'language':'telugu',
                  'airing_date':12,
                  'casts':6,
                  'genre':'comic',
                  'language':'tel',
                  'movie_name':'tej',
                  'ticket_id':12/12/22,
                  'seat_no':4,
                  'cinema_name':'tej',
                  'show_time':3})

    elif request.method == 'POST':
        movie_tutorials = Movie_Tutorials.objects.all()
        serializer = Movie_TutorialsSerializer(movie_tutorials, many=True)
        print('Request data is : ',request.data)
        return Response({'cancel_ticket':'done','ticket_booking':5})
        
 