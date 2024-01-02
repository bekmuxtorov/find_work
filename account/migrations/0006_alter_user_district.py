# Generated by Django 4.2 on 2024-01-02 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='account.district', verbose_name='Tuman'),
        ),
    ]
