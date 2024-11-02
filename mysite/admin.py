from django.contrib import admin

from mysite.models import User, Product


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	fields = ["title", "name", "email"]
	list_display = ["title", "name", "email"]
	search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "price"]
	search_fields = ["id"]

	fieldsets = (
		("Product Info", {
			"fields": ("seller", "name", "description")	
		}),
		("Stock Info", {
			"fields": ("price", "stock")	
		})
	)
