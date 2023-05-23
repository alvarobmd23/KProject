from django.contrib import admin

from users.models import Company, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company)
