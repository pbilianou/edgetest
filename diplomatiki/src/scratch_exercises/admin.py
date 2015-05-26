from django.contrib import admin
from .models import Category, Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':['name']}
	
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':['title']}
    inlines=[ChoiceInline]
	
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)

