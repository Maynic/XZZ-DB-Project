# Generated by Django 4.2 on 2023-04-25 00:18

from django.db import migrations

def create_data(apps, schema_editor):
    Visitor = apps.get_model('data_models', 'xzz_visitor')
    Visitor(1, 'John Smith', 'john.smith@example.com', '1975-06-30', 5551234567,  '123 Main St', 'Anytown', 'CA', 12345, 'IN' ).save()
    # (visitor_id, visitor_name, email, birth_date, phone, address, city, state, zip, visitor_type)


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
