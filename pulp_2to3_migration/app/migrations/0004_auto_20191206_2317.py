# Generated by Django 2.2.8 on 2019-12-06 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pulp_2to3_migration', '0003_pulp2repository_pulp3_repository_remote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pulp2distributor',
            name='pulp3_publication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Publication'),
        ),
    ]
