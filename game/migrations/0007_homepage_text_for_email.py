# Generated by Django 5.0.4 on 2024-04-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_review_image_alter_review_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='text_for_email',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
