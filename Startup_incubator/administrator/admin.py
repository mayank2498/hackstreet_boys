from django.contrib import admin
from .models import Documents
from .models import Updates,Fund,Incubation,AssignMentor,Milestones
# Register your models here.
admin.site.register(Documents)
# Register your models here.
admin.site.register(Updates)
admin.site.register(Fund)
admin.site.register(Incubation)
admin.site.register(AssignMentor)
admin.site.register(Milestones)


