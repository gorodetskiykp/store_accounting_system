# Generated by Django 4.1.1 on 2022-09-17 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=10, null=True, verbose_name='Объем')),
                ('title', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Объем ведра',
                'verbose_name_plural': 'Объемы ведер',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Наименование')),
                ('netto', models.IntegerField(null=True, verbose_name='Чистый вес')),
                ('brutto', models.IntegerField(null=True, verbose_name='Грязный вес')),
                ('volume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='buh.volumes')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['id'],
            },
        ),
    ]
