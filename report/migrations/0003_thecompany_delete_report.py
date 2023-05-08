# Generated by Django 4.1.8 on 2023-04-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_alter_report_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheCompany',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_company', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Отчёт',
                'verbose_name_plural': 'Отчёты',
            },
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]