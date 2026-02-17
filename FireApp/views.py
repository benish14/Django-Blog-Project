from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Category, Post, AboutUS
from django.core.paginator import Paginator
from .forms import ContactForm, ForgotPasswordForm, LoginForm, RegisterForm, ResetPasswordForm,PostForm
import logging
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail

#create your views here

#posts=[
    #{'id':1,'title':'Post 1', 'content': ' content of post 1',},
    #{'id':2,'title':'Post 2', 'content': ' content of post 2',},
    #{'id':3,'title':'Post 3', 'content': ' content of post 3',},
    #{'id':4,'title':'Post 4', 'content': ' content of post 4',}]
def index(request):
    block_title="Latest Post"
    # getting data from POst model
    all_posts=Post.objects.all()
    
    #paginate
    paginator=Paginator(all_posts, 5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    return render(request,'index.html', {
        'block_title': block_title,
        'page_obj': page_obj
        })
    
def detail(request, slug):
    #static data
   # post=next((item for item in posts if item['id'] == post_id), None)
   
   #get data by using id
   post=Post.objects.get(slug=slug)
   related_posts= Post.objects.filter(category= post.category).exclude(pk=post.id)
   # logger=logging.getLogger("TESTING")
   # logger.debug(f'post variable is {post}')
   return render(request,'detail.html',{"post":post, "related_posts": related_posts})
    
def old_url_redirect(request):
    return redirect(reverse('blog:new_page_urls' ))

def new_url_view(request):
    return HttpResponse("Hello new Urls")



def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')

        logger=logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'POST data is { form.cleaned_data['name']} { form.cleaned_data['email']} { form.cleaned_data['message']}')
            success_message='Your Email has been Send!'
            return render(request,'contact.html', {'form':form,'sucess_messag':success_message})

        else:
            logger.debug('Form Validation Error')
        return render(request,'contact.html', {'form':form,'name':name, 'email':email, 'message':message})    
    return render(request,'contact.html')

def about(request):
    about_content=AboutUS.objects.first()
    if about_content is None or not about_content.content:
        about_content= "Default content goes here."  #default text
    else:
        about_content= about_content.content
    return render(request,'about.html',{'about_content':about_content})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False) #user data created
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration Successfull. You can log in')
            return redirect("blog:login")
            
        
    return render(request, 'register.html', {'form':form})

def login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user= authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                print("LOGIN SUCCESS")
                return redirect("blog:dashboard")
           
    return render(request, 'login.html',{'form':form})

def dashborad(request):
    blog_title="My Posts"
    #getting user posts
    all_posts=Post.objects.filter(user=request.user)
    #paginate
    paginator=Paginator(all_posts, 5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    return render(request, 'dashboard.html',{"blog_title":blog_title, 'page_obj': page_obj})

def logout(request):
    auth_logout(request)
    return redirect("blog:index")

def forget_password(request):
    form=ForgotPasswordForm()
    if request.method=='POST':
        form=ForgotPasswordForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            user= User.objects.get(email=email)
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            current_site=get_current_site(request)
            domain=current_site.domain
            subject="Reset Password Requested"
            message= render_to_string('reset_password_email.html', {
                'domain':domain,
                'uid':uid,
                'token':token,
            })
            
            send_mail(subject, message, 'noreply@benish.com', [email])
            messages.success(request, 'Email has been send')
    return render(request, 'forget_password.html',{'form':form})

def reset_password(request, uidb64, token):
    form=ResetPasswordForm()
    if request.method=='POST':
        #form
        form=ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password=form.cleaned_data['new_password']
            try:
               uid= urlsafe_base64_decode(uidb64)
               user= User.objects.get(pk=uid)
            except(TypeError, ValueError, OverflowError ,User.DoesNotExist):
               user=None
            if user is not None and default_token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been reset successfully!')
                return redirect('blog:login')
            else:
                messages.error(request, 'The password reset link is invalid')
    return render(request, 'reset_password.html', {'form':form} )

def new_post(request):
    categories = Category.objects.all()
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:dashboard')

    return render(request, 'new_post.html', {
        'form': form,
        'categories': categories
    })




