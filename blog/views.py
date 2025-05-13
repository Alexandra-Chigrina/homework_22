from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 1

    # def get_queryset(self):
    #     return Blog.objects.filter(is_published=True).order_by("-created_at")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
