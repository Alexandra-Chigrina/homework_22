import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from config.settings import EMAIL_HOST_USER
from users.forms import CustomUserCreationForm, ProfileUpdateForm
from users.models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email_confirm/{token}/"

        message = (
            f"Здравствуйте!\n\n"
            f"Спасибо за регистрацию на нашем сайте.\n"
            f"Пожалуйста, подтвердите ваш адрес электронной почты, перейдя по ссылке:\n\n{url}\n\n"
            f"Если вы не регистрировались, просто проигнорируйте это письмо.\n\nС уважением, команда сайта."
        )

        send_mail(
            subject="Подтверждение почты",
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("users:profile_edit")

    def get_object(self, queryset=None):
        return self.request.user

