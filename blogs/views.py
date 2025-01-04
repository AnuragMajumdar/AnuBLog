from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Blog

class HomeView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
    paginate_by = 10

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
    paginate_by = 10

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('blog_detail')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
