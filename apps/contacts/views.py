from django.shortcuts import render, redirect

from .forms import ContactForm
from ..blog.models import Category


def contact_view(request):
    categories = Category.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/contact/')
    ctx = {
        'form': form,
        'categories': categories
    }
    return render(request, 'contact.html', context=ctx)
