# Generated by Django 4.1.1 on 2022-09-29 18:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buh', '0011_alter_volumes_options_customers_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='naklad',
            options={'ordering': ['-date'], 'verbose_name': 'Накладная', 'verbose_name_plural': 'Накладные'},
        ),
        migrations.RemoveField(
            model_name='naklad',
            name='address',
        ),
        migrations.RemoveField(
            model_name='naklad',
            name='zakaz',
        ),
        migrations.AddField(
            model_name='zakaz',
            name='naklad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='buh.naklad', verbose_name='Накладная'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='naklad',
            name='date',
            field=models.DateField(default=datetime.date(2022, 9, 30), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='volume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='buh.volumes', verbose_name='Объем'),
            preserve_default=False,
        ),
    ]