# Generated by Django 2.0 on 2018-04-18 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('reversion_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputrequestrevision',
            name='logged_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_logged_request',
                                    to='security.InputLoggedRequest', verbose_name='logged request'),
        ),
        migrations.AlterField(
            model_name='inputrequestrevision',
            name='revision',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='input_logged_request',
                                       to='reversion.Revision', verbose_name='revision'),
        ),
    ]
