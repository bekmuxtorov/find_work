# Generated by Django 4.2 on 2024-01-02 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_district'),
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works', to='account.district', verbose_name='Tuman'),
        ),
    ]