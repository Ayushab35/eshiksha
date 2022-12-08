from django.contrib import admin

from .models import Course,Chapter, FileUpload, YTLink, TextBlock

admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(TextBlock)
admin.site.register(YTLink)
admin.site.register(FileUpload)
# Register your models here.
