from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag

# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)


@admin.register(Post)  # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "message",
        "photo_tag",
        "created_at",
        "updated_at",
        "message_length",
        "is_public",
    ]
    list_display_links = ["message"]
    list_filter = ["created_at", "is_public"]
    search_fields = ["message"]

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        else:
            return None

    def message_length(self, post):
        return f"{len(post.message)} char"

    message_length.short_description = "char len"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
