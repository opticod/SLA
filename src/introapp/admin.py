from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import SignUp
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated","full_name","roll"]
	form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)

admin.site.unregister(User)
class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]
admin.site.register(User, UserProfileAdmin)