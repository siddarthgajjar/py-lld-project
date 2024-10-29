from django.contrib import admin
from mysite.models import User, Product

admin.site.register(Product)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	fields = ["name", "email"]
	list_display = ["name", "email"]
	search_fields = ["name"]