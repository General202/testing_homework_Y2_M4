# Generated by Django 5.2.1 on 2025-05-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_alter_post_options_alter_post_unique_together'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['title', 'user_email'], name='testingssss_title_a3ac99_idx'),
        ),
    ]
