from django.contrib import admin
from .models import Post, SubTagEdifici, Tag, TagSeccio

# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(TagSeccio)
admin.site.register(SubTagEdifici)
