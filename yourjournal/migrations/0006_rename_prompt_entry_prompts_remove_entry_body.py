# Generated by Django 4.1 on 2023-01-16 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("yourjournal", "0005_entry_body"),
    ]

    operations = [
        migrations.RenameField(
            model_name="entry", old_name="prompt", new_name="prompts",
        ),
        migrations.RemoveField(model_name="entry", name="body",),
    ]
