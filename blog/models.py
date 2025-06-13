from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок статьи")
    content = models.TextField(verbose_name="Содержимое", help_text="Основной текст статьи")
    preview = models.ImageField(
        upload_to="blog/previews",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Изображение-превью статьи (необязательно)",
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Количество просмотров статьи (обновляется автоматически)",
        default=0,
    )

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
        ordering = ["title"]
        permissions = [
            ("can_manage_blog", "Может управлять публикациями в блоге"),
        ]

    def __str__(self):
        return self.title
