# Generated by Django 2.0.3 on 2018-04-18 14:23

from django.db import migrations
from member_types.models import MemberType

def insert_defaults(apps, schema_editor):
    MemberType(name="Student").save()
    MemberType(name="Professional").save()
    MemberType(name="Executive").save()

class Migration(migrations.Migration):

    dependencies = [
        ('member_types', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_defaults)
    ]
