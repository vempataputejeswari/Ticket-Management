from django.db import models


class Movie_Tutorials(models.Model):
    title_name = models.CharField(max_length=70, blank=False, default='')
    language = models.CharField(max_length = 160)
    airing_date = models.DateField()
    theater_name= models.CharField(max_length=10)
    image = models.FileField(upload_to ='image')
    city = models.CharField(max_length = 200)
    def __str__(self):
        return self.title_name


class Theater(models.Model):
	movie_rating = models.BooleanField(default=False)
	casts = models.CharField(max_length=10)
	genre = models.CharField(max_length=15)
	language =  models.CharField(max_length = 160)
	movie_name = models.CharField(max_length = 200)

	def __str__(self):
		return self.movie_name

class ticket(models.Model):
	book_tickets = models.IntegerField(default=5)

class booking(models.Model):
	cancel_ticket = models.TextField(max_length=20)

class All(models.Model):
	all_booking = models.CharField(max_length=25)

class movie_details(models.Model):
	ticket_id = models.IntegerField()
	seat_no = models.IntegerField()
	cinema_name = models.CharField(max_length=40)
	movie_date = models.DateField()
	show_time = models.TimeField()



