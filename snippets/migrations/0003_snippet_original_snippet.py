# Generated by Django 3.0.8 on 2020-07-08 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='original_snippet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='copied_snippets', to='snippets.Snippet'),
        ),
    ]
