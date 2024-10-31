from django.contrib import admin

from .models import Question, Choice, Cat, Price

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Cat)
admin.site.register(Price)


