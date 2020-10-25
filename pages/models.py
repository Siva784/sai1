from django.db import models

# Create your models here.
class Logs_Table(models.Model):
	Farmer=models.CharField(max_length=50)
	Company_Name=models.CharField(max_length=50)
	Date_of_Pay=models.DateField()
	Payment=models.IntegerField()
	Return_Pay_Date=models.DateField(null=True)
	Total_Days=models.IntegerField(null=True)
	Rate_Of_Interest=models.IntegerField(null=True)
	Interest=models.FloatField(null=True)
	Total=models.FloatField(null=True)
	def __str__(self):
		return str(self.Date_of_Pay)

class Investment(models.Model):
	From_Investment=models.CharField(max_length=50)
	Investment_Date=models.DateField(null=True)
	Investment_amount=models.IntegerField()
	def __str__(self):
		return str(self.id)
class Returninvestment(models.Model):
	id1=models.IntegerField(null=True)
	To_Return_Investment=models.CharField(max_length=50)
	Return_Investment_Date=models.DateField(null=True)
	Investment_amount=models.IntegerField()
	def __str__(self):
		return str(self.id)
class Bankinterest(models.Model):
	Pay_Name=models.CharField(max_length=50)
	Paid_Date=models.DateField()
	Amount=models.IntegerField()
	def __str__(self):
		return str(self.id)
class Company(models.Model):
	Com_Name=models.CharField(max_length=50)
	
	def __str__(self):
		return str(self.Com_Name)
	
