from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout
from accounts.forms import Login_form,Register_form,DocumentForm

def check_register(request):
    message = "invalid user name"
    if request.POST:
        login_form = Login_form(request.POST)
        registr_form = Register_form(request.POST)
        if registr_form.is_valid():
            user = registr_form.save(commit=False)
            username= registr_form.cleaned_data['username']
            password= registr_form.cleaned_data['password']
            email=registr_form.cleaned_data['email']

            #clear session data before register
            if request.session.get("username"):
                del request.session['username']
            if request.session.get("password"):
                del request.session['password']
            if request.session.get("email"):
                del request.session['email']
            user.set_password(password)
            user.save()
            user = authenticate(username=username,password=password,email=email)

            if user is not None :
                login(request,user)
                request.session['username']=username
                request.session['password']=password
                request.session['email'] = email

                return redirect("/accounts/welcome/")
            else:
                return render(request, 'login.html', {"login_form": login_form, "registr_form": registr_form,"message":message})

        if not registr_form.is_valid():
            return render(request, 'login.html', {"login_form": login_form, "registr_form": registr_form,"message":message})


def login_and_register(request):
    if request.session.get("username"):
        username=request.session.get('username')
        password = request.session.get('password')
        email = request.session.get('email')
        return render(request,"profile.html",{"username":username,"password":password,"email":email})


    login_form = Login_form()
    registr_form = Register_form()
    return render(request, 'login.html', {"login_form": login_form , "registr_form" : registr_form})
def check_login(request):
    if request.POST:
        message = "invalid user name or password"
        login_form = Login_form(request.POST)
        registr_form = Register_form(request.POST)

        if login_form.is_valid():
            username= login_form.cleaned_data['username']
            password= login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['username']=username
                request.session['password']=password
                request.session['email'] = user.email
                print(user.email)
                return redirect("/accounts/welcome/")
            else:
                return render(request, 'login.html', {"login_form": login_form, "registr_form": registr_form,"message":message})

        if not login_form.is_valid():
            return render(request, 'login.html', {"login_form": login_form, "registr_form": registr_form,"message":message})

def logout_view(request):
    print("oOoOoO")
    logout(request)
    print("logout")
    # clear session data
    if request.session.get("username"):
        del request.session['username']
    if request.session.get("password"):
        del request.session['password']
    if request.session.get("email"):
        del request.session['email']
    return HttpResponseRedirect('/accounts/')


def home(request):
    if request.session.get("username"):
        get_profile()
    else :
        return HttpResponseRedirect('/accounts/')


def welcome(request):
    if request.session.get('username'):
        username=request.session.get('username')
        password = request.session.get('password')
        email = request.session.get('email')
        return render(request,"success.html",{"username":username,"password":password,"email":email})
    return HttpResponseRedirect('/accounts/')

def get_profile(request):
    if request.session.get('username'):
        username=request.session.get('username')
        password = request.session.get('password')
        email = request.session.get('email')
        return render(request,"profile.html",{"username":username,"password":password,"email":email})
    return HttpResponseRedirect('/accounts/')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'form_upload.html', {
        'form': form})


