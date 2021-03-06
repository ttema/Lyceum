from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Article, TimePeriod, Photo, Album
from .forms import ArticleForm, TimePeriodForm, PhotoForm, AlbumForm
import datetime


def tape(request):
    articles = Article.objects.all()
    return render(request, 'tape.html', context={'articles': articles})


def view_article(request, pk):
    article = Article.objects.filter(id=pk)
    return render(request, 'view_article.html', context={'article': article})


@login_required
def write_article(request):
    form = ArticleForm
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.prev = request.POST.get('prev')
        article.text = request.POST.get('text')
        if request.FILES.get('photo') is not None:
            article.photo = request.FILES.get('photo')
        article.create_preview()
        article.save()
        return redirect('/')
    return render(request, 'add_article.html', context={'form': form})


@login_required
def del_article(request, pk):
    article = Article.objects.filter(id=pk)
    article.delete()
    return redirect('/')


'''
@login_required
def edit_article(request, pk):
    ed_article = Article.objects.filter(id=pk)
    form = ArticleForm(instance=ed_article[0])
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        article = form.save(commit=False)
        art_id = ed_article[0].id
        article.id = art_id
        article.photo = ed_article[0].photo
        ed_article[0].delete
        article.save()
        return redirect('tape')
    return render(request, 'add_article.html', context={'form': form})
'''


@login_required
def view_periods(request):
    form = TimePeriodForm
    if request.method == 'POST':
        form = TimePeriodForm(request.POST)
        if form.is_valid():
            period = form.save(commit=False)
            period.save()
            return redirect('periods_view')
    periods = TimePeriod.objects.all()
    return render(request, 'date_manager.html', context={'periods': periods, 'form': form})


@login_required
def del_period(request, pk):
    period = TimePeriod.objects.filter(id=pk)
    period.delete()
    return redirect('periods_view')


def view_timetable(request):
    periods = TimePeriod.objects.all()
    current_date = datetime.date.today()
    periods_to_show = []
    for period in periods:
        if period.start_date <= current_date <= period.end_date:
            periods_to_show.append(period)
    if 6 <= current_date.month <= 8:
        week = 'Лето'
    else:
        first_sep = datetime.date(current_date.year, 9, 1)
        days = int(str(current_date - first_sep).split()[0])
        week = days // 7
        if week % 2 == 0:
            week = 'четная'
        else:
            week = 'нечётная'
    return render(request, "timetable.html", context={'periods': periods_to_show, 'week': week})


def add_album(request):
    albums = Album.objects.all()
    form = AlbumForm
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('albums')
    return render(request, "albums.html", context={'albums': albums, 'form': form})


def view_album(request, pk):
    album = Album.objects.filter(id=pk)
    photos = Photo.objects.filter(album__id=album[0].id)
    form = PhotoForm
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.album = album[0]
            photo.save()
    return render(request, "album.html", context={'form': form, 'photos': photos})


@login_required
def del_album(request, pk):
    album = Album.objects.filter(id=pk)
    album.delete()
    return redirect('/albums')
