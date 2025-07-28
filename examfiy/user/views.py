# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from user.models import CustomUser
from django.contrib.auth.models import Group
from django.contrib import messages  # ⭐ import messages

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_number=request.POST.get('phonenumber')
        last_name=request.POST.get('lastname')
        first_name=request.POST.get('firstname')
        username=request.POST.get('username')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered")
        else:
            user = CustomUser(email=email,phone_number=phone_number,last_name=last_name,first_name=first_name,username=username)
            user.set_password(password1)
            user.save()
            student_group, _ = Group.objects.get_or_create(name='Student')
            user.groups.add(student_group)
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('/exam/')  # or exams page
    
    return render(request, 'user/register.html')

def custom_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()

def is_student(user):
    return user.is_authenticated and user.groups.filter(name='Student').exists()

@login_required
def custom_password_change(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if not request.user.check_password(old_password):
            return render(request, 'user/password_change.html', {'error': 'Current password is incorrect.'})

        if new_password1 != new_password2:
            return render(request, 'user/password_change.html', {'error': 'New passwords do not match.'})

        # Update the password
        request.user.set_password(new_password1)
        request.user.save()
        # Optionally: Log the user back in, or ask them to log in again
        return render(request, 'user/password_change.html', {'success': 'Password changed successfully! Please log in again.'})

    return render(request, 'user/password_change.html')

@login_required
def profile(request):
    return render(request, 'user/profile.html')
