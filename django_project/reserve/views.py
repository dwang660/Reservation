from django.shortcuts import render
from .forms import PostForm
# Create your views here.
def new(request):
    if request.method == "POST":
        form = PostForm(request.Post)
    else:
        form = PostForm()
    return render(request, "posts/new.html",{"form":form})
