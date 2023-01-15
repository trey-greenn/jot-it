# Generated by Django 4.1 on 2023-01-08 21:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("aiprompt", "0003_remove_prompt_title"),
        ("yourjournal", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="entry", name="id",),
        migrations.AddField(
            model_name="entry",
            name="prompt_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="aiprompt.prompt",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="entry",
            name="body",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]