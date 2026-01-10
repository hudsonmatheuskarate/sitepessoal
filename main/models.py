from django.db import models
from django.utils.text import slugify


class Conquista(models.Model):
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True, blank=True)
    text = models.TextField('Texto')
    image = models.ImageField('Imagem', upload_to='conquistas/')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Conquista'
        verbose_name_plural = 'Conquistas'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # auto-generate unique slug from title if not provided
        if not self.slug:
            base = slugify(self.title)[:190]
            slug = base
            i = 1
            while Conquista.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('conquista_detail', args=[self.slug])


class Noticia(models.Model):
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True, blank=True)
    text = models.TextField('Texto')
    image = models.ImageField('Imagem', upload_to='noticias/', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # auto-generate unique slug from title if not provided
        if not self.slug:
            from django.utils.text import slugify
            base = slugify(self.title)[:190]
            slug = base
            i = 1
            while Noticia.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('noticia_detail', args=[self.slug])


class Bibliografia(models.Model):
    title = models.CharField('Título', max_length=200, default='Bibliografia')
    slug = models.SlugField('Slug', max_length=200, unique=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Bibliografia'
        verbose_name_plural = 'Bibliografias'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:190]
            slug = base
            i = 1
            while Bibliografia.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bibliografia_detail', args=[self.slug])


class BibliografiaBlock(models.Model):
    TYPE_PARAGRAPH = 'paragraph'
    TYPE_IMAGE = 'image'
    TYPE_YOUTUBE = 'youtube'
    BLOCK_TYPES = [
        (TYPE_PARAGRAPH, 'Parágrafo'),
        (TYPE_IMAGE, 'Imagem'),
        (TYPE_YOUTUBE, 'YouTube (link embed)'),
    ]

    bibliografia = models.ForeignKey(Bibliografia, related_name='blocks', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    block_type = models.CharField('Tipo', max_length=20, choices=BLOCK_TYPES, default=TYPE_PARAGRAPH)
    text = models.TextField('Texto', blank=True, null=True)
    image = models.ImageField('Imagem', upload_to='bibliografia/', blank=True, null=True)
    youtube_url = models.CharField('URL YouTube', max_length=400, blank=True, null=True,
                                   help_text='Cole o link do YouTube (ex: https://www.youtube.com/watch?v=...) ou share link.')

    class Meta:
        ordering = ['order']
        verbose_name = 'Bloco de Bibliografia'
        verbose_name_plural = 'Blocos de Bibliografia'

    def __str__(self):
        return f"{self.get_block_type_display()} ({self.bibliografia.title})"

    def youtube_embed_src(self):
        """Retorna a URL de embed para iframes a partir do youtube_url armazenado."""
        if not self.youtube_url:
            return ''
        url = self.youtube_url.strip()
        # suportar formatos como https://www.youtube.com/watch?v=ID ou https://youtu.be/ID
        import re
        m = re.search(r'(?:v=|youtu\.be/)([A-Za-z0-9_-]{6,})', url)
        if m:
            vid = m.group(1)
            return f'https://www.youtube.com/embed/{vid}'
        return url
