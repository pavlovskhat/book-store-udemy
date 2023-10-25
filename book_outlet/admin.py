from django.contrib import admin

from .models import Book, Author, Address

# Register your models here.
# https://docs.djangoproject.com/en/4.2/ref/contrib/admin/

class AuthorAdmin(admin.ModelAdmin):
    """
    "Admin" classes add functionality to the admin page
    """
    list_display = ("first_name", "last_name",)

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)  # Cannot work with prepopulated_fields
    prepopulated_fields = {"slug": ("title",)}  # dynamically auto-populates this field based on argument
    list_filter = ("author", "rating",)  # adds a filter section on right hand ribbon
    list_display = ("title", "author",)  # creates columns for each given field

# register if class needs admin attention
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
