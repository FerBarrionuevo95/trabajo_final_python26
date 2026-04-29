from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-fecha') # Trae los post más recientes a los más antiguos
    return render(request, "pages/home.html", {"posts": posts})

# Nueva vista de detalle
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "pages/post_detail.html", {"post": post})

# Vista de sobre mi
def about(request):
    return render(request, "pages/about.html")