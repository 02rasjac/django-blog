# Generated by Django 3.1.5 on 2021-01-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]