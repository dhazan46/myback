# Generated by Django 5.0.1 on 2024-01-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
