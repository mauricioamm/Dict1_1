# Generated by Django 3.2.4 on 2021-06-29 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0004_auto_20210629_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictclass',
            old_name='SuaResposta1',
            new_name='suaresposta1',
        ),
        migrations.RenameField(
            model_name='dictclass',
            old_name='SuaResposta2',
            new_name='suaresposta2',
        ),
        migrations.RenameField(
            model_name='dictclass',
            old_name='SuaResposta3',
            new_name='suaresposta3',
        ),
    ]
