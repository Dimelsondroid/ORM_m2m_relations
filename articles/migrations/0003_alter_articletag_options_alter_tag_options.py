# Generated by Django 4.1.1 on 2022-10-02 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_articletag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletag',
            options={'ordering': ['is_main']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]
