# Generated by Django 4.0.3 on 2022-04-26 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_rename_text_comment_body_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]