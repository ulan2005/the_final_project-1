# Generated by Django 3.2.9 on 2021-11-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0004_alter_logistic_field_name_sum'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
    ]
