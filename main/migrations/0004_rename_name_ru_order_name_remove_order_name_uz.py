# Generated by Django 4.1.7 on 2023-03-03 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_text_aboutus_text_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name_ru',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name_uz',
        ),
    ]
