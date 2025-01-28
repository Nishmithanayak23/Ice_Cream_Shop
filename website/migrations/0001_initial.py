# Generated by Django 5.1.2 on 2024-11-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.IntegerField()),
                ('price', models.FloatField()),
                ('image_url', models.CharField(max_length=2083)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]
