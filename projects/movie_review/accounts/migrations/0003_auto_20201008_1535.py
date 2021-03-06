# Generated by Django 3.1.2 on 2020-10-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_followings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
