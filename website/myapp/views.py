from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Book, Contact, Certificate
from .forms import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    return render(request, 'index.html')

def book(request):
    category_filter = request.GET.get('Category')
    if category_filter:
        category = Category.objects.get(name=category_filter)
        books = Book.objects.filter(category=category)
    else:
        books = Book.objects.all()

    paginator = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book.html', {
        'page_obj': page_obj,
        'category_filter': category_filter
        })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def course(request):
    certificates = Certificate.objects.all()
    return render(request, 'course.html', {'certificates': certificates})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact_info = Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, "Form submitted successfully!")
            return redirect('contact_form')
    else:
        form = ContactForm()
        messages.info(request, "Please use the form to submit your message.")
    return render(request, 'contact.html', {'form': form})

