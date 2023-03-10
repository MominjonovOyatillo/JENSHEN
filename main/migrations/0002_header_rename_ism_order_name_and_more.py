# Generated by Django 4.1.7 on 2023-03-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_uz', models.CharField(max_length=255)),
                ('text_ru', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='media/')),
                ('button', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ism',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='phone',
            new_name='number',
        ),
    ]
