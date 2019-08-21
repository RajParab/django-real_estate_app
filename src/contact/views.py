from django.shortcuts import render,redirect

# Create your views here.
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail as sm
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def contact_details(request):
	contact=Contact.objects.last()

	template='contact/contact_us.html'

	if request.method =='POST':
		contact_form=ContactForm(request.POST)
		if contact_form.is_valid():
			subject=contact_form.cleaned_data['subject']
			email=contact_form.cleaned_data['email']
			message=contact_form.cleaned_data['message']

			try:
				sm(subject, message, email,['test@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid Email ID')

			return redirect('contact:success')
			
	else:
		contact_form=ContactForm(request.POST)


	context={
				'contact':contact,
				'contact_form':contact_form,
	}

	return render(request, template, context)


def success(request):
	return HttpResponse("Message Successfully Sent")