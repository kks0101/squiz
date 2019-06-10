from django.contrib import admin
from .models import Test, Question, Options, Score, Response


admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(Score)
admin.site.register(Response)
