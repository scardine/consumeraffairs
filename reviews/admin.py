from django.contrib import admin

# Register your models here.
from reviews.models import Review, Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("nome",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("date_submitted", "author", "title", "company", "rating")


admin.site.register(Company, CompanyAdmin)
admin.site.register(Review, ReviewAdmin)
