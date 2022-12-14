# Generated by Django 4.1.1 on 2022-09-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buh', '0007_addresses_naklad_zakaz_naklad_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addresses',
            options={'ordering': ['id'], 'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.RemoveField(
            model_name='volumes',
            name='volume',
        ),
        migrations.RemoveField(
            model_name='naklad',
            name='address',
        ),
        migrations.AddField(
            model_name='naklad',
            name='address',
            field=models.ManyToManyField(to='buh.addresses'),
        ),
    ]
