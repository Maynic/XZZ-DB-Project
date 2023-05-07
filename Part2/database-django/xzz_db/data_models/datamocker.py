from django.utils import timezone
# from faker import Faker
from data_models.models import *
from decimal import Decimal
from random import randint, uniform
# UPDATE sqlite_sequence SET seq = 0 WHERE sqlite_sequence.name = "xzz_visitor";
# exec(open('/Users/maynic/Developer/XZZ-DB-Project/XZZ-DB-Project/Part2/database-django/xzz_db/data_models/datamocker.py').read())

# fake = Faker()

# for _ in range(25):
#     fake_name = fake.name()
#     fake_email = fake.email()
#     fake_birth_date = fake.date_of_birth(minimum_age=3, maximum_age=90)  # Adjust as necessary
#     fake_phone = fake.random_number(digits=10, fix_len=True)
#     fake_address = fake.address().replace("\n", ", ").split(',')[0]  # Remove line breaks
#     fake_city = fake.city()
#     fake_state = fake.state_abbr()
#     fake_zip = fake.zipcode()
#     fake_visitor_type = fake.random_element(elements=xzz_visitor.visitor_type_choices)

#     xzz_visitor.objects.create(
#         visitor_name=fake_name,
#         email=fake_email,
#         birth_date=fake_birth_date,
#         phone=str(fake_phone),
#         address=fake_address,
#         city=fake_city,
#         state=fake_state,
#         zip=fake_zip,
#         visitor_type=fake_visitor_type,
#     )
visitor_data = [
    (1, 'John Smith', '1975-06-30', 'Individual', '123 Main St', 'Anytown', 'CA', 12345, 'john.smith@example.com', 5551234567),
    (2, 'Jane Doe', '1900-01-15', 'Individual', '456 Elm St', 'Anycity', 'NY', 67890, 'jane.doe@example.com', 5552345678),
    (3, 'David Johnson', '1957-08-10', 'Individual', '789 Oak St', 'Anystate', 'TX', 34567, 'david.johnson@example.com', 5553456789),
    (4, 'Emma Thompson', '2001-05-20', 'Student', '321 Maple Ave', 'Anothercity', 'FL', 23456, 'emma.thompson@example.com', 5554567890),
    (5, 'Oliver Davis', '2015-12-01', 'Member', '654 Cedar St', 'Somecity', 'IL', 45678, 'oliver.davis@example.com', 5555678901),
    (6, 'Sophie Wilson', '1982-02-14', 'Individual', '987 Pine St', 'Anotherstate', 'MI', 56789, 'sophie.wilson@example.com', 5556789012),
    (7, 'Liam Baker', '2008-10-05', 'Student', '246 Oak Ave', 'Anothercity', 'MA', 67890, 'liam.baker@example.com', 5557890123),
    (8, 'Ava Mitchell', '2010-03-27', 'Student', '369 Elm St', 'Somestate', 'PA', 78901, 'ava.mitchell@example.com', 5558901234),
    (9, 'Noah Brown', '2016-07-15', 'Group', '753 Maple St', 'Somewhere', 'OH', 89012, 'noah.brown@example.com', 5559012345),
    (10, 'Isabella Davis', '2005-11-28', 'Member', '852 Pine Ave', 'Anycity', 'VA', 90123, 'isabella.davis@example.com', 5550123456),
    (11, 'William Taylor', '1940-03-01', 'Individual', '963 Oak St', 'Somewhere', 'OR', 23456, 'william.taylor@example.com', 5551234567),
    (12, 'Sophia Wilson', '1998-09-17', 'Student', '741 Maple Ave', 'Anycity', 'WA', 34567, 'sophia.wilson@example.com', 5552345678),
    (13, 'Logan Thomas', '2012-06-22', 'Group', '852 Cedar St', 'Anothercity', 'NJ', 45678, 'logan.thomas@example.com', 5553456789),
    (14, 'Mia Lee', '2018-01-10', 'Group', '159 Oak Ave', 'Somestate', 'MD', 56789, 'mia.lee@example.com', 5554567890),
    (15, 'Ethan Brown', '2006-04-15', 'Student', '753 Pine St', 'Somewhere', 'TX', 67890, 'ethan.brown@example.com', 5555678901),
    (16, 'Madison Garcia', '1955-11-30', 'Individual', '369 Maple St', 'Anystate', 'GA', 78901, 'madison.garcia@example.com', 5556789012),
    (17, 'Jacob Hernandez', '2011-08-18', 'Group', '963 Elm Ave', 'Somewhere', 'CA', 89012, 'jacob.hernandez@example.com', 5557890123),
    (18, 'Abigail Martinez', '2014-01-02', 'Group', '852 Pine St', 'Anothercity', 'NY', 90123, 'abigail.martinez@example.com', 5558901234),
    (19, 'Michael Rodriguez', '1952-12-24', 'Individual', '753 Cedar St', 'Anycity', 'MA', 12345, 'michael.rodriguez@example.com', 5559012345),
    (20, 'Emily Young', '2000-05-10', 'Student', '369 Oak Ave', 'Somestate', 'PA', 23456, 'emily.young@example.com', 5550123456),
    (21, 'Daniel Scott', '2013-02-14', 'Group', '852 Pine Ave', 'Anothercity', 'VA', 34567, 'daniel.scott@example.com', 5551234567),
    (22, 'Madison Perez', '2019-09-17', 'Group', '159 Cedar St', 'Somewhere', 'OH', 45678, 'madison.perez@example.com', 5552345678),
    (23, 'Aiden Roberts', '2010-06-22', 'Student', '753 Oak St', 'Anycity', 'WA', 56789, 'aiden.roberts@example.com', 5553456789),
    (24, 'Samantha Turner', '1945-01-10', 'Individual', '369 Maple Ave', 'Somestate', 'NJ', 67890, 'samantha.turner@example.com', 5554567890),
    (25, 'Alexander Phillips', '1960-04-15', 'Individual', '963 Pine St', 'Anycity', 'MD', 78901, 'alexander.phillips@example.com', 5555678901)
]
for data in visitor_data:
    if data[3] == 'Individual':
        type = 'IN'
    if data[3] == 'Group':
        type = 'GR'
    if data[3] == 'Member':
        type = 'ME'
    if data[3] == 'Student':
        type = 'ST'
    xzz_visitor.objects.create(
        visitor_name=data[1],
        email=data[8],
        birth_date=data[2],
        phone=data[9],
        address=data[4],
        city=data[5],
        state=data[6],
        zip=data[7],
        visitor_type=type,
    )

attraction_data = [ 
    (1, 'The Beast', 'The longest wooden roller coaster in the world', 'RC', 'OP', 36, 137, 4, 'Lot A'),
    (2, 'Jurassic Park River Adventure', 'A thrilling water ride through a prehistoric jungle', 'WR', 'OP', 20, 107, 5, 'Lot A'),
    (3, 'Haunted Mansion', 'A spooky dark ride through a haunted house', 'WR', 'CL', 16, 91, 3, 'Lot B'),
    (4, 'Dumbo the Flying Elephant', 'A gentle kid ride that lets guests soar through the air on a magical elephant', 'KR', 'OP', 32, 76, 2, 'Lot B'),
    (5, 'Millennium Force', 'One of the tallest and fastest roller coasters in the world', 'RC', 'UM', 24, 142, 3, 'Lot C'),
    (6, 'Pirates of the Caribbean', 'A classic dark ride that takes guests on a journey through a pirate-infested Caribbean', 'WR', 'OP', 12, 107, 4, 'Lot C'),
    (7, 'Splash Mountain', 'A thrilling water ride that culminates in a huge drop into a briar patch', 'WR', 'OP', 18, 102, 6, 'Lot D'),
    (8, 'Sesame Street Safari of Fun', 'A colorful kid ride featuring all of your favorite Sesame Street characters', 'KR', 'OP', 30, 61, 2, 'Lot D'),
    (9, 'Kingda Ka', 'The tallest and fastest roller coaster in the world', 'RC', 'CL', 20, 139, 2, 'Lot E'),
    (10, 'Its a Small World', 'A charming dark ride that takes guests on a musical journey around the world', 'WR', 'OP', 24, 91, 8, 'Lot E'),
    (11, 'The Hulk', 'A thrilling roller coaster that takes guests through a series of twists, turns, and inversions', 'RC', 'OP', 30, 137, 3, 'Lot F'),
    (12, 'Kali River Rapids', 'A wet and wild water ride through the heart of the jungle', 'WR', 'UM', 16, 107, 4, 'Lot F'),
    (13, 'Toy Story Midway Mania!', 'A fun-filled ride that lets guests compete in carnival', 'KR', 'OP', 24, 91, 5, 'Lot G'),
    (14, 'Expedition Everest', 'A thrilling roller coaster that takes guests on a journey through the Himalayas', 'RC', 'OP', 20, 122, 4, 'Lot G'),
    (15, 'Harry Potter and the Forbidden Journey', 'A magical dark ride that takes guests on a journey through the world of Harry Potter', 'WR', 'CL', 12, 122, 5, 'Lot H'),
    (16, 'The Cat in the Hat', 'A whimsical kid ride that lets guests join the Cat in the Hat', 'KR', 'OP', 32, 76, 2, 'Lot H'),
    (17, 'The Incredible Hulk Coaster', 'A thrilling roller coaster that takes guests through a series of high-speed inversions and twists', 'RC', 'UM', 30, 137, 3, 'Lot I'),
    (18, 'Journey to Atlantis', 'A water ride that takes guests on a journey through', 'WR', 'OP', 18, 107, 5, 'Lot I'),
    (19, 'Peter Pan''s Flight', 'A classic dark ride that takes guests on a journey through the world of Peter Pan', 'WR', 'OP', 12, 91, 3, 'Lot J'),
    (20, 'Flying Fish', 'A gentle kid ride that lets guests soar through the air on colorful fish', 'KR', 'OP', 24, 76, 2, 'Lot J'),
    (21, 'Top Thrill Dragster', 'A record-breaking roller coaster that launches riders from 0 to 120 mph in just a few seconds', 'RC', 'OP', 20, 137, 1, 'Lot K'),
    (22, 'Raging Rapids', 'A wild water ride that takes guests through turbulent rapids and cascading waterfalls', 'WR', 'CL', 16, 107, 4, 'Lot K'),
    (23, 'Transformers: The Ride 3D', 'A thrilling dark ride that puts guests in the middle of', 'WR', 'OP', 12, 107, 4, 'Lot L'),
    (24, 'The Magic Carpets of Aladdin', 'A fun kid ride that lets guests fly through the air on magical carpets', 'KR', 'OP', 32, 76, 2, 'Lot L'),
    (25, 'Steel Vengeance', 'A record-breaking roller coaster that features a wooden and steel hybrid track', 'RC', 'OP', 24, 137, 2, 'Lot M')
]




for data in attraction_data:
    # print(data)
    xzz_attraction.objects.create(
        attraction_name=data[1],
        attraction_description=data[2],
        attraction_type=data[3],
        attraction_status=data[4],
        capacity=data[5],
        min_height=data[6],
        duration=data[7],
        location=data[8],
    )


show_data = [
  (1, 'The Phantom of the Opera', 'A classic musical about a mysterious masked man and his obsession with a young soprano', 'musical', '2023-04-05 19:30:00', '2023-04-05 22:00:00', 'Yes', 100.00),
  (2, 'Hamlet', 'One of Shakespeare''s most famous plays about a young prince who seeks revenge against his uncle', 'drama', '2023-04-06 19:30:00', '2023-04-06 22:00:00', 'No', 75.00),
  (3, 'The Lion King', 'A beloved musical about a young lion cub''s journey to become king of the Pride Lands', 'musical', '2023-04-07 14:00:00', '2023-04-07 16:30:00', 'Yes', 125.00),
  (4, 'The Addams Family', 'A hilarious comedy about everyone''s favorite spooky family', 'comedy', '2023-04-08 20:00:00', '2023-04-08 22:30:00', 'Yes', 90.00),
  (5, 'Sweeney Todd: The Demon Barber of Fleet Street', 'A dark and thrilling musical about a vengeful barber and his quest for revenge', 'musical', '2023-04-09 19:00:00', '2023-04-09 22:30:00', 'Yes', 110.00),
  (6, 'The Crucible', 'A powerful drama about the Salem witch trials and the hysteria that gripped a community', 'drama', '2023-04-10 18:00:00', '2023-04-10 20:30:00', 'No', 80.00),
  (7, 'Wicked', 'A magical musical that tells the untold story of the witches of Oz', 'musical', '2023-04-11 14:00:00', '2023-04-11 17:00:00', 'Yes', 130.00),
  (8, 'The Book of Mormon', 'A hilarious and irreverent musical about two young missionaries who are sent to Uganda', 'musical', '2023-04-12 19:30:00', '2023-04-12 22:00:00', 'No', 95.00),
  (9, 'Death of a Salesman', 'A classic drama about an aging salesman who struggles to cope with his life and career', 'drama', '2023-04-13 20:00:00', '2023-04-13 22:30:00', 'Yes', 85.00),
  (10, 'The Rocky Horror Picture Show', 'A cult classic musical about a couple who stumble upon a strange castle', 'musical', '2023-04-14 23:00:00', '2023-04-15 01:00:00', 'No', 70.00),
  (11, 'The Exorcist', 'A terrifying horror show about a young girl possessed by a demon', 'horror', '2023-04-15 22:00:00', '2023-04-15 23:00:00','Yes', 120.00),
  (12, 'The Importance of Being Earnest', 'A witty and humorous comedy of manners about two young men who assume false identities', 'comedy', '2023-04-16 15:00:00', '2023-04-16 17:30:00', 'Yes', 95.00),
  (13, 'Cats', 'A beloved musical about a tribe of cats who gather for their annual Jellicle Ball', 'musical', '2023-04-17 14:00:00', '2023-04-17 16:30:00', 'Yes', 110.00),
  (14, 'Dracula', 'A thrilling horror show about the legendary vampire and his encounters with the living', 'horror', '2023-04-18 20:00:00', '2023-04-18 22:30:00', 'No', 80.00),
  (15, 'The Sound of Music', 'A timeless musical about a young woman who becomes a governess to a large family and falls in love', 'musical', '2023-04-19 19:30:00', '2023-04-19 22:00:00', 'Yes', 125.00),
  (16, 'A Midsummer Night''s Dream', 'One of Shakespeare''s most popular plays about the adventures of young lovers in a magical forest', 'comedy', '2023-04-20 18:00:00', '2023-04-20 20:30:00', 'Yes', 90.00),
  (17, 'Jekyll and Hyde', 'A dark and thrilling musical about a scientist who discovers a potion that unleashes his darker side', 'musical', '2023-04-21 19:00:00', '2023-04-21 22:00:00', 'No', 100.00),
  (18, 'The Great Gatsby', 'A dramatic adaptation of F. Scott Fitzgerald''s iconic novel about the excesses of the Jazz Age', 'drama', '2023-04-22 20:00:00', '2023-04-22 22:30:00', 'Yes', 85.00),
  (19, 'Little Shop of Horrors', 'A zany musical about a down-on-his-luck florist who discovers a plant with a taste for human blood', 'musical', '2023-04-23 14:00:00', '2023-04-23 16:30:00', 'Yes', 95.00),
  (20, 'A Streetcar Named Desire', 'A powerful drama about a southern belle who moves in with her sister and her brutish husband', 'drama', '2023-04-24 19:30:00', '2023-04-24 22:00:00', 'Yes', 90.00),
  (21, 'The Rocky Horror Show', 'A live stage production of the cult classic musical about a couple', 'musical', '2023-04-25 23:00:00', '2023-04-26 01:00:00', 'No', 70.00),
  (22, 'Carrie', 'A chilling horror show about a high school student with telekinetic powers', 'horror','2023-04-26 20:00:00', '2023-04-26 22:30:00', 'Yes', 80.00),
  (23, 'The Importance of Being Earnest', 'A witty and humorous comedy of manners about two young men who assume false identities', 'comedy', '2023-04-27 15:00:00', '2023-04-27 17:30:00', 'Yes', 95.00),
  (24, 'Les Misérables', 'A legendary musical about a former convict who seeks redemption in 19th century France', 'musical', '2023-04-28 19:30:00', '2023-04-28 22:30:00', 'Yes', 130.00),
  (25, 'The Glass Menagerie', 'A poignant drama about a family struggling to come to terms with their past and their present', 'drama', '2023-04-29 20:00:00', '2023-04-29 22:30:00', 'Yes', 85.00)
]

for data in show_data:
    show = xzz_show(
        show_name=data[1],
        show_description=data[2],
        show_type=xzz_show.ShowTypeChoices[data[3].upper()],
        start_time=data[4],
        end_time=data[5],
        show_accessible=xzz_show.ShowAccessibleChoices[data[6].upper()],
        show_price=data[7]
    )
    show.save()


store_data = [
  (1, 'Taco Bell', 'Food stall'),
  (2, 'Baskin Robbins', 'Ice cream parlor'),
  (3, 'Olive Garden', 'Restaurant'),
  (4, 'Hallmark', 'Gift Shop'),
  (5, 'Zara', 'Apparels'),
  (6, 'Subway', 'Food stall'),
  (7, 'Cold Stone Creamery', 'Ice cream parlor'),
  (8, 'Red Lobster', 'Restaurant'),
  (9, 'Barnes & Noble', 'Gift Shop'),
  (10, 'H&M', 'Apparels'),
  (11, 'McDonalds', 'Food stall'),
  (12, 'Dairy Queen', 'Ice cream parlor'),
  (13, 'Outback Steakhouse', 'Restaurant'),
  (14, 'Spencer Gifts', 'Gift Shop'),
  (15, 'Nike', 'Apparels'),
  (16, 'Pizza Hut', 'Food stall'),
  (17, 'Ben & Jerry''s', 'Ice cream parlor'),
  (18, 'Cheesecake Factory', 'Restaurant'),
  (19, 'Disney Store', 'Gift Shop'),
  (20, 'Forever 21', 'Apparels'),
  (21, 'KFC', 'Food stall'),
  (22, 'Haagen-Dazs', 'Ice cream parlor'),
  (23, 'Panera Bread', 'Restaurant'),
  (24, 'Yankee Candle', 'Gift Shop'),
  (25, 'Adidas', 'Apparels')
]

for data in store_data:
    store = xzz_store(
        store_name=data[1],
        category=data[2],
    )
    store.save()

order_data = [
  (1, '2023-04-01 12:00:00', 1),
  (2, '2023-04-01 14:30:00', 2),
  (3, '2023-04-01 16:45:00', 3),
  (4, '2023-04-02 10:00:00', 4),
  (5, '2023-04-02 13:15:00', 5),
  (6, '2023-04-02 15:30:00', 6),
  (7, '2023-04-03 11:00:00', 7),
  (8, '2023-04-03 14:30:00', 8),
  (9, '2023-04-03 16:00:00', 9),
  (10, '2023-04-04 12:30:00', 10),
  (11, '2023-04-04 15:45:00', 11),
  (12, '2023-04-04 18:00:00', 12),
  (13, '2023-04-05 11:00:00', 13),
  (14, '2023-04-05 13:45:00', 14),
  (15, '2023-04-05 16:00:00', 15),
  (16, '2023-04-06 12:30:00', 16),
  (17, '2023-04-06 15:15:00', 17),
  (18, '2023-04-06 17:30:00', 18),
  (19, '2023-04-07 11:00:00', 19),
  (20, '2023-04-07 14:15:00', 20),
  (21, '2023-04-07 16:30:00', 1),
  (22, '2023-04-08 12:00:00', 2),
  (23, '2023-04-08 15:15:00', 3),
  (24, '2023-04-08 17:30:00', 4),
  (25, '2023-04-09 11:00:00', 5)
]

for data in order_data:
    order = xzz_order(
        order_date=data[1],
        xzz_visitor=xzz_visitor.objects.get(id=data[2]),
    )
    order.save()



payment_data = [
  (1, 'Cash', 50.00, None, None, None, None, 1),
  (2, 'Cash', 75.00, None, None, None, None, 2),
  (3, 'Cash', 100.00, None, None, None, None, 3),
  (4, 'Credit', 125.00, 'John Doe', 1234567890123456, '2024-12-31 23:59:59', 123, 4),
  (5, 'Credit', 150.00, 'Jane Smith', 9876543210987654, '2025-06-30 23:59:59', 456, 5),
  (6, 'Debit', 175.00, 'Bob Johnson', 1111222233334444, '2023-03-31 23:59:59', 789, 6),
  (7, 'Cash', 80.00, None, None, None, None, 7),
  (8, 'Credit', 90.00, 'Alice Davis', 5555666677778888, '2025-09-30 23:59:59', 234, 8),
  (9, 'Debit', 110.00, 'Sarah Wilson', 4444333322221111, '2024-08-31 23:59:59', 567, 9),
  (10, 'Cash', 70.00, None, None, None, None, 10),
  (11, 'Credit', 120.00, 'Mark Thompson', 8888777766665555, '2023-11-30 23:59:59', 890, 11),
  (12, 'Debit', 95.00, 'Karen Brown', 7777666655554444, '2024-05-31 23:59:59', 123, 12),
  (13, 'Cash', 60.00, None, None, None, None, 13),
  (14, 'Credit', 130.00, 'David Lee', 2222333344445555, '2025-02-28 23:59:59', 456, 14),
  (15, 'Debit', 85.00, 'Michael Nguyen', 3333444455556666, '2023-10-31 23:59:59', 789, 15),
  (16, 'Cash', 55.00, None, None, None, None, 16),
  (17, 'Credit', 95.00, 'Mary Kim', 6666555577778888, '2023-06-30 23:59:59', 234, 17),
  (18, 'Debit', 120.00, 'Emily Chen', 7777888899990000, '2024-04-30 23:59:59', 567, 18),
  (19, 'Cash', 65.00, None, None, None, None, 19),
  (20, 'Credit', 110.00, 'Ryan Lee', 4444555566667777, '2024-12-31 23:59:59', 890, 20),
  (21, 'Debit', 75.00, 'Erica Chen', 9999888877776666, '2025-01-31 23:59:59', 123, 1),
  (22, 'Cash', 90.00, None, None, None, None, 2),
  (23, 'Credit', 105.00, 'Steven Chang', 1111222233334444, '2023-08-31 23:59:59', 456, 3),
  (24, 'Debit', 80.00, 'Linda Wang', 5555666677778888, '2024-06-30 23:59:59', 789, 4),
  (25, 'Cash', 100.00, None, None, None, None, 5)
]

for data in payment_data:
    payment = xzz_payment(
        payment_method=data[1],
        payment_amount=data[2],
        name_on_card=data[3],
        card_number=data[4],
        expiration_date=data[5],
        cvv=data[6],
        order=xzz_order.objects.get(order_id=data[7]),
    )
    payment.save()


ticket_data = [
  (1, 'Online', '2023-04-01 12:00:00', 50.00, 1, 1),
  (2, 'Onsite', '2023-04-01 14:30:00', 50.00, 2, 2),
  (3, 'Online', '2023-04-01 16:45:00', 50.00, 3, 3),
  (4, 'Onsite', '2023-04-02 10:00:00', 50.00, 4, 4),
  (5, 'Online', '2023-04-02 13:15:00', 50.00, 5, 5),
  (6, 'Onsite', '2023-04-02 15:30:00', 50.00, 6, 6),
  (7, 'Online', '2023-04-03 11:00:00', 50.00, 7, 7),
  (8, 'Onsite', '2023-04-03 14:30:00', 50.00, 8, 8),
  (9, 'Online', '2023-04-03 16:00:00', 50.00, 9, 9),
  (10, 'Onsite', '2023-04-04 12:30:00', 50.00, 10, 10),
  (11, 'Online', '2023-04-04 15:45:00', 50.00, 11, 11),
  (12, 'Onsite', '2023-04-04 18:00:00', 50.00, 12, 12),
  (13, 'Online', '2023-04-05 11:00:00', 50.00, 13, 13),
  (14, 'Onsite', '2023-04-05 13:45:00', 50.00, 14, 14),
  (15, 'Online', '2023-04-05 16:00:00', 50.00, 15, 15),
  (16, 'Onsite', '2023-04-06 12:30:00', 50.00, 16, 16),
  (17, 'Online', '2023-04-06 15:15:00', 50.00, 17, 17),
  (18, 'Onsite', '2023-04-06 17:30:00', 50.00, 18, 18),
  (19, 'Online', '2023-04-07 11:00:00', 50.00, 19, 19),
  (20, 'Onsite', '2023-04-07 14:15:00', 50.00, 20, 20),
  (21, 'Online', '2023-04-07 16:30:00', 50.00, 21, 1),
  (22, 'Onsite', '2023-04-08 12:00:00', 50.00, 22, 2),
  (23, 'Online', '2023-04-08 15:15:00', 50.00, 23, 3),
  (24, 'Onsite', '2023-04-08 17:30:00', 50.00, 24, 4),
  (25, 'Online', '2023-04-09 11:00:00', 50.00, 25, 5)
]

for data in ticket_data:
    ticket = xzz_ticket(
        ticket_method=data[1],
        visit_date=data[2],
        ticket_price=data[3],
        order=xzz_order.objects.get(order_id=data[4]),
        visitor=xzz_visitor.objects.get(id=data[5]),
    )
    ticket.save()

parking_data = [
  (1, 'Lot A', 1, '2023-04-01 10:00:00', '2023-04-01 15:30:00', 10.00, 6),
  (2, 'Lot B', 2, '2023-04-01 11:30:00', '2023-04-01 16:45:00', 12.50, 16),
  (3, 'Lot C', 3, '2023-04-01 12:15:00', '2023-04-01 17:15:00', 13.50, 11),
  (4, 'Lot D', 4, '2023-04-02 09:30:00', '2023-04-02 14:45:00', 9.00, 19),
  (5, 'Lot A', 5, '2023-04-02 10:45:00', '2023-04-02 15:30:00', 11.50, 5),
  (6, 'Lot B', 6, '2023-04-02 12:00:00', '2023-04-02 17:00:00', 13.00, 23),
  (7, 'Lot C', 7, '2023-04-03 10:00:00', '2023-04-03 15:15:00', 10.50, 13),
  (8, 'Lot D', 8, '2023-04-03 11:15:00', '2023-04-03 16:30:00', 12.00, 21),
  (9, 'Lot A', 9, '2023-04-03 12:30:00', '2023-04-03 17:45:00', 14.00, 10),
  (10, 'Lot B', 10, '2023-04-04 09:00:00', '2023-04-04 14:30:00', 9.50, 24),
  (11, 'Lot C', 11, '2023-04-04 10:15:00', '2023-04-04 15:00:00', 11.00, 15),
  (12, 'Lot D', 12, '2023-04-04 11:30:00', '2023-04-04 16:45:00', 12.50, 3),
  (13, 'Lot A', 13, '2023-04-05 10:00:00', '2023-04-05 15:00:00', 10.00, 9),
  (14, 'Lot B', 14, '2023-04-05 11:30:00', '2023-04-05 16:15:00', 11.50, 18),
  (15, 'Lot C', 15, '2023-04-05 12:45:00', '2023-04-05 17:30:00', 13.00, 1),
  (16, 'Lot D', 16, '2023-04-06 09:30:00', '2023-04-06 14:45:00', 9.00, 8),
  (17, 'Lot A', 17, '2023-04-06 10:45:00', '2023-04-06 15:30:00', 11.50, 4),
  (18, 'Lot B', 18, '2023-04-06 12:00:00', '2023-04-06 17:00:00', 13.00, 22),
  (19, 'Lot C', 19, '2023-04-07 10:00:00', '2023-04-07 15:15:00', 10.50, 12),
  (20, 'Lot D', 20, '2023-04-07 11:15:00', '2023-04-07 16:30:00', 12.00, 25),
  (21, 'Lot A', 21, '2023-04-07 12:30:00', '2023-04-07 17:45:00', 14.00, 17),
  (22, 'Lot B', 22, '2023-04-08 09:00:00', '2023-04-08 14:30:00', 9.50, 20),
  (23, 'Lot C', 23, '2023-04-08 10:15:00', '2023-04-08 15:00:00', 11.00, 2),
  (24, 'Lot D', 24, '2023-04-08 11:30:00', '2023-04-08 16:45:00', 12.50, 14),
  (25, 'Lot A', 25, '2023-04-09 10:00:00', '2023-04-09 15:00:00', 10.00, 7)
]

for data in parking_data:
    parking = xzz_parking(
        lot=data[1],
        spot=data[2],
        time_in=data[3],
        time_out=data[4],
        fee=data[5],
        order=xzz_order.objects.get(order_id=data[6]),
    )
    parking.save()

Attraction_Visit = [
  (1, '2023-04-01 10:00:00', 3, 6),
  (2, '2023-04-01 11:30:00', 16, 17),
  (3, '2023-04-01 12:15:00', 11, 7),
  (4, '2023-04-02 09:30:00', 19, 16),
  (5, '2023-04-02 10:45:00', 5, 2),
  (6, '2023-04-02 12:00:00', 23, 14),
  (7, '2023-04-03 10:00:00', 13, 22),
  (8, '2023-04-03 11:15:00', 21, 3),
  (9, '2023-04-03 12:30:00', 10, 5),
  (10, '2023-04-04 09:00:00', 24, 15),
  (11, '2023-04-04 10:15:00', 15, 4),
  (12, '2023-04-04 11:30:00', 3, 21),
  (13, '2023-04-05 10:00:00', 9, 9),
  (14, '2023-04-05 11:30:00', 18, 20),
  (15, '2023-04-05 12:45:00', 1, 19),
  (16, '2023-04-06 09:30:00', 8, 3),
  (17, '2023-04-06 10:45:00', 4, 7),
  (18, '2023-04-06 12:00:00', 22, 13),
  (19, '2023-04-07 10:00:00', 12, 10),
  (20, '2023-04-07 11:15:00', 25, 22),
  (21, '2023-04-07 12:30:00', 17, 12),
  (22, '2023-04-08 09:00:00', 20, 14),
  (23, '2023-04-08 10:15:00', 2, 1),
  (24, '2023-04-08 11:30:00', 14, 4),
  (25, '2023-04-09 10:00:00', 7, 5),
  (26, '2023-04-01 14:00:00', 1, 22),
  (27, '2023-04-02 16:00:00', 2, 20),
  (28, '2023-04-03 13:00:00', 3, 17),
  (29, '2023-04-04 15:00:00', 4, 12),
  (30, '2023-04-05 11:00:00', 5, 11),
  (31, '2023-04-06 13:30:00', 6, 19),
  (32, '2023-04-07 16:00:00', 7, 23),
  (33, '2023-04-08 14:00:00', 8, 8),
  (34, '2023-04-09 12:00:00', 9, 2),
  (35, '2023-04-01 15:30:00', 10, 16)
]

for data in Attraction_Visit:
    attr_visi = xzz_attr_visi(
        r_in_time=data[1],
        visitor=xzz_visitor.objects.get(id=data[2]),
        attraction=xzz_attraction.objects.get(id=data[3]),
    )
    attr_visi.save()


show_order = [
  (1, 12, 9),
  (2, 18, 23),
  (3, 10, 1),
  (4, 20, 16),
  (5, 15, 12),
  (6, 6, 11),
  (7, 8, 13),
  (8, 2, 8),
  (9, 24, 14),
  (10, 23, 2),
  (11, 14, 3),
  (12, 25, 6),
  (13, 21, 19),
  (14, 9, 20),
  (15, 4, 4),
  (16, 7, 5),
  (17, 11, 21),
  (18, 16, 18),
  (19, 17, 7),
  (20, 1, 10),
  (21, 19, 25),
  (22, 22, 15),
  (23, 13, 24),
  (24, 5, 22),
  (25, 3, 17),
  (26, 16, 24),
  (27, 9, 2),
  (28, 20, 11),
  (29, 23, 8),
  (30, 11, 16),
  (31, 8, 14),
  (32, 19, 1),
  (33, 2, 10),
  (34, 6, 25),
  (35, 1, 13)
]

for data in show_order:
    orde_show = xzz_orde_show(
        show=xzz_show.objects.get(id=data[1]),
        order=xzz_order.objects.get(order_id=data[2]),
    )
    orde_show.save()

store_order_data = [
(1, 'Cheeseburger', 'Juicy beef patty topped with melted cheese and served on a toasted bun with lettuce and tomato', 9.99, 3, 14),
(2, 'Chicken Caesar Salad', 'Grilled chicken breast, crisp romaine lettuce', 8.49, 16, 20),
(3, 'Margherita Pizza', 'Traditional pizza topped with tomato sauce, mozzarella cheese, and fresh basil leaves', 12.99, 11, 22),
(4, 'French Fries', 'Crispy golden fries served with ketchup or your choice of dipping sauce', 4.99, 5, 19),
(5, 'Fish and Chips', 'Beer-battered fish and crispy fries, served with tartar sauce and lemon wedges', 11.99, 9, 23),
(6, 'Spaghetti Bolognese', 'Hearty meat sauce served over a bed of al dente spaghetti noodles', 10.99, 12, 2),
(7, 'BBQ Chicken Wings', 'Crispy chicken wings glazed with sweet and tangy BBQ sauce', 7.99, 18, 3),
(8, 'Vegetable Stir-Fry', 'Assorted fresh vegetables stir-fried with your choice of protein in a savory sauce', 9.49, 22, 15),
(9, 'Beef Tacos', 'Three soft-shell tacos filled with seasoned ground beef, lettuce, cheese, and salsa', 10.99, 4, 9),
(10, 'Roasted Chicken', 'Tender roasted chicken served with your choice of side dish and gravy', 13.99, 17, 18),
(11, 'Chocolate Brownie', 'Warm and gooey chocolate brownie served with vanilla ice cream', 6.99, 6, 10),
(12, 'Caesar Salad', 'Crisp romaine lettuce, garlic croutons, and Parmesan cheese tossed with creamy Caesar dressing', 7.99, 19, 21),
(13, 'Pesto Pasta', 'Penne pasta tossed with homemade basil pesto sauce and Parmesan cheese', 11.49, 2, 25),
(14, 'Cheese Pizza', 'Traditional pizza topped with tomato sauce and mozzarella cheese', 10.99, 8, 6),
(15, 'Mushroom Risotto', 'Creamy risotto with sautéed mushrooms and Parmesan cheese', 12.99, 24, 1),
(16, 'Hamburger', 'Juicy beef patty served on a toasted bun with lettuce and tomato', 8.99, 7, 12),
(17, 'Caesar Grilled Shrimp', 'Grilled shrimp, crisp romaine lettuce', 12.49, 21, 17),
(18, 'Onion Rings', 'Crispy fried onion rings served with your choice of dipping sauce', 5.99, 14, 4),
(19, 'Fish Tacos', 'Three soft-shell tacos filled with grilled fish, lettuce, cheese, and salsa', 12.99, 20, 24),
(20, 'Lemon Chicken','Grilled chicken breast topped with lemon butter sauce and served with your choice of side dish', 11.99, 15, 16),
(21, 'Pesto Chicken Pizza', 'Traditional pizza topped with basil pesto sauce, mozzarella cheese, and grilled chicken', 13.49, 10, 8),
(22, 'Beef Stir-Fry', 'Tender strips of beef stir-fried with fresh vegetables in a savory sauce', 12.99, 13, 7),
(23, 'Chicken Parmesan', 'Breaded chicken breast topped with marinara sauce and melted mozzarella cheese', 14.99, 1, 11),
(24, 'Greek Salad', 'Crisp lettuce, juicy tomatoes, cucumbers, red onion, Kalamata olives', 9.99, 23, 13),
(25, 'Spicy Buffalo Wings', 'Crispy chicken wings coated in spicy buffalo sauce', 8.99, 25, 5),
(26, 'Grilled Salmon', 'Fresh salmon fillet grilled to perfection and served with your choice of side dish', 15.99, 9, 24),
(27, 'Vegetable Pizza', 'Traditional pizza topped with tomato sauce, mozzarella cheese, and assorted fresh vegetables', 12.99, 2, 14),
(28, 'Shrimp Scampi', 'Sauteed shrimp tossed with garlic, butter, lemon juice, and white wine', 16.49, 18, 6),
(29, 'Crispy Chicken Sandwich', 'Crispy fried chicken breast served on a toasted bun with lettuce, tomato, and mayo', 9.99, 5, 20),
(30, 'Caprese Salad', 'Fresh mozzarella cheese, ripe tomatoes, and fresh basil leaves drizzled with balsamic glaze', 8.99, 7, 19),
(31, 'Beef and Broccoli Stir-Fry', 'Tender strips of beef and fresh broccoli florets stir-fried in a savory sauce', 11.99, 12, 3),
(32, 'Fettuccine Alfredo', 'Creamy Alfredo sauce tossed with fettuccine noodles and Parmesan cheese', 10.99, 16, 15),
(33, 'Chicken Fajitas', 'Sizzling hot chicken fajitas served with warm tortillas, guacamole, sour cream, and salsa', 13.99, 21, 2),
(34, 'Caesar Grilled Chicken', 'Grilled chicken breast, crisp romaine lettuce', 10.49, 24, 18),
(35, 'Margarita', 'Classic tequila-based cocktail made with lime juice and triple sec, served with salt on the rim', 7.99, 3, 9)
]

for data in store_order_data:
    store_order = xzz_orde_stor(
        menu_item_name=data[1],
        menu_item_description=data[2],
        menu_item_unit_price=data[3],
        store=xzz_store.objects.get(id=data[4]),
        order=xzz_order.objects.get(order_id=data[5]),
    )
    store_order.save()