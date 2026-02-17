from django.contrib import admin
from .models import Post, Category, AboutUS



class PostAdmin(admin.ModelAdmin):
    list_filter=('category',)
    search_fields=('title', 'content')
    
#Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUS)