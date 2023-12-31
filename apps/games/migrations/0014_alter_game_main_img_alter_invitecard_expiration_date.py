# Generated by Django 4.2.3 on 2023-07-24 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_alter_invitecard_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='main_img',
            field=models.ImageField(default='games/pexels-borja-lopez-1346154.jpg', upload_to='games/', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 23, 14, 1, 51, 959505), verbose_name='дата истечения'),
        ),
    ]
