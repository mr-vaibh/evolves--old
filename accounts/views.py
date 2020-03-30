from django.shortcuts import render, redirect
from .forms import RegistrationForm, EditProfileForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
	return render(request, 'accounts/index.html')


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			form = RegistrationForm()
			messages.success(request, 'New user created successfully.')
			return redirect('/accounts/login')
	else:
		form = RegistrationForm()

	context = {'form': form}
	return render(request, 'accounts/register.html', context)


# def login(request):
#     return render(request, 'accounts/login.html')

@login_required
def editProfile(request):
	if request.method == 'POST':
		edituser_form = EditProfileForm(request.POST, instance=request.user)
		editprofile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

		if edituser_form.is_valid() and editprofile_form.is_valid():
			edituser_form.save()
			editprofile_form.save()
			return redirect('/accounts')
	else:
		edituser_form = EditProfileForm(instance=request.user)
		editprofile_form = UserProfileForm(instance=request.user.userprofile)

	context = {'edituser_form': edituser_form, 'editprofile_form': editprofile_form}
	return render(request, 'accounts/edit-profile.html', context)


@login_required
def changePass(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/accounts/edit')
	else:
		form = PasswordChangeForm(user=request.user)
	context = {'form': form}
	return render(request, 'accounts/change-password.html', context)