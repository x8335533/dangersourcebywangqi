from django.contrib import admin

# Register your models here.

from checksource.models import Checkproblem,Inquireproblem,ImgProblem
admin.site.register(Checkproblem)
admin.site.register(Inquireproblem)
admin.site.register(ImgProblem)
