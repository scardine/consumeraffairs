from django.contrib import admin

# Register your models here.
from reviews.models import Review, Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("date_submitted", "author", "title", "company", "rating")
    list_filter = ("rating",)
    search_fields = ("company", "author", "title",)
    date_hierarchy = "date_submitted"


admin.site.register(Company, CompanyAdmin)
admin.site.register(Review, ReviewAdmin)
