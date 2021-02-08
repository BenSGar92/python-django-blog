from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    #need to specify a get or post request
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #next step will be to log the user in
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
    
    #first POST request check if valid true then redirect to article list page
    #second if it's not a POST request and is a GET request instead go to else statement and create an instance for signup page
    #third is checking validation and if false goes right to rendering the form
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user using the form above and using a built in django function get_user
            user = form.get_user()
            #then we call login that was imported above and (request, user)
            login(request, user)
            #this if statement is connected with the protected /create page and the if statement within login.html to go along with the 'next' syntax
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')