# Generated by Django 3.2 on 2021-04-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users_avatar/', verbose_name='Аватар'),
        ),
    ]