# Generated by Django 3.1.1 on 2021-02-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210204_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AddField(
            model_name='about',
            name='about_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
