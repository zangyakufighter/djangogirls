from django.contrib import admin
from .models import Post

# modelをAdminページ(管理画面)上から参照できるようにする
admin.site.register(Post)