from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from .forms import BookForm
from django.template.loader import render_to_string



def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_create(request):
    data = dict()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = BookForm()
        
    context = {'form': form}
    html_form = render_to_string('partial_book_create.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form': html_form})