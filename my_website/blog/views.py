from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    #1. Get all Post objects from the database and order them
    all_posts = Post.objects.all().order_by('-id')
    
    # 2. Send them to a template called 'post_list.html'
    # We'll create this template in the next step.
    return render(request, 'blog/post_list.html', {'posts': all_posts})
