# Generated by Django 3.1.3 on 2020-11-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20201122_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='profile_pic',
            field=models.ImageField(blank=True, default=3, upload_to='new_post/'),
            preserve_default=False,
        ),
    ]
