from django.contrib import admin
from .models import Post,Category,borrowPost

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

admin.site.register(borrowPost)


