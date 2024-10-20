from django.contrib import admin
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets =[
    (None, {
        "Field":["question_text"]
    }),
    ('Data Information', {"field":['pub_date'],'classes':['collapse']})
    ]
    inline = [ChoiceInline]
    list_display =('question_text','pub_date')
    list_filter =('pub_date')
    search_field=('question_text')


admin.site.register(Question)
admin.site.register(Choice)