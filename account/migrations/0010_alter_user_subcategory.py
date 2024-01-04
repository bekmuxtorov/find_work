# Generated by Django 4.2 on 2024-01-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_alter_work_district'),
        ('account', '0009_tokenproxy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subcategory',
            field=models.ManyToManyField(blank=True, related_name='users', to='work.subcategory'),
        ),
    ]