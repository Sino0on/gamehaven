from django.contrib import admin
from game.models import HomePage, Game, About, News, Review, Contacts, Application


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', )


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
