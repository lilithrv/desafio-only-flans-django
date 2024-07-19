from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest 
from .models import Flan, ContactForm, ContactFormModelForm
from .forms import ContactFormForm, SignUpForm
from django.contrib import messages

# Create your views here.
def home(request):
    flanes = Flan.objects.filter(is_private=False)
    context = {
        "flanes": flanes
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
       'flanes_privados': flanes_privados
    }
    return render(request, 'welcome.html',context)

def contact(request):
    # if request.method  == 'POST':
    #     form = ContactFormForm(request.POST)

    #     if form.is_valid():
    #         contact_form = ContactForm.objects.create(**form.cleaned_data)
    #         return HttpResponseRedirect('exito')

    # else:
    #     form= ContactFormForm()
    
    if request.method  == 'POST':
        form = ContactFormModelForm(request.POST)

        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('exito')

    else:
        form= ContactFormModelForm()
    
    context = {
        'form': form
    }

    return render(request, 'contact.html',  context)

def exito(request):
    return render(request, 'exito.html')

def logout_view(request):
    logout(request)
    return redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()  
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión')
            return redirect('/accounts/login')  
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

