from django.db import models

class User(models.Model):
	name=models.CharField(max_length=50)
	password=models.CharField(max_length=10)
	phone=models.CharField(max_length=10)
	email=models.CharField(max_length=50)
	class Meta:
		db_table='user'

class Expence(models.Model):
	time=models.TimeField()
	date=models.DateField()
	remark=models.CharField(max_length=100)
	amount=models.FloatField()
	category=models.CharField(max_length=50)
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	class Meta:
		db_table='expence'

class Income(models.Model):
	time=models.TimeField()
	date=models.DateField()
	remark=models.CharField(max_length=100)
	amount=models.FloatField()
	category=models.CharField(max_length=50)
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	class Meta:
		db_table='income'

