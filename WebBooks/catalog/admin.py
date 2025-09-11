from django.contrib import admin
from .models import Author, BookInstance, Book, Genre, Status, Language, Publisher
from django.utils.html import format_html

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'photo',
                    'show_photo')
    fields = ['last_name', 'first_name', ('date_of_birth', 'photo')]
    readonly_fields = ["show_photo"]
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;">'
        )
    show_photo.short_description = 'Фото'
admin.site.register(Author, AuthorAdmin)
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author',
                    'show_photo')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]
    readonly_fields = ["show_photo"]
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;">'
        )
    show_photo.short_description = 'Обложка'
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземляр книги', {
            'fields': ('book', 'inv_nom')}),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back')
        }),
    )
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Status)
admin.site.register(Language)
admin.site.register(Publisher)

