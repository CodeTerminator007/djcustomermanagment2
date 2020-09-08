# Generated by Django 3.1.1 on 2020-09-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='address',
            field=models.CharField(default='address here', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='profile_pic',
            field=models.ImageField(blank=True, default='defaultprofile.jpg', null=True, upload_to=''),
        ),
    ]