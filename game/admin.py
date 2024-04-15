from django.contrib import admin
from django.contrib.admin import StackedInline

from game.models import HomePage, Game, About, News, Review, Contacts, Application, Phone, Feature, SiteContent


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('site_name', )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', )


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', )


class PhoneInline(StackedInline):
    model = Phone
    extra = 0


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')
    search_fields = ('number', )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'created_at')
    search_fields = ('fullname', )


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    # inlines = [PhoneInline]


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('current_text', 'original_text')  # Display these fields in the list view
    readonly_fields = ('original_text',)  # Prevent modification of the original text
    search_fields = ('original_text', 'current_text')  # Allow searching by both original and current text

    fieldsets = (
        (None, {
            'fields': ('original_text', 'current_text'),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('original_text',)
        return self.readonly_fields

