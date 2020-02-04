from django.shortcuts import render
from .models import Picture,Category

# Create your views here.
def home_page(request):

  title = 'home'
  categories = Category.all_categs(category)
  pics = Picture.all_pics()
  return render(request, 'homepage.html', {"title":title,"pics":pics, "categories":categories})

def category(request):
  if 'picture' in request.GET and request.GET["picture"]:
    search_term = request.GET.get("picture")
    searched_pictures = Picture.show_by_categs(search_term)
    message = f"{search_term}"

    return render(request,'category.html',{"pictures":searched_pictures, "message":message})

  else:
    message = "You haven't searched for any term"
    return render(request,'category.html',{"message":message})

  