# Generated by Django 2.0.3 on 2018-06-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compDashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('prof_title', models.CharField(blank=True, max_length=50, null=True)),
                ('degrees', models.CharField(blank=True, max_length=500, null=True)),
                ('research_interests', models.CharField(blank=True, max_length=500, null=True)),
                ('homepage', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('fax', models.CharField(blank=True, max_length=12, null=True)),
                ('office', models.CharField(blank=True, max_length=7, null=True)),
                ('by_mail_or_courier', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='scrapyitem',
            name='unique_id',
        ),
        migrations.AddField(
            model_name='scrapyitem',
            name='event_category',
            field=models.CharField(choices=[('csevent', 'Event'), ('cspresentaion', 'CS Presentaion'), ('lanparty', 'LAN Party')], default='csevent', max_length=9),
        ),
        migrations.AddField(
            model_name='scrapyitem',
            name='event_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='scrapyitem',
            name='event_time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
