# Generated by Django 2.2.5 on 2019-11-04 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0003_usersubmission_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubmission',
            name='language',
            field=models.CharField(choices=[('C', 'C'), ('Python', 'Python'), ('C#', 'C#'), ('C++', 'C++'), ('Java', 'Java'), ('Clojure', 'Clojure'), ('JavaScript', 'JavaScript')], default='Java', max_length=50),
        ),
    ]
