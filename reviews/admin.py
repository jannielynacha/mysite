from django.contrib import admin

from .models import Review, Critic, Link, Multimedia

admin.site.register(Review)
admin.site.register(Critic)
admin.site.register(Link)
admin.site.register(Multimedia)
