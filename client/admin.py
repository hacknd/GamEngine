from django.contrib import admin
from .models import *

admin.site.register(Member)
admin.site.register(Community)
admin.site.register(Tournament)
admin.site.register(Bookmarks)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Follow)

