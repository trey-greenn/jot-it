# Generated by Django 3.2.5 on 2023-01-08 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aiprompt', '0002_rename_body_prompt_prompt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prompt',
            name='title',
        ),
    ]
