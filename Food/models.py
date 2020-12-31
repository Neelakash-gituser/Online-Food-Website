from django.db import models

# Create your models here.
class Food(models.Model):

	food_id=models.AutoField
	food_name=models.CharField(max_length=50)
	category=models.CharField(max_length=50,default='')
	price=models.IntegerField(default=0)
	food_desc=models.CharField(max_length=300)
	image=models.ImageField(upload_to='static/Food',default='')
   
	def __str__(self):
		return self.food_name
		
class Contact(models.Model):

	msg_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=70,default='')
	message=models.CharField(max_length=500,default='')

   
	def __str__(self):
		return self.name   

class Buy(models.Model):
	food_id=models.AutoField(primary_key=True)
	quantity=models.CharField(max_length=50)
	payment_method=models.CharField(max_length=70,default='')
	price=models.CharField(max_length=500,default='')
	name=models.CharField(max_length=500,default='')
	mobile=models.CharField(max_length=500,default='')
	address=models.CharField(max_length=500,default='')
	city=models.CharField(max_length=500,default='')

	def __str__(self):
		return self.name+" | "+self.price+" | "+self.quantity+" | "+self.address+" | "+self.payment_method




