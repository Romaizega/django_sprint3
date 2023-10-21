from django.contrib import admin

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'location',
        'is_published',
        'created_at',
        'category'
    )
    list_editable = (
        'is_pubished',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
