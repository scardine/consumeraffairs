from django.contrib import admin

# Register your models here.
from reviews.models import Review, Company


class CompanyAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Review, ReviewAdmin)
