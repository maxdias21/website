# Generated by Django 4.2.16 on 2024-09-08 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_rename_matiral_status_authors_marital_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile/photo_profile'),
        ),
    ]
