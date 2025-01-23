from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

@login_required
def Home(request):
    return render(request, 'index2.html')

def RegisterView(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        # email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request,"Username already exists!")

        # if User.objects.filter(email=email).exists():
        #     user_data_has_error = True
        #     messages.error(request,"Email already exists!")

        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, "Password must be at least 5 characters")

        if password != confirm_password:
            user_data_has_error = True
            messages.error(request, "Passwords do not match")

        if user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = password
            )
            messages.success(request, "Account created. Login now")
            return redirect('login')
        
    return render(request, 'register.html')

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect('login')
    return render(request, 'login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')

def ForgotPassword(request):
    if request.method == "POST":
        email = request.POST.get('username')

        try:
            user = User.objects.get(username=email)

            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})
            
            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'
            
            email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'
        
            email_message = EmailMessage(
                'Reset your password', # email subject
                email_body,
                settings.EMAIL_HOST_USER, # email sender
                [email] # email  receiver 
            )

            email_message.fail_silently = True
            email_message.send()

            return render(request, 'password_reset_sent.html')
        
        except User.DoesNotExist:
            messages.error(request, f"No user with email '{email}' found")
            return redirect('forgot-password')
    return render(request, 'forgot_password.html')

def PasswordResetSent(request, reset_id):
    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
    else:
        messages.error(request, "Invalid reset id")
        return redirect('forgot-password')

def ResetPassword(request, reset_id):
    try:
        password_reset_id = PasswordReset.objects.get(reset_id=reset_id)

        expiration_time = password_reset_id.created_when + timezone.timedelta(seconds=2)
        if timezone.now() > expiration_time:
            print(timezone.now(), expiration_time)
            messages.error(request, 'Reset link has expired')
            password_reset_id.delete()
            return redirect('reset-password', reset_id=reset_id)

        if request.method == "POST":
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            password_has_error = False

            if password != confirm_password:
                password_has_error = True
                messages.error(request, "Passwords do not match")
            if len(password) < 5:
                password_has_error = True
                messages.error(request, "Password must be at least 5 characters")


            if not password_has_error:
                user = password_reset_id.user
                user.set_password(password)
                user.save()

                password_reset_id.delete()
                messages.success(request, 'Password reset. Proceed to login')
                return redirect('login')
            else:
                return redirect('reset-password', reset_id=reset_id)

    except PasswordReset.DoesNotExist:
        messages.error(request, "invalid reset id")
        return redirect('forgot-password')
    return render(request, 'reset_password.html')
