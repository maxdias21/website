# Generated by Django 4.2.16 on 2024-09-21 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newstype_alter_news_image_news_type_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstype',
            name='type_news',
            field=models.CharField(choices=[('M', 'MainNews'), ('S', 'SecondaryNews'), ('T', 'ThirdNews'), ('N', 'Normal')], max_length=20),
        ),
    ]
