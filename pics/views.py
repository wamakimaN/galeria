from django.shortcuts import render
from .models import Picture,Category

# Create your views here.
def home_page(request):

  title = 'home'
  categories = Category.all_categs()
  pics = Picture.all_pics()
  return render(request, 'homepage.html', {"title":title,"pics":pics, "categories":categories})