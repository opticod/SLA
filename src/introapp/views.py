from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		instance = form.save(commit=False)

		context = {
			"title": "Thank you"
		}

	if request.user.is_authenticated() and request.user.is_staff:
		queryset = SignUp.objects.all().order_by('-timestamp') 
		context = {
			"queryset": queryset
		}

	return render(request, "home.html", context)


