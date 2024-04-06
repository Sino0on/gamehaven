from django.db import models
from django.utils.translation import gettext as _


class SingletonModel(models.Model):
    """
    Модель, которая всегда имеет только один экземпляр.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Если модель уже существует, удалите ее
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Если модель еще не существует, создайте ее
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class HomePage(SingletonModel):
    home_image_1 = models.ImageField(upload_to='images/home/')
    home_image_2 = models.ImageField(upload_to='images/home/')
    home_image_3 = models.ImageField(upload_to='images/home/')
    home_image_4 = models.ImageField(upload_to='images/home/')
    home_image_5 = models.ImageField(upload_to='images/home/')
    home_image_6 = models.ImageField(upload_to='images/home/')
    home_image_7 = models.ImageField(upload_to='images/home/')


    class Meta:
        verbose_name = _('Константа')
        verbose_name_plural = _('Константы')


class Game(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/catalog/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог игр'
        ordering = ['-created_at']


class About(SingletonModel):
    title = models.CharField(max_length=234)
    description = models.TextField()
    file = models.FileField(upload_to='files/about_us/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'О нас'


class News(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    image = models.ImageField(upload_to='images/news/%Y/%m/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Review(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='files/reviews/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']


class Contacts(SingletonModel):
    phone1 = models.CharField(max_length=123)
    phone2 = models.CharField(max_length=123)
    phone3 = models.CharField(max_length=123)
    address = models.CharField(max_length=123)
    instagram = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    whatsup = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    address_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = ''


class Application(models.Model):
    fullname = models.CharField(max_length=123)
    email = models.EmailField()
    phone_number = models.CharField(max_length=123)
    comment = models.TextField(blank=True, default='Пусто')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заявка от - {self.fullname}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


