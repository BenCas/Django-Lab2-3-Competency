from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Comics

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class ComicsInline(admin.ModelAdmin):
    model = Comics


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Comics)