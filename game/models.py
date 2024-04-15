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
    text_for_email = models.TextField(verbose_name='Описание для писем отправки')
    meta_image = models.ImageField(upload_to='images/meta/')
    site_name = models.CharField(verbose_name=_('Название сайта'), max_length=255, help_text=_('The name of the website'))
    logo = models.FileField(verbose_name=_('Logo'), upload_to='logos/', blank=True, null=True,
                            help_text=_('The logo of the website'))
    footer_logo = models.FileField(verbose_name=_('Footer Logo'), upload_to='logos/', blank=True, null=True)
    favicon = models.FileField(verbose_name=_('Favicon'), upload_to='favicons/', blank=True, null=True,
                               help_text=_('The favicon of the website'))
    default_meta_description = models.TextField(verbose_name=_('Default Meta Description'),
                                                help_text=_('Default meta description for SEO'), max_length=20000)
    default_meta_keywords = models.CharField(verbose_name=_('Default Meta Keywords'), max_length=255,
                                             help_text=_('Default meta keywords for SEO'))


    class Meta:
        verbose_name = _('Настройки сайта')
        verbose_name_plural = _('Настройки сайта')


class Game(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/catalog/', verbose_name='Изображение')
    image_bg = models.ImageField(upload_to='images/catalog_no_bg/', verbose_name='Изображение на фон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог игр'
        ordering = ['-created_at']


class Feature(models.Model):
    image = models.ImageField(upload_to='images/features/', verbose_name='Изображение')
    title = models.CharField(max_length=123, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ['-created_at']


class About(SingletonModel):
    title = models.CharField(max_length=234, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    file = models.FileField(upload_to='files/about_us/', verbose_name='Видео')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class News(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/news/%Y/%m/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Review(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/review/%Y/%m/', blank=True, null=True, verbose_name='Изображение')
    video = models.FileField(upload_to='files/reviews/', blank=True, null=True, verbose_name='Видео')
    created_at = models.DateTimeField(verbose_name='Дата создание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']


class Phone(models.Model):
    number = models.CharField(max_length=123, verbose_name='Номер телефона')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class Contacts(SingletonModel):
    phones = models.ManyToManyField(Phone, verbose_name='Номера')
    address = models.CharField(max_length=123, verbose_name='Адрес')
    instagram = models.URLField(blank=True, null=True, verbose_name='Инстраграм')
    telegram = models.URLField(blank=True, null=True, verbose_name='Телеграмм')
    whatsup = models.URLField(blank=True, null=True, verbose_name='Вотсап')
    vk = models.URLField(blank=True, null=True, verbose_name='Вк')
    youtube = models.URLField(blank=True, null=True, verbose_name='Ютуб')
    facebook = models.URLField(blank=True, null=True, verbose_name='Фейсбук')
    address_link = models.URLField(verbose_name='Ссылка на адрес')
    address_iframe = models.TextField(verbose_name='iframe')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Application(models.Model):
    fullname = models.CharField(max_length=123, verbose_name='Полное имя')
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(max_length=123, verbose_name='Номер телефона')
    comment = models.TextField(blank=True, default='Пусто', verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return f'Заявка от - {self.fullname}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


class SiteContent(models.Model):
    original_text = models.TextField(verbose_name="Оригинальный текст",
                                     help_text="Оригинальный текст, который отображается на сайте.",
                                     max_length=20000
                                     )
    current_text = models.TextField(
        verbose_name="Текущий текст",
        help_text="Измененный или текущий текст, который отображается на сайте.",
        max_length=20000
    )

    class Meta:
        verbose_name = "Контент сайта"
        verbose_name_plural = "Контент сайта"


class HomeImage(models.Model):
    image = models.ImageField(upload_to='images/home/')

    class Meta:
        verbose_name = 'Дом изображении'
        verbose_name_plural = 'Дом изображении'
