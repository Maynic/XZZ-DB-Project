DROP TABLE IF EXISTS xzz_attr_visi;
DROP TABLE IF EXISTS xzz_attraction;
DROP TABLE IF EXISTS xzz_orde_show;
DROP TABLE IF EXISTS xzz_orde_stor;
DROP TABLE IF EXISTS xzz_parking;
DROP TABLE IF EXISTS xzz_payment;
DROP TABLE IF EXISTS xzz_show;
DROP TABLE IF EXISTS xzz_store;
DROP TABLE IF EXISTS xzz_ticket;
DROP TABLE IF EXISTS xzz_order;
DROP TABLE IF EXISTS xzz_visitor;
DROP PROCEDURE IF EXISTS populate_summary_table;
DROP TABLE IF EXISTS summary;


CREATE TABLE xzz_attr_visi (
    r_id          DOUBLE NOT NULL,
    r_in_time     DATETIME NOT NULL,
    visitor_id    DOUBLE NOT NULL,
    attraction_id DOUBLE NOT NULL
)
;

ALTER TABLE xzz_attr_visi ADD CONSTRAINT xzz_attr_visi_pk PRIMARY KEY ( r_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_attraction (
    attraction_id          DOUBLE NOT NULL,
    attraction_name        VARCHAR(60) NOT NULL,
    attraction_description VARCHAR(100) NOT NULL,
    attraction_type        VARCHAR(20) NOT NULL,
    attraction_status      VARCHAR(20) NOT NULL,
    capacity               DOUBLE NOT NULL,
    min_height             DOUBLE NOT NULL COMMENT 'Assume in cm',
    duration               DOUBLE NOT NULL COMMENT 'In Minutes',
    location               VARCHAR(10) NOT NULL
)
;

/* Moved to CREATE TABLE
COMMENT ON COLUMN xzz_attraction.min_height IS
    'Assume in cm'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN xzz_attraction.duration IS
    'In Minutes'; */

ALTER TABLE xzz_attraction ADD CONSTRAINT xzz_attraction_pk PRIMARY KEY ( attraction_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_orde_show (
    os_id    DOUBLE NOT NULL,
    show_id  DOUBLE NOT NULL,
    order_id DOUBLE NOT NULL
)
;

ALTER TABLE xzz_orde_show ADD CONSTRAINT xzz_orde_show_pk PRIMARY KEY ( os_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_orde_stor (
    menu_item_id          DOUBLE NOT NULL,
    menu_item_name        VARCHAR(30) NOT NULL,
    menu_item_description VARCHAR(100) NOT NULL,
    menu_item_unit_price  DOUBLE NOT NULL,
    store_id              DOUBLE NOT NULL,
    order_id              DOUBLE NOT NULL
)
;

ALTER TABLE xzz_orde_stor ADD CONSTRAINT xzz_orde_stor_pk PRIMARY KEY ( menu_item_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_order (
    order_id   DOUBLE NOT NULL,
    order_date DATETIME NOT NULL,
    visitor_id DOUBLE NOT NULL
)
;

ALTER TABLE xzz_order ADD CONSTRAINT xzz_order_pk PRIMARY KEY ( order_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_parking (
    parking_id DOUBLE NOT NULL,
    lot        VARCHAR(10) NOT NULL,
    spot       DOUBLE NOT NULL,
    time_in    DATETIME NOT NULL,
    time_out   DATETIME,
    fee        DOUBLE NOT NULL,
    order_id   DOUBLE NOT NULL
)
;

ALTER TABLE xzz_parking ADD CONSTRAINT xzz_parking_pk PRIMARY KEY ( parking_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_payment (
    payment_id      DOUBLE NOT NULL,
    payment_method  VARCHAR(15) NOT NULL,
    payment_amount  DOUBLE NOT NULL,
    name_on_card    VARCHAR(30),
    card_number     DOUBLE,
    expiration_date DATETIME,
    cvv             DOUBLE,
    order_id        DOUBLE NOT NULL
)
;

ALTER TABLE xzz_payment ADD CONSTRAINT xzz_payment_pk PRIMARY KEY ( payment_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_show (
    show_id          DOUBLE NOT NULL,
    show_name        VARCHAR(50) NOT NULL,
    show_description VARCHAR(100) NOT NULL,
    show_type        VARCHAR(15) NOT NULL,
    start_time       DATETIME NOT NULL,
    end_time         DATETIME NOT NULL,
    show_accessible  VARCHAR(3) NOT NULL COMMENT 'Wheelchair',
    show_price       DOUBLE NOT NULL
)
;

/* Moved to CREATE TABLE
COMMENT ON COLUMN xzz_show.show_accessible IS
    'Wheelchair'; */

ALTER TABLE xzz_show ADD CONSTRAINT xzz_show_pk PRIMARY KEY ( show_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_store (
    store_id   DOUBLE NOT NULL,
    store_name VARCHAR(255) NOT NULL,
    category   VARCHAR(20) NOT NULL
)
;

ALTER TABLE xzz_store ADD CONSTRAINT xzz_store_pk PRIMARY KEY ( store_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_ticket (
    ticket_id     DOUBLE NOT NULL,
    ticket_method VARCHAR(6) NOT NULL,
    visit_date    DATETIME NOT NULL,
    ticket_price  DOUBLE NOT NULL,
    order_id      DOUBLE NOT NULL,
    visitor_id    DOUBLE NOT NULL
)
;

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE INDEX xzz_ticket__idx ON
    xzz_ticket (
        visitor_id
    ASC )
       ;

ALTER TABLE xzz_ticket ADD CONSTRAINT xzz_ticket_pk PRIMARY KEY ( ticket_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE xzz_visitor (
    visitor_id   DOUBLE NOT NULL,
    visitor_name VARCHAR(60) NOT NULL,
    birth_date   DATETIME NOT NULL,
    visitor_type VARCHAR(10) NOT NULL,
    address      VARCHAR(60),
    city         VARCHAR(20),
    state        VARCHAR(20),
    zip          DOUBLE,
    email        VARCHAR(60),
    phone        DOUBLE
)
;

ALTER TABLE xzz_visitor ADD CONSTRAINT xzz_visitor_pk PRIMARY KEY ( visitor_id );

ALTER TABLE xzz_attr_visi
    ADD CONSTRAINT xzz_attr_visi_xzz_attraction_fk FOREIGN KEY ( attraction_id )
        REFERENCES xzz_attraction ( attraction_id )
    ;

ALTER TABLE xzz_attr_visi
    ADD CONSTRAINT xzz_attr_visi_xzz_visitor_fk FOREIGN KEY ( visitor_id )
        REFERENCES xzz_visitor ( visitor_id )
    ;

ALTER TABLE xzz_orde_show
    ADD CONSTRAINT xzz_orde_show_xzz_order_fk FOREIGN KEY ( order_id )
        REFERENCES xzz_order ( order_id )
    ;

ALTER TABLE xzz_orde_show
    ADD CONSTRAINT xzz_orde_show_xzz_show_fk FOREIGN KEY ( show_id )
        REFERENCES xzz_show ( show_id )
    ;

ALTER TABLE xzz_orde_stor
    ADD CONSTRAINT xzz_orde_stor_xzz_order_fk FOREIGN KEY ( order_id )
        REFERENCES xzz_order ( order_id )
    ;

ALTER TABLE xzz_orde_stor
    ADD CONSTRAINT xzz_orde_stor_xzz_store_fk FOREIGN KEY ( store_id )
        REFERENCES xzz_store ( store_id )
    ;

ALTER TABLE xzz_order
    ADD CONSTRAINT xzz_order_xzz_visitor_fk FOREIGN KEY ( visitor_id )
        REFERENCES xzz_visitor ( visitor_id )
    ;

ALTER TABLE xzz_parking
    ADD CONSTRAINT xzz_parking_xzz_order_fk FOREIGN KEY ( order_id )
        REFERENCES xzz_order ( order_id )
    ;

ALTER TABLE xzz_payment
    ADD CONSTRAINT xzz_payment_xzz_order_fk FOREIGN KEY ( order_id )
        REFERENCES xzz_order ( order_id )
    ;

ALTER TABLE xzz_ticket
    ADD CONSTRAINT xzz_ticket_xzz_order_fk FOREIGN KEY ( order_id )
        REFERENCES xzz_order ( order_id )
    ;

ALTER TABLE xzz_ticket
    ADD CONSTRAINT xzz_ticket_xzz_visitor_fk FOREIGN KEY ( visitor_id )
        REFERENCES xzz_visitor ( visitor_id )
    ;

/* Visitor */
CONSTRAINT chk_visitor_type CHECK (visitor_type IN ('Individual', 'Group', 'Member', 'Student'))

/* Attraction */
CONSTRAINT chk_attraction_type CHECK (attraction_type IN ('roller coaster', 'water ride', 'dark ride', 'kid ride')),
CONSTRAINT chk_attraction_status CHECK (attraction_status IN ('open', 'closed', 'under maintenance')),
CONSTRAINT chk_location CHECK (location REGEXP '^Lot [A-Z]$')

/* Show */
CONSTRAINT chk_show_accessible CHECK (show_accessible IN ('Yes', 'No'))
CONSTRAINT chk_show_type CHECK (show_type IN ('drama', 'musical', 'comedy', 'horror', 'adventure'))

/* Store */
CONSTRAINT chk_category CHECK (category IN ('Food stall', 'Ice cream parlor', 'Restaurant', 'Gift Shop', 'Apparels'))

/* Payment */
CONSTRAINT chk_payment_method CHECK (payment_method IN ('Cash', 'Credit', 'Debit'))
CONSTRAINT chk_payment CHECK (
    (payment_method = 'Cash' AND name_on_card IS NULL AND card_number IS NULL AND expiration_date IS NULL AND CVV IS NULL) 
    OR (payment_method IN ('Credit', 'Debit') AND name_on_card IS NOT NULL AND card_number IS NOT NULL AND expiration_date IS NOT NULL AND CVV IS NOT NULL)
)

/* Ticket */
CONSTRAINT chk_ticket_method CHECK (ticket_method IN ('Online', 'Onsite'))


-- trigger for update ticket price based on online or onsite 
DELIMITER //
CREATE TRIGGER apply_discount_Online
BEFORE INSERT
ON xzz_ticket
FOR EACH ROW
BEGIN
	IF NEW.ticket_method = 'Online' THEN
        SET NEW.ticket_price = NEW.ticket_price * 0.95;
	END IF;
END//


-- trigger for update ticket price based on child or senior type
-- compute by DOB - current date
 CREATE TRIGGER apply_child_senior
 BEFORE INSERT
 ON xzz_ticket
 FOR EACH ROW
 BEGIN
	DECLARE age INT;
    SELECT FLOOR(DATEDIFF(NOW(), xzz_visitor.birth_date) / 365) INTO age
    FROM xzz_visitor
    WHERE xzz_visitor.visitor_id = NEW.visitor_id;
    
    IF age > 60 OR age < 7 THEN
 		SET NEW.ticket_price = NEW.ticket_price * 0.85;
 	END IF;
 END;
 
 -- trigger for update ticket price based on member
CREATE TRIGGER apply_member_disc
BEFORE INSERT ON xzz_ticket
FOR EACH ROW
BEGIN
    DECLARE visitortype VARCHAR(20);
    DECLARE is_weekend BOOLEAN;
    DECLARE num_visitors INT;
    SELECT xzz_visitor.visitor_type INTO visitortype 
    FROM xzz_visitor
    WHERE xzz_visitor.visitor_id = NEW.visitor_id;
    
    SET is_weekend = DAYOFWEEK(NEW.visit_date) IN (1, 7);
    
    IF visitortype = 'Member' AND NOT is_weekend THEN 
        SELECT COUNT(*) INTO num_visitors
        FROM xzz_ticket t
        JOIN xzz_visitor v ON v.visitor_id = t.visitor_id
        WHERE v.visitor_type = 'Member'
        AND NOT DAYOFWEEK(t.visit_date) IN (1, 7)
        AND t.visit_date = NEW.visit_date;
        
        IF num_visitors < 5 THEN
            SET NEW.ticket_price = NEW.ticket_price * 0.9;
        ELSE
            SET NEW.ticket_price = CASE 
                WHEN NEW.ticket_id IN (
                    SELECT id FROM (
                        SELECT id FROM xzz_ticket t
                        JOIN xzz_visitor v ON v.visitor_id = t.visitor_id
                        WHERE v.visitor_type = 'Member'
                        AND NOT DAYOFWEEK(t.visit_date) IN (1, 7)
                        AND t.visit_date = NEW.visit_date
                        ORDER BY t.ticket_price
                        LIMIT 5
                    ) AS t5
                ) THEN NEW.ticket_price * 0.9
                ELSE NEW.ticket_price
            END;
        END IF;
    END IF;
END;






/* Visitor */
INSERT INTO xzz_visitor (visitor_id, visitor_name, birth_date, visitor_type, address, city, state, zip, email, phone)
VALUES
  (1, 'John Smith', '1975-06-30', 'Individual', '123 Main St', 'Anytown', 'CA', 12345, 'john.smith@example.com', 5551234567),
  (2, 'Jane Doe', '1900-01-15', 'Individual', '456 Elm St', 'Anycity', 'NY', 67890, 'jane.doe@example.com', 5552345678),
  (3, 'David Johnson', '1957-08-10', 'Individual', '789 Oak St', 'Anystate', 'TX', 34567, 'david.johnson@example.com', 5553456789),
  (4, 'Emma Thompson', '2001-05-20', 'Student', '321 Maple Ave', 'Anothercity', 'FL', 23456, 'emma.thompson@example.com', 5554567890),
  (5, 'Oliver Davis', '2015-12-01', 'Member', '654 Cedar St', 'Somecity', 'IL', 45678, 'oliver.davis@example.com', 5555678901),
  (6, 'Sophie Wilson', '1982-02-14', 'Individual', '987 Pine St', 'Anotherstate', 'MI', 56789, 'sophie.wilson@example.com', 5556789012),
  (7, 'Liam Baker', '2008-10-05', 'Student', '246 Oak Ave', 'Anothercity', 'MA', 67890, 'liam.baker@example.com', 5557890123),
  (8, 'Ava Mitchell', '2010-03-27', 'Student', '369 Elm St', 'Somestate', 'PA', 78901, 'ava.mitchell@example.com', 5558901234),
  (9, 'Noah Brown', '2016-07-15', 'Child', '753 Maple St', 'Somewhere', 'OH', 89012, 'noah.brown@example.com', 5559012345),
  (10, 'Isabella Davis', '2005-11-28', 'Member', '852 Pine Ave', 'Anycity', 'VA', 90123, 'isabella.davis@example.com', 5550123456),
  (11, 'William Taylor', '1940-03-01', 'Individual', '963 Oak St', 'Somewhere', 'OR', 23456, 'william.taylor@example.com', 5551234567),
  (12, 'Sophia Wilson', '1998-09-17', 'Student', '741 Maple Ave', 'Anycity', 'WA', 34567, 'sophia.wilson@example.com', 5552345678),
  (13, 'Logan Thomas', '2012-06-22', 'Child', '852 Cedar St', 'Anothercity', 'NJ', 45678, 'logan.thomas@example.com', 5553456789),
  (14, 'Mia Lee', '2018-01-10', 'Child', '159 Oak Ave', 'Somestate', 'MD', 56789, 'mia.lee@example.com', 5554567890),
  (15, 'Ethan Brown', '2006-04-15', 'Student', '753 Pine St', 'Somewhere', 'TX', 67890, 'ethan.brown@example.com', 5555678901),
  (16, 'Madison Garcia', '1955-11-30', 'Individual', '369 Maple St', 'Anystate', 'GA', 78901, 'madison.garcia@example.com', 5556789012),
  (17, 'Jacob Hernandez', '2011-08-18', 'Child', '963 Elm Ave', 'Somewhere', 'CA', 89012, 'jacob.hernandez@example.com', 5557890123),
  (18, 'Abigail Martinez', '2014-01-02', 'Child', '852 Pine St', 'Anothercity', 'NY', 90123, 'abigail.martinez@example.com', 5558901234),
  (19, 'Michael Rodriguez', '1952-12-24', 'Individual', '753 Cedar St', 'Anycity', 'MA', 12345, 'michael.rodriguez@example.com', 5559012345),
  (20, 'Emily Young', '2000-05-10', 'Student', '369 Oak Ave', 'Somestate', 'PA', 23456, 'emily.young@example.com', 5550123456),
  (21, 'Daniel Scott', '2013-02-14', 'Child', '852 Pine Ave', 'Anothercity', 'VA', 34567, 'daniel.scott@example.com', 5551234567),
  (22, 'Madison Perez', '2019-09-17', 'Child', '159 Cedar St', 'Somewhere', 'OH', 45678, 'madison.perez@example.com', 5552345678),
  (23, 'Aiden Roberts', '2010-06-22', 'Student', '753 Oak St', 'Anycity', 'WA', 56789, 'aiden.roberts@example.com', 5553456789),
  (24, 'Samantha Turner', '1945-01-10', 'Individual', '369 Maple Ave', 'Somestate', 'NJ', 67890, 'samantha.turner@example.com', 5554567890),
  (25, 'Alexander Phillips', '1960-04-15', 'Individual', '963 Pine St', 'Anycity', 'MD', 78901, 'alexander.phillips@example.com', 5555678901);


/* Attraction */
INSERT INTO xzz_attraction (attraction_id, attraction_name, attraction_description, attraction_type, attraction_status, capacity, min_height, duration, location)
VALUES
  (1, 'The Beast', 'The longest wooden roller coaster in the world', 'roller coaster', 'open', 36, 137, 4, 'Lot A'),
  (2, 'Jurassic Park River Adventure', 'A thrilling water ride through a prehistoric jungle', 'water ride', 'open', 20, 107, 5, 'Lot A'),
  (3, 'Haunted Mansion', 'A spooky dark ride through a haunted house', 'dark ride', 'closed', 16, 91, 3, 'Lot B'),
  (4, 'Dumbo the Flying Elephant', 'A gentle kid ride that lets guests soar through the air on a magical elephant', 'kid ride', 'open', 32, 76, 2, 'Lot B'),
  (5, 'Millennium Force', 'One of the tallest and fastest roller coasters in the world', 'roller coaster', 'under maintenance', 24, 142, 3, 'Lot C'),
  (6, 'Pirates of the Caribbean', 'A classic dark ride that takes guests on a journey through a pirate-infested Caribbean', 'dark ride', 'open', 12, 107, 4, 'Lot C'),
  (7, 'Splash Mountain', 'A thrilling water ride that culminates in a huge drop into a briar patch', 'water ride', 'open', 18, 102, 6, 'Lot D'),
  (8, 'Sesame Street Safari of Fun', 'A colorful kid ride featuring all of your favorite Sesame Street characters', 'kid ride', 'open', 30, 61, 2, 'Lot D'),
  (9, 'Kingda Ka', 'The tallest and fastest roller coaster in the world', 'roller coaster', 'closed', 20, 139, 2, 'Lot E'),
  (10, 'It''s a Small World', 'A charming dark ride that takes guests on a musical journey around the world', 'dark ride', 'open', 24, 91, 8, 'Lot E'),
  (11, 'The Hulk', 'A thrilling roller coaster that takes guests through a series of twists, turns, and inversions', 'roller coaster', 'open', 30, 137, 3, 'Lot F'),
  (12, 'Kali River Rapids', 'A wet and wild water ride through the heart of the jungle', 'water ride', 'under maintenance', 16, 107, 4, 'Lot F'),
  (13, 'Toy Story Midway Mania!', 'A fun-filled ride that lets guests compete in carnival', 'kid ride', 'open', 24, 91, 5, 'Lot G'),
  (14, 'Expedition Everest', 'A thrilling roller coaster that takes guests on a journey through the Himalayas', 'roller coaster', 'open', 20, 122, 4, 'Lot G'),
  (15, 'Harry Potter and the Forbidden Journey', 'A magical dark ride that takes guests on a journey through the world of Harry Potter', 'dark ride', 'closed', 12, 122, 5, 'Lot H'),
  (16, 'The Cat in the Hat', 'A whimsical kid ride that lets guests join the Cat in the Hat', 'kid ride', 'open', 32, 76, 2, 'Lot H'),
  (17, 'The Incredible Hulk Coaster', 'A thrilling roller coaster that takes guests through a series of high-speed inversions and twists', 'roller coaster', 'under maintenance', 30, 137, 3, 'Lot I'),
  (18, 'Journey to Atlantis', 'A water ride that takes guests on a journey through', 'water ride', 'open', 18, 107, 5, 'Lot I'),
  (19, 'Peter Pan''s Flight', 'A classic dark ride that takes guests on a journey through the world of Peter Pan', 'dark ride', 'open', 12, 91, 3, 'Lot J'),
  (20, 'Flying Fish', 'A gentle kid ride that lets guests soar through the air on colorful fish', 'kid ride', 'open', 24, 76, 2, 'Lot J'),
  (21, 'Top Thrill Dragster', 'A record-breaking roller coaster that launches riders from 0 to 120 mph in just a few seconds', 'roller coaster', 'open', 20, 137, 1, 'Lot K'),
  (22, 'Raging Rapids', 'A wild water ride that takes guests through turbulent rapids and cascading waterfalls', 'water ride', 'closed', 16, 107, 4, 'Lot K'),
  (23, 'Transformers: The Ride 3D', 'A thrilling dark ride that puts guests in the middle of', 'dark ride', 'open', 12, 107, 4, 'Lot L'),
  (24, 'The Magic Carpets of Aladdin', 'A fun kid ride that lets guests fly through the air on magical carpets', 'kid ride', 'open', 32, 76, 2, 'Lot L'),
  (25, 'Steel Vengeance', 'A record-breaking roller coaster that features a wooden and steel hybrid track', 'roller coaster', 'open', 24, 137, 2, 'Lot M');


/* Show */
INSERT INTO xzz_show (show_id, show_name, show_description, show_type, start_time, end_time, show_accessible, show_price)
VALUES
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
  (25, 'The Glass Menagerie', 'A poignant drama about a family struggling to come to terms with their past and their present', 'drama', '2023-04-29 20:00:00', '2023-04-29 22:30:00', 'Yes', 85.00);


/* Store */
INSERT INTO xzz_store (store_id, store_name, category)
VALUES
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
  (25, 'Adidas', 'Apparels');



/* Order */
INSERT INTO xzz_order (order_id, order_date, visitor_id)
VALUES
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
  (25, '2023-04-09 11:00:00', 5);


/* Payment */
/* Amount needs to be refined */
INSERT INTO xzz_payment (payment_id, payment_method, payment_amount, name_on_card, card_number, expiration_date, cvv, order_id)
VALUES
  (1, 'Cash', 50.00, NULL, NULL, NULL, NULL, 1),
  (2, 'Cash', 75.00, NULL, NULL, NULL, NULL, 2),
  (3, 'Cash', 100.00, NULL, NULL, NULL, NULL, 3),
  (4, 'Credit', 125.00, 'John Doe', 1234567890123456, '2024-12-31 23:59:59', 123, 4),
  (5, 'Credit', 150.00, 'Jane Smith', 9876543210987654, '2025-06-30 23:59:59', 456, 5),
  (6, 'Debit', 175.00, 'Bob Johnson', 1111222233334444, '2023-03-31 23:59:59', 789, 6),
  (7, 'Cash', 80.00, NULL, NULL, NULL, NULL, 7),
  (8, 'Credit', 90.00, 'Alice Davis', 5555666677778888, '2025-09-30 23:59:59', 234, 8),
  (9, 'Debit', 110.00, 'Sarah Wilson', 4444333322221111, '2024-08-31 23:59:59', 567, 9),
  (10, 'Cash', 70.00, NULL, NULL, NULL, NULL, 10),
  (11, 'Credit', 120.00, 'Mark Thompson', 8888777766665555, '2023-11-30 23:59:59', 890, 11),
  (12, 'Debit', 95.00, 'Karen Brown', 7777666655554444, '2024-05-31 23:59:59', 123, 12),
  (13, 'Cash', 60.00, NULL, NULL, NULL, NULL, 13),
  (14, 'Credit', 130.00, 'David Lee', 2222333344445555, '2025-02-28 23:59:59', 456, 14),
  (15, 'Debit', 85.00, 'Michael Nguyen', 3333444455556666, '2023-10-31 23:59:59', 789, 15),
  (16, 'Cash', 55.00, NULL, NULL, NULL, NULL, 16),
  (17, 'Credit', 95.00, 'Mary Kim', 6666555577778888, '2023-06-30 23:59:59', 234, 17),
  (18, 'Debit', 120.00, 'Emily Chen', 7777888899990000, '2024-04-30 23:59:59', 567, 18),
  (19, 'Cash', 65.00, NULL, NULL, NULL, NULL, 19),
  (20, 'Credit', 110.00, 'Ryan Lee', 4444555566667777, '2024-12-31 23:59:59', 890, 20),
  (21, 'Debit', 75.00, 'Erica Chen', 9999888877776666, '2025-01-31 23:59:59', 123, 1),
  (22, 'Cash', 90.00, NULL, NULL, NULL, NULL, 2),
  (23, 'Credit', 105.00, 'Steven Chang', 1111222233334444, '2023-08-31 23:59:59', 456, 3),
  (24, 'Debit', 80.00, 'Linda Wang', 5555666677778888, '2024-06-30 23:59:59', 789, 4),
  (25, 'Cash', 100.00, NULL, NULL, NULL, NULL, 5);


/* Ticket */
INSERT INTO xzz_ticket (ticket_id, ticket_method, visit_date, ticket_price, order_id, visitor_id)
VALUES
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
  (25, 'Online', '2023-04-09 11:00:00', 50.00, 25, 5);


/* Parking */
INSERT INTO xzz_parking (parking_id, lot, spot, time_in, time_out, fee, order_id)
VALUES
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
  (25, 'Lot A', 25, '2023-04-09 10:00:00', '2023-04-09 15:00:00', 10.00, 7);


/* xzz_attr_visi */
INSERT INTO xzz_attr_visi (r_id, r_in_time, visitor_id, attraction_id)
VALUES
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
  (35, '2023-04-01 15:30:00', 10, 16);


/* xzz_orde_show */
INSERT INTO xzz_orde_show (os_id, show_id, order_id)
VALUES
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
  (35, 1, 13);


/* xzz_orde_stor */
INSERT INTO xzz_orde_stor (menu_item_id, menu_item_name, menu_item_description, menu_item_unit_price, store_id, order_id) VALUES
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
(35, 'Margarita', 'Classic tequila-based cocktail made with lime juice and triple sec, served with salt on the rim', 7.99, 3, 9);


CREATE PROCEDURE populate_summary_table(IN p_date DATETIME)
BEGIN
    DECLARE v_visitor_id INT;
    DECLARE v_visitor_date DATETIME;
    DECLARE v_amount DOUBLE;
    DECLARE v_source VARCHAR(10);
    DECLARE v_source_id DOUBLE;
    
    -- create summary table
    CREATE TABLE summary (
        visitor_id   DOUBLE NOT NULL,
        visitor_date DATETIME NOT NULL,
        amount       DOUBLE NOT NULL,
        source       VARCHAR(10) NOT NULL,
        source_id    DOUBLE NOT NULL
    );
    
    -- insert ticket payments into summary table
    INSERT INTO summary(visitor_id, visitor_date, amount, source, source_id)
    SELECT t.visitor_id, t.visit_date, t.ticket_price, 'Ticket', t.ticket_id
    FROM xzz_ticket t
    WHERE DATE(t.visit_date) = DATE(p_date);
    
    -- insert show payments into summary table
	INSERT INTO summary(visitor_id, visitor_date, amount, source, source_id)
	SELECT v.visitor_id, sw.start_time, sw.show_price, 'Show', sw.show_id
	FROM xzz_visitor v
    JOIN xzz_ticket t ON t.visitor_id = v.visitor_id
	JOIN xzz_order o ON v.visitor_id = o.visitor_id
	JOIN xzz_orde_show os ON o.order_id = os.order_id
	JOIN xzz_show sw ON sw.show_id = os.show_id
	WHERE DATE(sw.start_time) = DATE(p_date);
    
    -- insert store payments into summary table
	INSERT INTO summary (visitor_id, visitor_date, amount, source, source_id)
	SELECT v.visitor_id, t.visit_date, SUM(os.menu_item_unit_price), 'Store', o.order_id
	FROM xzz_visitor v
	JOIN xzz_ticket t ON t.visitor_id = v.visitor_id
	JOIN xzz_order o ON v.visitor_id = o.visitor_id
	JOIN xzz_orde_stor os ON os.order_id = o.order_id
	JOIN xzz_store st ON st.store_id = os.store_id
	WHERE DATE(o.order_date) = DATE(p_date)
	GROUP BY v.visitor_id, t.visit_date,  o.order_id;


    
    -- insert parking payment into summary table
    INSERT INTO summary(visitor_id, visitor_date, amount, source, source_id)
    SELECT v.visitor_id, p.time_in, p.fee, 'Parking', p.parking_id
    FROM xzz_visitor v
    JOIN xzz_ticket t ON t.visitor_id = v.visitor_id
    JOIN xzz_order o ON v.visitor_id = o.visitor_id
    JOIN xzz_parking p ON P.order_id = o.order_id
    WHERE DATE(p.time_in) = DATE(p_date);
    -- Assume that the parking time in is the date to match
END;

-- some test case (uncomment to test)
-- test for procedure

	-- CALL populate_summary_table('2023-04-01 09:00:00');
	-- SELECT * FROM summary;

-- test for data
SELECT COUNT(*) FROM  xzz_visitor;
SELECT COUNT(*) FROM  xzz_attraction;
SELECT COUNT(*) FROM  xzz_show;
SELECT COUNT(*) FROM  xzz_store;
SELECT COUNT(*) FROM  xzz_order;
SELECT COUNT(*) FROM  xzz_payment;
SELECT COUNT(*) FROM  xzz_ticket;
SELECT COUNT(*) FROM  xzz_parking;
SELECT COUNT(*) FROM  xzz_attr_visi;
SELECT COUNT(*) FROM  xzz_orde_show;
SELECT COUNT(*) FROM  xzz_orde_stor;



 CALL populate_summary_table(SYSDATE());
 SELECT * FROM summary;