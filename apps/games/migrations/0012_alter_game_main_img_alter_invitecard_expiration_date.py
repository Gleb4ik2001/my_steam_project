# Generated by Django 4.2.3 on 2023-07-24 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_alter_invitecard_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='main_img',
            field=models.ImageField(default='games/steam.png', upload_to='games/', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 23, 13, 41, 14, 512968), verbose_name='дата истечения'),
        ),
    ]
