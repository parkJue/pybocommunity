# Generated by Django 3.1.3 on 2022-11-25 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_auto_20221125_0209'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=40, null=True)),
                ('imgfile', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', models.TextField()),
            ],
        ),
    ]
