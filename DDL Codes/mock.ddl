INSERT INTO xzz_visitor (visitor_id, visitor_name, birth_date, visitor_type, address, city, state, zip, email, phone) VALUES
(100, 'John Smith', '1990-01-01', 'Adult', '123 Main St', 'New York', 'NY', 10001, 'john.smith@example.com', 555-1234),
(101, 'Jane Doe', '1995-05-05', 'Student', '456 Elm St', 'Los Angeles', 'CA', 90001, 'jane.doe@example.com', 555-5678),
(102, 'Bob Johnson', '1985-03-15', 'Adult', '789 Oak St', 'Chicago', 'IL', 60007, 'bob.johnson@example.com', 555-9012),
(103, 'Mary Lee', '1992-12-25', 'Senior', '246 Maple St', 'Houston', 'TX', 77002, 'mary.lee@example.com', 555-3456),
(104, 'David Chen', '2000-06-10', 'Student', '369 Pine St', 'San Francisco', 'CA', 94110, 'david.chen@example.com', 555-7890),
(105, 'Julia Park', '1975-08-20', 'Senior', '135 Cedar St', 'Seattle', 'WA', 98101, 'julia.park@example.com', 555-2345),
(106, 'Samuel Kim', '1988-11-30', 'Adult', '579 Walnut St', 'Boston', 'MA', 02108, 'samuel.kim@example.com', 555-6789),
(107, 'Karen Wong', '1998-04-02', 'Student', '246 Oak St', 'Los Angeles', 'CA', 90001, 'karen.wong@example.com', 555-1234),
(108, 'Michael Chan', '1980-07-20', 'Adult', '369 Elm St', 'San Francisco', 'CA', 94110, 'michael.chan@example.com', 555-5678),
(109, 'Amy Chen', '1993-02-14', 'Student', '123 Pine St', 'New York', 'NY', 10001, 'amy.chen@example.com', 555-9012),
(110, 'Tom Brown', '1972-09-30', 'Senior', '789 Maple St', 'Chicago', 'IL', 60007, 'tom.brown@example.com', 555-3456),
(111, 'Cathy Lee', '1991-07-05', 'Adult', '246 Oak St', 'Houston', 'TX', 77002, 'cathy.lee@example.com', 555-7890),
(112, 'Kevin Smith', '2002-01-20', 'Student', '579 Cedar St', 'Seattle', 'WA', 98101, 'kevin.smith@example.com', 555-2345),
(113, 'Emily Wang', '1978-04-18', 'Senior', '135 Walnut St', 'Boston', 'MA', 02108, 'emily.wang@example.com', 555-6789),
(114, 'Jake Johnson', '1997-11-05', 'Student', '369 Oak St', 'San Francisco', 'CA', 94110, 'jake.johnson@example.com', 555-1234);

INSERT INTO xzz_order (order_id, order_date, order_quantity, visitor_id) VALUES
(1, '2023-04-01 10:00:00', 2, 100),
(2, '2023-04-01 11:00:00', 1, 101),
(3, '2023-04-02 12:00:00', 4, 102),
(4, '2023-04-02 13:00:00', 3, 103),
(5, '2023-04-03 14:00:00', 2, 104),
(6, '2023-04-03 15:00:00', 1, 105),
(7, '2023-04-04 16:00:00', 4, 106),
(8, '2023-04-04 17:00:00', 3, 107),
(9, '2023-04-05 18:00:00', 2, 108),
(10, '2023-04-05 19:00:00', 1, 109);

INSERT INTO xzz_ticket (ticket_id, ticket_method, visit_date, ticket_price, order_id, visitor_id) VALUES
(1, 'Online', '2023-04-01 11:00:00', 25.00, 1, 100),
(2, 'Onsite', '2023-04-01 12:00:00', 30.00, 1, 100),
(3, 'Online', '2023-04-02 13:00:00', 20.00, 2, 101),
(4, 'Onsite', '2023-04-02 14:00:00', 25.00, 2, 101),
(5, 'Online', '2023-04-03 15:00:00', 35.00, 3, 102),
(6, 'Onsite', '2023-04-03 16:00:00', 40.00, 3, 102),
(7, 'Online', '2023-04-04 17:00:00', 15.00, 4, 103),
(8, 'Onsite', '2023-04-04 18:00:00', 20.00, 4, 103),
(9, 'Online', '2023-04-05 19:00:00', 30.00, 5, 104),
(10, 'Onsite', '2023-04-05 20:00:00', 35.00, 5, 104);
