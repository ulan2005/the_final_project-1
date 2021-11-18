# Generated by Django 3.2.9 on 2021-11-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0005_hitcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]