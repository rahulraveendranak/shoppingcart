# Generated by Django 3.1.1 on 2020-09-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]