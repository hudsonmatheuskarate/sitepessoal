from django.contrib import admin
from .models import Conquista


@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)

from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)

from .models import Bibliografia, BibliografiaBlock


class BibliografiaBlockInline(admin.StackedInline):
    model = BibliografiaBlock
    extra = 1
    fields = ('order', 'block_type', 'text', 'image', 'youtube_url')


@admin.register(Bibliografia)
class BibliografiaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)
    inlines = (BibliografiaBlockInline,)
