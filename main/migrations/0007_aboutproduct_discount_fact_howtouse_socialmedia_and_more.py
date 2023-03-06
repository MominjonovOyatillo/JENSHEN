# Generated by Django 4.1.7 on 2023-03-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_abouttea'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_uz', models.TextField()),
                ('text_ru', models.TextField()),
                ('img', models.ImageField(upload_to='about_product/')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='discount/')),
            ],
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('text_uz', models.TextField()),
                ('text_ru', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HowToUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255)),
                ('text_uz', models.TextField()),
                ('text_ru', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='social_media/')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WhoUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Aboutus',
            new_name='AboutCompany',
        ),
        migrations.DeleteModel(
            name='Abouttea',
        ),
        migrations.DeleteModel(
            name='Advice',
        ),
        migrations.DeleteModel(
            name='Fakt',
        ),
        migrations.DeleteModel(
            name='Faq',
        ),
        migrations.DeleteModel(
            name='Header',
        ),
        migrations.DeleteModel(
            name='Productfaq',
        ),
        migrations.DeleteModel(
            name='Productinfo',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cost',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='info',
            name='Instagram',
        ),
        migrations.RemoveField(
            model_name='info',
            name='Instagram_img',
        ),
        migrations.RemoveField(
            model_name='info',
            name='facebok',
        ),
        migrations.RemoveField(
            model_name='info',
            name='facebok_img',
        ),
        migrations.RemoveField(
            model_name='info',
            name='telegram',
        ),
        migrations.RemoveField(
            model_name='info',
            name='telegram_img',
        ),
        migrations.RemoveField(
            model_name='info',
            name='youtube',
        ),
        migrations.RemoveField(
            model_name='info',
            name='youtube_img',
        ),
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.RemoveField(
            model_name='product',
            name='logo',
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=1, upload_to='product/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='info',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='info',
            name='text_ru',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='text_uz',
            field=models.TextField(),
        ),
    ]
