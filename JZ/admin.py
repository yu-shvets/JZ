from django.contrib import admin
from .models import Project, Image, About, Feedback

# Register your models here.
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Feedback)


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(About, AboutAdmin)