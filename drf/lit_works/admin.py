from django.contrib import admin

from lit_works.models import *

admin.site.site_header = "Панель администрирования"
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(LitWork)
