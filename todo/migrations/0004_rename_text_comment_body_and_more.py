# Generated by Django 4.0.3 on 2022-04-24 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='created_at',
        ),
    ]