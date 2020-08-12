from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForm
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/details.html'


def post_list(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'blog/list.html', {'filter': f})


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ('title', 'text')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')
