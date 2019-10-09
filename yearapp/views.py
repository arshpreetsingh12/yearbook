from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from random import *
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
from django.utils.html import strip_tags




class Homepage(TemplateView):
	template_name = '1000-TICKETS-HOME_PAGE.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})
	
class MultipleEnvent(TemplateView):
	template_name = '1100-TICKETS-MULTIPLE_EVENT_LIST_DISPLAY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


	
class EventDetails(TemplateView):
	template_name = '1110-TICKETS-EVENT_DETAILS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class Aboutus(TemplateView):
	template_name = '1201-NAV_BAR-ABOUT.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class Whyus(TemplateView):
	template_name = '1202-NAV-BAR-WHY-US.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class NavBar(TemplateView):
	template_name = '1203-NAV-BAR-FAQ.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class ContactUs(TemplateView):
	template_name = '1204-NAV-BAR-CONTACT.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})




class Terms(TemplateView):
	template_name = '1205-NAV-BAR-TERMS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class Privacy(TemplateView):
	template_name = '1206-NAV-BAR-PRIVACY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class Blog(TemplateView):
	template_name = '1207-NAV-BAR-BLOG.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class SingleBlog(TemplateView):
	template_name = '1207-NAV-BAR-SINGLE-BLOG.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class Registration(TemplateView):
	template_name = '1300-NAV-BAR-LOGIN-RESTRATION.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


	def post(self, request, *args, **kwargs):

		# Get Parent Info
		parent_fname=request.POST.get("parent_fname")
		parent_lname=request.POST.get("parent_lname")
		parent_email=request.POST.get("parent_email")
		parent_password=request.POST.get("parent_password")
		country=request.POST.get("parent_country")
		state=request.POST.get("parent_state")
		terms = request.POST.get("terms")

	
		try:
			user=User.objects.get(email=parent_email)
			messages.info(request,"User already Exist.")
			return HttpResponseRedirect("registration")

		except User.DoesNotExist:
			parent=User.objects.create_user(
				username=parent_email,
				email=parent_email,
				password=parent_password
				)
			parent.first_name=parent_fname
			parent.last_name=parent_lname
			
			parent.is_active=True
			parent.save()
			parent.set_password('password')
			
			profile=Profile(user=parent,country=country,state=state,terms_condition=terms)
			messages.success(request, 'Successfully Register.')
			profile.save()
			
			login(request, parent,backend='django.contrib.auth.backends.ModelBackend')
			return HttpResponseRedirect("multiple_event")

		



class Login(View):
	def post(self, request, *args, **kwargs):
			email = request.POST.get('email')
			password = request.POST.get('password')
			print(">>>>password",password)
			try:
				user= User.objects.get(email=email)
				userauth = authenticate(username=user.username, password=password)
				
				if userauth:
					login(request, user,backend='django.contrib.auth.backends.ModelBackend')
					if request.user.is_authenticated:
						return HttpResponseRedirect('multiple_event')
					else:
						return HttpResponseRedirect('registration')
				else:
					
					messages.error(request,'Incorrect password given.')
					return HttpResponseRedirect('registration')

			except Exception as e:
				print(e)
				messages.error(request,'Incorrect email address given.')
				return HttpResponseRedirect('registration')

class LogoutView(View):
	def get(self,request,*args, **kwargs):
		logout(request)
		return HttpResponseRedirect('/')

	

class ForgetPass(TemplateView):
	template_name = '1310-NAV-BAR-FORGET-PASSWORD.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

	def post(self, request, *args, **kwargs):
		email=self.request.POST.get('forget_email')
		
		try:
			user = User.objects.get(email=email)
			code = randint(100000, 999999) 
			
			fg_pwd = ForgetPassword(user_id=user.id,code=code)
			fg_pwd.save()
			link = settings.BASE_URL+"/confirm_email/"+str(code)
			print(link)
			content_html = render_to_string("forget_password.html", {'link':link})
			
			recipients = [email]		
			subject = "Reset Password"
			send_status=send_mail(subject , content_html, 'redexsolutionspvtlmt@gmail.com',recipients)
		
			if send_status:
				messages.success(request,'Your request has been received.Please look for an email from yearbook of Code for more'+ 'details.Thank you.')
			else:
				messages.error(request,'Some error occur. Retry or contact with administrator.')

		except User.DoesNotExist:
		 	messages.error(request,'This email address is not registred.')
		except Exception as e:
		 	print(str(e))
		 	messages.error(request,'Some error occur. Retry or contact with administrator.')
		return HttpResponseRedirect('forget_password')
		

class ConfirmEmail(TemplateView):
	template_name = '1320-NAV BAR-ENTER-NEW-PASSWORD.html'
	def get(self, request, *args, **kwargs):
		code=kwargs.get('code')
		# print(">>>>",code)
		return render(request,self.template_name,locals())
	
	def post(self,request,*args, **kwargs):
		email=request.POST.get("email")
	#	print(">>>>",email)
		code=kwargs.get('code')
	#	print(">>post",code)
		try:
			user=User.objects.get(email=email)
			code=ForgetPassword.objects.get(code=conf_code)
			print(">>>>",code)
			if user and code:
				return HttpResponseRedirect('reset_password/'+conf_code)
			else:
				messages.error(request,'Invaild Email or Code.')
				return HttpResponseRedirect('/confirm_email/'+str(code))
		except Exception as e:
			# raise e
			messages.error(request,'Invaild Email or Code.')
			return HttpResponseRedirect('confirm_email')


class ResetPassword(View):
	template_name = '1320-NAV BAR-ENTER-NEW-PASSWORD.html'
	def get(self, request, *args, **kwargs):
		code=kwargs.get('code')
		return render(request,self.template_name,locals())

	def post(self, request, *args, **kwargs):
		password = request.POST.get("password")
		code=kwargs.get('code')
		# print(">>>>",password)
		

		try:
			u=ForgetPassword.objects.get(code=code)
		#	print(">>>>>>", u)
			u.user.set_password(password)
			u.user.save()
			messages.success(request,'Password Changed successfully please signin.')
			return HttpResponseRedirect('/registration')
		except Exception as e:
			print(str(e))
			messages.error(request,'Some error occur please try again.')
			return HttpResponseRedirect('/reset_password/'+code)





class AccountInfo(TemplateView):
	template_name = '1208A-TICKETS-DASHBOARD-MY-ACCOUNT-INFORMATION.html'
	def get(self, request, *args, **kwargs):
		print(">>>>>",request.user)
		profile = Profile.objects.get(user=request.user)
		print(">>>",profile)
		return render(request,self.template_name,locals())


	def post(self,request,*args, **kwargs):
		first_name=request.POST.get('fname')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		old_pass=request.POST.get('old_pass')
		new_pass=request.POST.get('pass')
		company_name=request.POST.get('company_name')
		website=request.POST.get('website')
		pay_email=request.POST.get('pay_email')
		phone=request.POST.get('phone')
		billing_address=request.POST.get('billing_add')
		address=request.POST.get('address')
		country=request.POST.get('country')
		state=request.POST.get('state')
		city=request.POST.get('city')
		Zip=request.POST.get('zip')
		cc_number=request.POST.get('cc_number')
		exp_date=request.POST.get('exp_date')
		print("exp_date>>>>>",exp_date)
		terms_condition = request.POST.get('terms')
		print("terms_condition>>>>",terms_condition)
		cvv=request.POST.get('cvv')
		comp_logo=request.FILES.get('logo')
		business_license=request.FILES.get('license')
		about_seller=request.POST.get('txtarea')
		
	

		try:
			user = User.objects.get(id=request.user.id)
			
			# userauth = authenticate(username=user.username, password=old_pass)
			# print("userauth>>>>>>>>>>>>>>>>>>",userauth)
			# if userauth:
			if old_pass=="" and new_pass=="":
				user.first_name=first_name 
				user.last_name=last_name
				user.email=email
			# user.set_password(new_pass) # pass 123456789
				user.save()

				prof=Profile.objects.get(user_id=request.user.id)
				print("prof>>>>>>>>>>>>>>",prof)
				prof.country=country
				prof.company_name=company_name
				prof.website=website
				prof.paypal_email=pay_email
				prof.phone=phone
				prof.billing_address=billing_address
				prof.address=address
				prof.state=state
				prof.city=city
				prof.Zip=Zip
				prof.credit_card_number=cc_number
				prof.expiration_date=exp_date
				prof.cvv=cvv
				prof.about_seller=about_seller
				prof.business_license=business_license
				prof.company_logo=comp_logo
				prof.terms_condition =terms_condition
				prof.save()
				messages.success(request, 'Successfully updated !!!')
				return HttpResponseRedirect('myaccount_info')

			else:
				userauth = authenticate(username=user.username, password=old_pass)
				print("userauth>>>>>>>>>>>>>>>>>>",userauth)
				if userauth:
					user.first_name=first_name 
					user.last_name=last_name
					user.email=email
					user.set_password(new_pass) # pass 123456789
					user.save()

					prof=Profile.objects.get(user_id=request.user.id)
					print("prof>>>>>>>>>>>>>>",prof)
					prof.country=country
					prof.company_name=company_name
					prof.website=website
					prof.paypal_email=pay_email
					prof.phone=phone
					prof.billing_address=billing_address
					prof.address=address
					prof.state=state
					prof.city=city
					prof.Zip=Zip
					prof.credit_card_number=cc_number
					prof.expiration_date=exp_date
					prof.terms_condition =terms_condition
					prof.cvv=cvv
					prof.about_seller=about_seller
					prof.business_license=business_license
					prof.company_logo=comp_logo
					prof.save()

				
					login(request, user,backend='django.contrib.auth.backends.ModelBackend')
					if request.user.is_authenticated:
						messages.success(request, 'Successfully updated.')
						return HttpResponseRedirect('myaccount_info')
					else:
						messages.success(request, 'Your password is not valid')	
						return HttpResponseRedirect('myaccount_info')

			
				else:
					messages.success(request, 'Your password is not valid')		
					return HttpResponseRedirect('myaccount_info')


		except Exception as e:
			print(str(e))
			return HttpResponseRedirect('myaccount_info')



class TicketsSale(TemplateView):
	template_name = '2100-TICKETS-POST_AND_SELL.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

	def post(self,request,*args, **kwargs):
		title = request.POST.get('title')
		description = request.POST.get("description")
		ticket_sale_end = request.POST.get("ticket_sale_end")
		sale_end_hour = request.POST.get('sale_end_hour')
		sale_end_minutes = request.POST.get('sale_end_minutes')
		formate = request.POST.get('formate')
	
		event_start = request.POST.get('event_start')
		event_start_hour = request.POST.get('event_start_hour')
		event_start_minutes = request.POST.get('event_start_minutes')
		event_start_formate = request.POST.get("event_start_formate")
		
		event_end = request.POST.get("event_end")
		event_end_hour = request.POST.get("event_end_hour")
		event_end_minutes = request.POST.get("event_end_minutes")
		event_end_formate = request.POST.get("event_end_formate")
		
		door_open_hour = request.POST.get("door_open_hour")
		door_open_minutes = request.POST.get("door_open_minutes")
		time_formate = request.POST.get("time_formate")


		venue_name = request.POST.get("name_of_venue")
		website = request.POST.get("website")
		country = request.POST.get("country")
		state = request.POST.get("state")
		city = request.POST.get("city")
		address = request.POST.get("address")
		postal_code = request.POST.get("postal_code")
		telephone = request.POST.get("telephone")


		try:
			user = User.objects.get(id=request.user.id)
			
			invitation = Invitation()
			invitation.user_id = user.id
			invitation.name_of_venue = venue_name
			invitation.website = website
			invitation.address = address
			invitation.country = country
			invitation.state = state
			invitation.city = city
			invitation.postal_code = postal_code
			invitation.telephone = telephone
			invitation.save()


			sale_end = ticket_sale_end + " " + sale_end_hour + ":"  + sale_end_minutes + " " + formate
			final_sale_end = datetime.strptime(sale_end, '%Y-%m-%d %I:%M %p')

			event_start_at = event_start + " " + event_start_hour + ":" + event_start_minutes + " " + event_start_formate
			final_event_start_at = datetime.strptime(event_start_at, '%Y-%m-%d %I:%M %p')

			event_end_at = event_end + " " + event_end_hour + ":" + event_end_minutes + " " + event_end_formate
			final_event_end_at = datetime.strptime(event_end_at, '%Y-%m-%d %I:%M %p')

			door_open = door_open_hour + ":" + door_open_minutes + " " + time_formate
			final_door_open = datetime.strptime(door_open, '%I:%M %p')
			
			event = SetEvent()
			event.invitation_id = invitation.id
			event.title = title
			event.description = description
			event.tickets_sale_end = final_sale_end
			event.event_start = final_event_start_at
			event.event_end = final_event_end_at
			event.open_door = final_door_open
			event.save()




			messages.success(request, 'Submit')	
			return HttpResponseRedirect('tickets_sale')


		except Exception as e:
			print(str(e))
			return HttpResponseRedirect('tickets_sale')





class TicketsManage(TemplateView):
	template_name = '2200-TICKETS-MANAGE-POSTING.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class TicketsOrder(TemplateView):
	template_name = '2300-TICKETS-SALES-ORDER.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class OrderHistory(TemplateView):
	template_name = '2400-TICKETS-ORDER-HISTORY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class MyCart(TemplateView):
	template_name = '1120-TICKETS-MY-CART.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class MyOrder(TemplateView):
	template_name = '1130-TICKETS-MY-ORDER.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class MyOrderPNS(TemplateView):
	template_name = '2500-TICKETS-MY-ORDER-PNS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AdminHome(TemplateView):
	template_name = '9000-SUMMARY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class SuperAdmin(TemplateView):
	template_name = '9001-TICKETS-SUPER-ADMIN.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class AddStaff(TemplateView):
	template_name = '9002-ADD-STAFF.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class AddTicketsStaff(TemplateView):
	template_name = '9002-TICKETS-ADD-STAFF.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class TicketsUsers(TemplateView):
	template_name = '9003-TICKETS-USERS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class ManageUser(TemplateView):
	template_name = '9011-TICKETS-MANAGE-CONTENT.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})