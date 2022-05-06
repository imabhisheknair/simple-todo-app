from django.contrib import admin
from .models import Todolist
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class MyClassAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at', 'deleted')
    list_display = ('title', 'description', 'status', 'created_at', 'modified_at', 'deleted')
    search_fields = ('title', 'description')

    list_filter = ("status", 'deleted')
    actions = ["download_csv"]
    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        f = open('data.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(['title', 'description', 'status', 'created_at', 'modified_at'])

        for s in queryset:
            writer.writerow([s.title, s.description, s.status, s.created_at, s.modified_at])

        f.close()

        f = open('data.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=todo-list.csv'
        return response
    download_csv.short_description = "Download CSV for selected todolists"


admin.site.register(Todolist, MyClassAdmin)