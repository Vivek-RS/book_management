# Generated by Django 5.0.2 on 2024-02-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdetails', '0002_alter_author_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
