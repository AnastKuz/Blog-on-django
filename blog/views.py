from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm

from .models import Post
from .serializers import PostSerializer


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/details.html'


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


"""
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})



from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

class BlogView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('post')

        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post '{}' created successfully".format(post_saved.title)})

    def put(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data.get('post')
        serializer = PostSerializer(instance=saved_post, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()

        return Response({
            "success": "Post '{}' updated successfully".format(post_saved.title)
        })

    def delete(self, request, pk):
        post = get_object_or_404(Post.objects.all(), pk=pk)
        post.delete()
        return Response({
            "message": "Post with id `{}` has been deleted.".format(pk)
        }, status=204)"""
