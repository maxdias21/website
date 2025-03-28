# Generated by Django 4.2.16 on 2024-09-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_news', models.CharField(choices=[('M', 'MainNews'), ('S', 'SecondaryNews'), ('T', 'ThirdNews')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/covers/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='news',
            name='type_news',
            field=models.ManyToManyField(to='news.newstype'),
        ),
    ]
