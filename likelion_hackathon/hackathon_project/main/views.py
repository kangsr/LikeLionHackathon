from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import Book, Free
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def home(request):
    books = Book.objects.all()
    frees = Free.objects.all()
    return render(request,'main.html', {'books':books, 'frees':frees})

def select(request):
    return render(request, 'select.html')

def new_fiction(request):
    return render(request, 'new_fiction.html')

def new_poetry(request):
    return render(request, 'new_poetry.html')

def new_nonfiction(request):
    return render(request, 'new_nonfiction.html')

def new_essay(request):
    return render(request, 'new_essay.html')

def new_free(request):
    return render(request, 'new_free.html')


    
def create_fiction(request):
    new_book = Book()
    new_book.genre = "fiction"
    new_book.title = request.POST['title']
    new_book.writer = request.POST['writer']
    new_book.author=request.user
    new_book.read_date = request.POST['read_date']
    new_book.question1 = request.POST['question1']
    new_book.question2 = request.POST['question2']
    new_book.question3 = request.POST['question3']
    new_book.question4 = request.POST['question4']
    new_book.question5 = request.POST['question5']
    new_book.save()
    return redirect('home')

def create_poetry(request):
    new_book = Book()
    new_book.genre = "poetry"
    new_book.title = request.POST['title']
    new_book.writer = request.POST['writer']
    new_book.author=request.user
    new_book.read_date = request.POST['read_date']
    new_book.question1 = request.POST['question1']
    new_book.question2 = request.POST['question2']
    new_book.question3 = request.POST['question3']
    new_book.question4 = request.POST['question4']
    new_book.question5 = request.POST['question5']
    new_book.save()
    return redirect('home')

def create_nonfiction(request):
    new_book = Book()
    new_book.genre = "nonfiction"
    new_book.title = request.POST['title']
    new_book.writer = request.POST['writer']
    new_book.author=request.user
    new_book.read_date = request.POST['read_date']
    new_book.question1 = request.POST['question1']
    new_book.question2 = request.POST['question2']
    new_book.question3 = request.POST['question3']
    new_book.question4 = request.POST['question4']
    new_book.question5 = request.POST['question5']
    new_book.save()
    return redirect('home')

def create_essay(request):
    new_book = Book()
    new_book.genre = "essay"
    new_book.title = request.POST['title']
    new_book.writer = request.POST['writer']
    new_book.author = request.user
    new_book.read_date = request.POST['read_date']
    new_book.question1 = request.POST['question1']
    new_book.question2 = request.POST['question2']
    new_book.question3 = request.POST['question3']
    new_book.question4 = request.POST['question4']
    new_book.question5 = request.POST['question5']
    new_book.save()
    return redirect('home')

def createFree(request):
    new_book = Free()
    new_book.title = request.POST['title']
    new_book.writer = request.POST['writer']
    new_book.author=request.user
    new_book.read_date = request.POST['read_date']
    new_book.question1 = request.POST['question1']
    new_book.save()
    return redirect('home')

def detail(request,id):
    
    book=get_object_or_404(Book,pk=id)
    return render(request,'detail.html',{'book':book})


def editBook(request, id):
    edit_book = Book.objects.get(id=id)
    return render(request,'editBook.html',{'book':edit_book})

def updateBook(request, id):
    update_book = Book.objects.get(id = id)
    update_book.title = request.POST['title']
    update_book.writer = request.POST['writer']
    update_book.read_date = request.POST['read_date']
    update_book.question1 = request.POST['question1']
    update_book.question2 = request.POST['question2']
    update_book.question3 = request.POST['question3']
    update_book.question4 = request.POST['question4']
    update_book.question5 = request.POST['question5']
    update_book.save()
    return redirect('detail', update_book.id)

def deleteBook(request, id):
    delete_book = Book.objects.get(id = id)
    delete_book.delete()
    return redirect('home')

def editFree(request, id):
    edit_free = Free.objects.get(id = id)
    return render(request, 'editFree.html', {'free':edit_free})

def updateFree(request, id):
    update_free = Free.objects.get(id = id)
    update_free.title = request.POST['title']
    update_free.writer = request.POST['writer']
    update_free.read_date = request.POST['read_date']
    update_free.question1 = request.POST['question1']
    update_free.save()
    return redirect('detailFree', update_free.id)

def detailFree(request,id):
    free=get_object_or_404(Free,pk=id)
    return render(request,'detail_free.html',{'free':free})

def deleteFree(request, id):
    delete_free = Free.objects.get(id=id)
    delete_free.delete()
    return redirect('home')

############로그인관련#############################
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request=request,username=username,password=password)
            
            if user is not None:

                login(request,user)
        return redirect("home")
    else:
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)

    #     if form.is_valid():
    #         user=form.save()
    #         login(request,user)
    #     return redirect("home")

    # else:
    #     form=UserCreationForm()
    #     return render(request,'signup.html',{'form':form})
    if request.method =="POST":
        if request.POST["password"]==request.POST["password2"]:
            user=User.objects.create_user(username=request.POST["username"],password=request.POST["password"])
            auth.login(request,user)
            return redirect('home')
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')



