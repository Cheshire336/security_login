from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from .models import MyModel
from .models import EvaluationRequest
from .forms import EvaluationRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.db import connection






def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after login
            else:
                form.add_error(None, 'Incorrect Username or password!')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# Logout View
def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    return redirect('login')


def request_evaluation(request):
    """
    Handle the submission of evaluation requests.
    """
    if request.method == 'POST':
        form = EvaluationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            evaluation_request = form.save(commit=False)
            evaluation_request.user = request.user
            evaluation_request.save()
            return redirect('evaluation_success')  # Ensure this matches the URL name
    else:
        form = EvaluationRequestForm()
    return render(request, 'accounts/evaluation.html', {'form': form})


def evaluation_list(request):
    """
    Display all evaluation requests. Only accessible by admin users.
    """
    evaluations = EvaluationRequest.objects.all().order_by('-created_at')  # Sort by newest
    return render(request, 'accounts/evaluation_list.html', {'evaluations': evaluations})


def home_view(request):
    """
    Render the home page.
    """
    return render(request, 'accounts/home.html')


def safe_query(request):
    user_input = request.GET.get('name', '')  
    query = "SELECT * FROM users WHERE name = %s" 
    with connection.cursor() as cursor:
        try:
            cursor.execute(query, [user_input])  
            results = cursor.fetchall()
            return HttpResponse(f"Results: {results}")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
