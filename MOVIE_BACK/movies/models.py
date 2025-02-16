from django.db import models
# from django.contrib.auth import get_user_model
# settings.AUTH_USER_MODEL = get_user_model()

from django.urls import reverse

from django.conf import settings

from django_random_queryset import RandomManager


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Keyword(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.content}'


class Movie(models.Model):

    objects = RandomManager()

    title = models.CharField(max_length=100, default='')
    titleEng = models.CharField(max_length=100, default='')
    director = models.CharField(max_length=50, default='')
    actors = models.CharField(max_length=100, default='')
    nation = models.CharField(max_length=50, default='')
    plot = models.TextField()
    runtime = models.CharField(max_length=50, default='')
    genre1 = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_main_genre'
        )
    genre2 = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_sub_genre'
        )
    ratingGrade = models.CharField(max_length=50, default='')
    releaseDt = models.CharField(max_length=50, default='')
    descriptions = models.CharField(max_length=100, default='')
    poster = models.CharField(max_length=100, default='')
    stills = models.TextField()
    awards = models.TextField()
    keyword1 = models.ForeignKey(
        Keyword,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_main_keyword'
        )
    keyword2 = models.ForeignKey(
        Keyword,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_sub_keyword1'
        )
    keyword3 = models.ForeignKey(
        Keyword,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_sub_keyword2'
        )

    def genre1_name(self):
        return Genre.objects.get(id=self.genre1.id).name

    def genre2_name(self):
        return Genre.objects.get(id=self.genre1.id).name

    def keyword1_content(self):
        if self.keyword1:
            return Keyword.objects.get(id=self.keyword1.id).content

    def keyword2_content(self):
        if self.keyword2:
            return Keyword.objects.get(id=self.keyword2.id).content

    def keyword3_content(self):
        if self.keyword3:
            return Keyword.objects.get(id=self.keyword3.id).content

    def __str__(self):
        return f'{self.id}: {self.title}'


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.BooleanField()
    comment = models.CharField(max_length=100)
    keyword1 = models.ForeignKey(Keyword, null=True, on_delete=models.SET_NULL, related_name='rating_main_keword')
    keyword2 = models.ForeignKey(Keyword, null=True, on_delete=models.SET_NULL, related_name='rating_sub_keyword')

    def keyword1_content(self):
        if self.keyword1:
            return Keyword.objects.get(id=self.keyword1.id).content

    def keyword2_content(self):
        if self.keyword2:
            return Keyword.objects.get(id=self.keyword2.id).content 

    def __str__(self):
        return f'{self.id} => by: {self.user.id} {self.keyword1} || {self.keyword2} || {self.comment}'
