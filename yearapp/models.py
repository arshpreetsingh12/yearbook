from django.db import models
from django.contrib.auth.models import User
import datetime
from django_countries.fields import CountryField


# Create your models here.


class Profile(models.Model):
	user=models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	country = models.CharField(max_length=25,blank=True,null=True)
	state = models.CharField(max_length=25)
	company_name = models.CharField(max_length=100, blank=True,null=True)
	website = models.CharField(max_length=100, blank=True,null=True)
	paypal_email = models.EmailField(max_length=100,blank=True,null=True)
	phone = models.CharField(max_length=15,blank=True,null=True)
	billing_address = models.TextField(max_length=200,blank=True,null=True) 
	address = models.TextField(max_length=50,blank=True,null=True) 
	city = models.CharField(max_length=25,blank=True,null=True)
	Zip = models.CharField(max_length=25,blank=True,null=True)
	credit_card_number = models.CharField(max_length=15,blank=True,null=True)
	expiration_date = models.CharField(max_length=15,blank=True,null=True)
	cvv = models.CharField(max_length=5,blank=True,null=True)
	company_logo = models.FileField(blank=True, upload_to='media')
	business_license = models.FileField(blank=True, upload_to='media')
	about_seller = models.CharField(max_length=50,  blank=True,null=True)
	terms_condition = models.BooleanField(null=True,blank=True,default=False)

	def __str__(self):
		return self.user.username



class ForgetPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    code = models.CharField(max_length=100, blank=True, null=True, verbose_name='Code')

    def __str__(self):
        name = self.user.first_name + self.user.last_name
        return name




class Invitation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
	name_of_venue = models.CharField(max_length=50,blank=True,null=True)
	website = models.CharField(max_length=100,blank=True,null=True)
	address = models.TextField(max_length=200,blank=True,null=True)
	country = models.CharField(max_length=25,blank=True,null=True)
	state = models.CharField(max_length=25,blank=True,null=True)
	city = models.CharField(max_length=25,blank=True,null=True)
	postal_code = models.CharField(max_length=25,blank=True,null=True)
	telephone = models.CharField(max_length=15,blank=True,null=True)

	def __str__(self):
		return self.name_of_venue



class SetEvent(models.Model):
	invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE, verbose_name='Invitation')
	title = models.CharField(max_length=25,blank=True,null=True)
	description = models.TextField(max_length=200,blank=True,null=True)
	tickets_sale_end = models.DateTimeField(auto_now_add=False)
	event_start = models.DateTimeField(auto_now_add=False)
	event_end = models.DateTimeField(auto_now_add=False)
	open_door = models.TimeField(blank = True, null = True)


# class SeatsAndPrice(models.Model):
# 	set_event = models.ForeignKey(SetEvent, on_delete=models.CASCADE, verbose_name='SetEvent')
# 	ticket_type = models.CharField(max_length=25,blank=True,null=True)
# 	seat_type = 


	












