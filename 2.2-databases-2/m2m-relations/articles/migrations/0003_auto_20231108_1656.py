# Generated by Django 3.1.2 on 2023-11-08 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_tag_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article_Tag',
            new_name='Scope',
        ),
    ]
