from django.contrib import admin
from .models import EvaluationRequest

class EvaluationRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'contact_method', 'created_at')
    list_filter = ('contact_method', 'created_at')
    search_fields = ('description', 'user__username')

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(EvaluationRequest, EvaluationRequestAdmin)
