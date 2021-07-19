from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)  # Post has multiple tags
    is_public = models.BooleanField(default=False, verbose_name="is public content")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        # Java toString
        return self.message

    @property
    def photo_path(self) -> str:
        if self.photo:
            return self.photo.url
        else:
            return ""

    # def message_length(self):
    #     return len(self.message)

    # message_length.short_description = "length of message"

    class Meta:
        ordering = ["-id"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # post_id
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self) -> str:
        return self.name
