from django import forms
from .models import Article, TimePeriod, Album, Photo


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'prev', 'text', 'photo')
        labels = {
            'title': 'Название',
            'prev': 'Аннотация',
            'text': 'Содержание',
            'photo': 'Обложка',
        }


class TimePeriodForm(forms.ModelForm):

    class Meta:
        model = TimePeriod
        fields = ('start_date', 'end_date', 'description')
        labels = {
            'start_date': 'Дата начала',
            'end_date': 'Дата окончания',
            'description': 'Название события'
        }


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('name', 'description')
        labels = {
            'name': 'Название',
            'description': 'Описание'
        }


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('photo',)
        labels = {'photo': 'Изображение'}
