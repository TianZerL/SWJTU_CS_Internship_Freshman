# Generated by Django 2.2.3 on 2019-07-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='favorte',
            field=models.ManyToManyField(blank=True, related_name='my_favor_post', to='main_page.post'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='follow_sb', to='main_page.userinfo'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='my_posts',
            field=models.ManyToManyField(blank=True, related_name='my_post', to='main_page.post'),
        ),
    ]
