from django import forms
from registration.forms import RegistrationForm
from .models import SignUp
from django.forms import ModelForm
from registration.forms import RegistrationFormUniqueEmail
from django import forms

class UserProfileRegistrationForm(RegistrationForm):
    roll = forms.CharField()
    dep_choice = (
    	('CSE', 'CSE'),
    	('EE', 'EE'),
    	('ME', 'Mechanical'),
   	 	('CE', 'Civil'),
   	 	('CH','Chemical'),
    		
	)
    department = forms.ChoiceField(choices=dep_choice)
    semester = forms.FloatField()
	
    def clean_semester(self):
    	semester = self.cleaned_data.get('semester')
    	if semester>8 or semester<1:
    		raise forms.ValidationError("Please enter correct semester number")
    	return semester
    
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email','roll','department','semester']
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		#domain, extension = provider.split('.')
		#if not domain == 'iitp':
		# 	raise forms.ValidationError("Please make sure you use your IITP email.")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

	def clean_roll(self):
		roll = self.cleaned_data.get('roll')
		return roll

	def clean_department(self):
		department = self.cleaned_data.get('department')
		return department

	def clean_semester(self):
		semester = self.cleaned_data.get('semester')
		return semester
