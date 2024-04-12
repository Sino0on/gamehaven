from django.contrib import admin
from django.contrib.admin import StackedInline

from game.models import HomePage, Game, About, News, Review, Contacts, Application, Phone, Feature


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id', )


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
