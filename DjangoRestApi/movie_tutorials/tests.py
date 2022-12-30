from django.test import TestCase

# Create your tests here.
from movie_tutorials.models import Movie_Tutorials

from movie_tutorials.models import Movie_Tutorials

class MyTest(TestCase):
	def test_record(self):
		try:
			obj = Movie_Tutorials(name="love_today",
			      language="Telugu",
	              theater = "krishna",
	              city="rajam")

			obj.save()
			self.assertEquals(obj.name,'love_today',"name mismatch")
			self.assertEquals(obj.language,'telugu',"movie language mismatch")
			self.assertEquals(obj.theater,'krishna',"theater mismatch")

		except Exception as e:
			print('unable to insert the record')

class MyTest(TestCase):
	def test_record(self):
		try:
			obj = movie_details(ticket_id=15,
			      seat_no=2,
	              cinema_name = "krishna",
	              movie_date = 12
	             )

			obj.save()
			self.assertEquals(obj.ticket_id,15,"id mismatch")
			self.assertEquals(obj.seat_no, 3,"number language mismatch")
			self.assertEquals(obj.cinema_name,'krishna',"cinema mismatch")


		except Exception as e:
			print('unable to insert the record')
