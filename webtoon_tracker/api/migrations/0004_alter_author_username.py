# Generated by Django 3.2.4 on 2021-06-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210606_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
