# Generated by Django 4.2 on 2024-01-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='users/default.jpg', upload_to='users/', verbose_name='Rasm'),
        ),
    ]
