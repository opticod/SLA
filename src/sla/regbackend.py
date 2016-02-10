from registration.backends.default.views import RegistrationView
from introapp.forms import UserProfileRegistrationForm
from introapp.models import UserProfile

class MyRegistrationView(RegistrationView):

    form_class = UserProfileRegistrationForm

    def register(self, request, form_class):
        new_user = super(MyRegistrationView, self).register(request, form_class)
        user_profile = UserProfile()
        user_profile.user = new_user
        user_profile.roll = form_class.cleaned_data['roll']
        user_profile.department = form_class.cleaned_data['department']
        user_profile.semester = form_class.cleaned_data['semester']
        user_profile.save()
        return user_profile