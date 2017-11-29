from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Bug(models.Model):
	employee_id = models.PositiveIntegerField(blank = False)
	message		= models.TextField(max_length = 1000,blank = False)
	reason		= models.TextField(max_length = 1000,blank = True)
	record_stat = models.CharField(max_length = 1,default = 'O')
	date_time	= models.DateTimeField()

	def __str__(self):
		return str(self.pk) + "  " + str(self.employee_id) + " " + str(self.message) + " " + str(self.date_time)

	def mesage_neat(self):
		return self.message[1:100]


