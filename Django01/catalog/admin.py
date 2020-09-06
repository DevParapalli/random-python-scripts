from django.contrib import admin

# Register your models here.

from . models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    
    
# classic method
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth','date_of_death')]
    inline = [BookInline,]
admin.site.register(Author, AuthorAdmin)

# Tabular Inline to add data quickly
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
#decorator method
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    inlines = [BookInstanceInline,]
    
    

    
    
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('author', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )