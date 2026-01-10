from django.shortcuts import render, get_object_or_404
from .models import Conquista, Noticia, Bibliografia


def index(request):
    conquistas = Conquista.objects.all()
    noticias = Noticia.objects.all()
    bibliografia = Bibliografia.objects.order_by('-created_at').first()
    return render(request, 'index.html', {'conquistas': conquistas, 'noticias': noticias, 'bibliografia': bibliografia})


def conquistas_list(request):
    conquistas = Conquista.objects.all()
    return render(request, 'conquistas.html', {'conquistas': conquistas})


def conquista_detail(request, slug):
    conquista = get_object_or_404(Conquista, slug=slug)
    return render(request, 'conquista_detail.html', {'conquista': conquista})

from .models import Noticia


def noticia_detail(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, 'noticia_detail.html', {'noticia': noticia})

from .models import Bibliografia


def bibliografia_detail(request, slug):
    bibliografia = get_object_or_404(Bibliografia, slug=slug)
    blocks = bibliografia.blocks.all()
    return render(request, 'bibliografia_detail.html', {'bibliografia': bibliografia, 'blocks': blocks})


from django.http import JsonResponse
from django.db.models import Q


def search_ajax(request):
    q = request.GET.get('q', '').strip()
    data = {'noticias': [], 'conquistas': []}
    if q:
        noticias = Noticia.objects.filter(Q(title__icontains=q) | Q(text__icontains=q)).order_by('-created_at')[:5]
        conquistas = Conquista.objects.filter(Q(title__icontains=q) | Q(text__icontains=q)).order_by('-created_at')[:5]
        for n in noticias:
            data['noticias'].append({
                'title': n.title,
                'slug': n.slug,
                'created_at': n.created_at.strftime('%d/%m/%Y'),
            })
        for c in conquistas:
            data['conquistas'].append({
                'title': c.title,
                'slug': c.slug,
                'created_at': c.created_at.strftime('%d/%m/%Y'),
            })
    return JsonResponse(data)


def search_results(request):
    q = request.GET.get('q', '').strip()
    noticias = Noticia.objects.none()
    conquistas = Conquista.objects.none()
    if q:
        noticias = Noticia.objects.filter(Q(title__icontains=q) | Q(text__icontains=q)).order_by('-created_at')
        conquistas = Conquista.objects.filter(Q(title__icontains=q) | Q(text__icontains=q)).order_by('-created_at')
    return render(request, 'search_results.html', {'q': q, 'noticias': noticias, 'conquistas': conquistas})
