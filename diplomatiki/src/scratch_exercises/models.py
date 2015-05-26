# encoding: utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    """
    A model class describing a category.
    """
    name = models.CharField(u'Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Description', blank=True)

    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'

    def __unicode__(self):
        return self.name
		
class Question(models.Model):
    """
    A model describing a coobook recipe.
    """
    DIFFICULTY_EASY = 1
    DIFFICULTY_MEDIUM = 2
    DIFFICULTY_HARD = 3
    DIFFICULTIES = (
        (DIFFICULTY_EASY, u'easy'),
        (DIFFICULTY_MEDIUM, u'normal'),
        (DIFFICULTY_HARD, u'hard'),
    )
    title = models.CharField(u'Title', max_length=255)
    slug = models.SlugField(unique=True)
    image=models.ImageField(upload_to='photos', default='C:\pollsSite\mysite\media\photos\scratch logo.jpg')
    difficulty = models.SmallIntegerField(u'Difficulty',
        choices=DIFFICULTIES, default=DIFFICULTY_MEDIUM)
    category = models.ManyToManyField(Category, verbose_name=u'Κατηγορίες')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Author')
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = u'Άσκηση'
        verbose_name_plural = u'Άσκήσεις'
        ordering = ['-date_created']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Question, self).save(*args, **kwargs)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
	
    class Meta:
        verbose_name = u'Epilogi'
        verbose_name_plural = u'Epiloges'
        

    def __unicode__(self):
        return self.choice_text
