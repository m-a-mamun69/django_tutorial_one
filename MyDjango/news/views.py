from django.shortcuts import render
from .models import Article

# Create your views here.

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "year_archive.html", context)