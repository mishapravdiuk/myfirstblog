# Generated by Django 4.0.4 on 2022-04-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_text', models.CharField(max_length=1000)),
                ('post_image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
