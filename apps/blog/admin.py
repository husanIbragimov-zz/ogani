from django.contrib import admin

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title',)
    filter_horizontal = ('tag',)
    exclude = ('category', )


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
