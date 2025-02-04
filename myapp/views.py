from django.shortcuts import render, HttpResponse, redirect
from .models import todoList, item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.timezone import now
from datetime import timedelta
from .models import fitur, education, databs, experience, contact

# Create your views here.
def home(request):
    '''
    context = {
        'title': 'Selamat datang di web ini',
        'nama': 'FikWeb'
    }  
    '''
    feature = fitur
    feature.nama = 'FikWeb'
    feature.about = 'Web dalam tahap pengembangan. Bertujuan untuk pembelajaran'
    return render(request, 'index.html', {'fitur': feature})



def kontak(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pesan = request.POST['pesan']
        
        if contact.objects.filter(email=email).exists():
            messages.info(request, 'anda sudah kontak sebelumnya')
            return redirect('kontak')
        else:
            
            contact.objects.create(
                nama=username,
                email=email,
                message=pesan,
                
            )
            messages.success(request, 'berhasil dikirim')
    return render(request, 'contact.html')

def masuk(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'account NOT FOUND')
            return redirect('login')
        
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['user']
        email = request.POST['email']
        pw = request.POST['password']
        confirmpw =request.POST['repeatpw']
        if pw == confirmpw:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email sudah ada')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'User sudah ada')
                return redirect('register')
        
            else:
                user = User.objects.create_superuser(username=username, email=email, password=pw)
                user.save();
                return redirect('resume')
        else: 
            messages.info('error')
            return redirect(request, 'register')
        
    
    
    return render(request, 'register.html')

def out(request):
    logout(request)
    return redirect('/')

def resume(request):
    pendidikan = education.objects.all()
    experiencee = experience.objects.all()
    
    
    

    return render(request, 'resume.html',{'pendidikan': pendidikan,'pengalaman': experiencee})

def project(request):
    show = True
    return render(request, 'projects.html', )

'''def counter(request):
    words = request.POST['text']
    get = meminta data dari server atau mengambil
    post = mengirim data ke server, dont show in urls link
    put = mengubah seluruh data yang ada di server
    patch = change some exits data in server
    delete = detele all the fvkng data in server
    jumlah = len(words.split())
    return render(request, 'counter.html', {'amount': jumlah})
    #penghitung jumlah kata
'''