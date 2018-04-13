from django.db import models

# Create your models here.
class Earthquake(models.Model):
	latitude = models.FloatField()
	longitude = models.FloatField()
	depth = models.FloatField()
	magnitude = models.FloatField()
	date = models.DateTimeField()

	def __str__(self):
		return str(self.date)

	class Meta:
		verbose_name = 'Землетрясение'
		verbose_name_plural = 'землетрясения'