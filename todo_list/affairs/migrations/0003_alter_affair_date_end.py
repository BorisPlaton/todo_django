# Generated by Django 4.0.4 on 2022-04-19 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0002_alter_affair_options_alter_affair_date_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affair',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]
