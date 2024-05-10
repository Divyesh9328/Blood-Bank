# Generated by Django 4.2.6 on 2023-10-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_bloodrequest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='progress',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Reject', 'Reject')], default='Pending', max_length=30),
        ),
    ]
