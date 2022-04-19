# Generated by Django 4.0.4 on 2022-04-19 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='affair',
            options={'ordering': ('-date_add',)},
        ),
        migrations.AlterField(
            model_name='affair',
            name='date_end',
            field=models.DateTimeField(blank=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='affair',
            name='text',
            field=models.CharField(blank=True, max_length=2047, verbose_name='Описание'),
        ),
    ]