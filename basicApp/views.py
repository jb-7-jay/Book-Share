from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import DonateBook
from django.contrib import messages 
from .models import Donate

def index(request):
    return render(request,"index.html")

def help(request):
    return render(request,"help.html")

@login_required 
def donate(request):
    # form = DonateBook()
    if request.method == "POST":    
        form = DonateBook(request.POST,request.FILES) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.id = request.user.id   
            instance.save()     
            title = form.cleaned_data.get('title')
            messages.success(request, f'Your Book Is Added')
            return redirect('donate')
    else:
        form = DonateBook()
    return render(request,"donate.html",{ 'form':form })

@login_required
def borrow_list(request):
    form = Donate()
    all_uploads = Donate.objects.all()  
    return render(request, "borrow_list.html",{ 'uploads':all_uploads })

@login_required
def dynamic_lookup_view(request, my_id):
    obj = Donate.objects.get(id=my_id)
    return render(request, 'book_details.html', { 'obj' : obj })