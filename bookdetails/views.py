from django.shortcuts import render,redirect
from bookdetails.models import Book,Category,Author,City
from django.contrib.auth import authenticate, login, logout
# from .forms import UserCreationForm, LoginForm


def home(request):
    return render(request,'base.html')
 def blank(request):
     pass

def addbooks(request):
    authors = Author.objects.all()
    return render(request, 'addbooks.html', {'authors': authors})
def addauthor(request):

    return render(request, 'addauthor.html')


def submitauthor(request):
    if request.method == 'POST':
        c = City()
        c.city_name = request.POST['city']
        c.save()
        a = Author()
        a.author_name = request.POST['authorname']
        a.city = c
        a.save()
        return redirect('home')


def submitbooks(request):
    if request.method == 'POST':
        b = Book()
        b.book_name = request.POST["bookname"]
        b.description = request.POST["description"]
        b.published_date = request.POST["published_date"]
        b.price = request.POST["price"]
        category_name = request.POST["category"]
        category, created = Category.objects.get_or_create(category_name=category_name)

        author_name = request.POST["author"]
        author, created = Author.objects.get_or_create(author_name=author_name)

        b.category = category
        b.author = author
        b.save()
        return redirect('display_books')



def displaybooks(request):

   books = Book.objects.all()
   data = {'books':books}
   return render(request,'displaybooks.html',data)

def editbooks(request,id):
    if request.method == 'GET':
        b = Book.objects.get(id = id)
        a = Author.objects.all()
        c = City.objects.all()
        data = {'book':b,'authors':a,'cities':c}
        return render(request,'editbooks.html',data)
    else:
        b = Book.objects.get(id = id)
        b.book_name= request.POST['bookname']
        b.description = request.POST['description']
        b.published_date = request.POST['published_date']
        b.price = request.POST['price']
        category_name = request.POST['category']
        category, created = Category.objects.get_or_create(category_name=category_name)
        b.category = category
        author_name = request.POST['author']

        author, created = Author.objects.get_or_create(id=author_name)

        author.save()

        b.author = author
        b.save()
        return redirect('display_books')

def deletebooks(request,id):
    b = Book.objects.get(id = id)
    b.delete()
    b.save()
    return redirect('display_books')




