from django.utils import timezone
from faker import Faker
from data_models.models import *

fake = Faker()

for _ in range(25):
    fake_name = fake.name()
    fake_email = fake.email()
    fake_birth_date = fake.date_of_birth(minimum_age=3, maximum_age=90)  # Adjust as necessary
    fake_phone = fake.random_number(digits=10, fix_len=True)
    fake_address = fake.address().replace("\n", ", ").split(',')[0]  # Remove line breaks
    fake_city = fake.city()
    fake_state = fake.state_abbr()
    fake_zip = fake.zipcode()
    fake_visitor_type = fake.random_element(elements=xzz_visitor.visitor_type_choices)

    xzz_visitor.objects.create(
        visitor_name=fake_name,
        email=fake_email,
        birth_date=fake_birth_date,
        phone=str(fake_phone),
        address=fake_address,
        city=fake_city,
        state=fake_state,
        zip=fake_zip,
        visitor_type=fake_visitor_type,
    )
# UPDATE sqlite_sequence SET seq = 0 WHERE sqlite_sequence.name = "data_models_xzz_visitor";
