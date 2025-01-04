from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from .models import Comment
from .forms import CommentForm

@login_required
def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('blog_detail', pk=blog.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

