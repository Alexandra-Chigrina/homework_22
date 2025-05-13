import os

from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from dotenv import load_dotenv

from blog.models import Blog

load_dotenv(override=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()

        if self.object.views_counter == 100:
            send_mail(
                subject="🎉 Поздравляем! Статья набрала 100 просмотров",
                message=f"Ваша статья «{self.object.title}» достигла 100 просмотров!",
                from_email=None,
                recipient_list=[os.getenv("MY_EMAIL_HOST_USER")],
                fail_silently=False,
            )
        return self.object


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "posts"
    paginate_by = 1

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).order_by("-created_at")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blog_form.html"

    def get_success_url(self):
        return reverse("blog:blog_detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
