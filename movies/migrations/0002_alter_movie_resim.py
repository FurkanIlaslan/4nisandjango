# Generated by Django 4.2.3 on 2023-10-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='resim',
            field=models.FileField(blank=True, null=True, upload_to='filmler/', verbose_name='Film Resmi'),
        ),
    ]
