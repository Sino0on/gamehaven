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
    title = models.CharField(max_length=123)
    text_for_email = models.TextField()


    class Meta:
        verbose_name = _('Константа')
        verbose_name_plural = _('Константы')


class Game(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/catalog/')
    image_bg = models.ImageField(upload_to='images/catalog_no_bg/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог игр'
        ordering = ['-created_at']


class Feature(models.Model):
    image = models.ImageField(upload_to='images/features/')
    title = models.CharField(max_length=123)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
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
        verbose_name_plural = 'О нас'


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
    image = models.ImageField(upload_to='images/review/%Y/%m/', blank=True, null=True)
    video = models.FileField(upload_to='files/reviews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']


class Phone(models.Model):
    number = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class Contacts(SingletonModel):
    phones = models.ManyToManyField(Phone)
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
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


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


