# Generated by Django 5.0.4 on 2024-04-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_alter_homepage_options_homepage_meta_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/home/')),
            ],
            options={
                'verbose_name': 'Дом изображении',
                'verbose_name_plural': 'Дом изображении',
            },
        ),
    ]
