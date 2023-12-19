from django.contrib import admin
from .models import emps, testimonial

# Register your models here.

class emp_admin(admin.ModelAdmin):
    list_display = ("name", "is_working", "phone")
    list_editable = ("is_working", "phone")
    search_fields = ("name",)


admin.site.register(emps, emp_admin)
admin.site.register(testimonial)



