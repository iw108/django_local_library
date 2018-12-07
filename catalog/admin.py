from django.contrib import admin
from catalog.models import Author, Genre, Language, Book, BookInstance


# Register your models here.
# admin.site.register(Book)
# admin.site.register(BookInstance)

# register the admin classes for Book
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]


# register the admin classes for BookInstance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')

    list_filter = ('status', 'due_back')

    fieldsets = (
    	(None, {
    		'fields' : ('book', 'imprint', 'id')
    	}),
        ('Availability', {
        	'fields': ('status', 'due_back', 'borrower')
        })
    )


class BooksInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
	list_display = (
		'last_name', 'first_name', 'date_of_birth', 'date_of_death'
	)

	fields = [
	    'first_name', 'last_name', ('date_of_birth', 'date_of_death')
	]
	
	inlines = [BooksInline]


# register the admin class with associated model
# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)

