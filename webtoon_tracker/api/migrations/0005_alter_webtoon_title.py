# Generated by Django 3.2.4 on 2021-06-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_author_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtoon',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
