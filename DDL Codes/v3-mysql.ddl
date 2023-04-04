-- SQLINES DEMO *** le SQL Developer Data Modeler 22.2.0.165.1149
-- SQLINES DEMO *** -04-04 00:36:51 EDT
-- SQLINES DEMO *** le Database 21c
-- SQLINES DEMO *** le Database 21c



-- SQLINES DEMO *** no DDL - MDSYS.SDO_GEOMETRY

-- SQLINES DEMO *** no DDL - XMLTYPE

-- SQLINES LICENSE FOR EVALUATION USE ONLY
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
    order_id       DOUBLE NOT NULL,
    order_date     DATETIME NOT NULL,
    order_quantity DOUBLE NOT NULL,
    visitor_id     DOUBLE NOT NULL
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
CREATE UNIQUE INDEX xzz_ticket__idx ON
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



-- SQLINES DEMO *** per Data Modeler Summary Report: 
-- 
-- SQLINES DEMO ***                        11
-- SQLINES DEMO ***                         1
-- SQLINES DEMO ***                        22
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** DY                      0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***  TYPE                   0
-- SQLINES DEMO ***  TYPE                   0
-- SQLINES DEMO ***  TYPE BODY              0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** EGMENT                  0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** ED VIEW                 0
-- SQLINES DEMO *** ED VIEW LOG             0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** A                       0
-- SQLINES DEMO *** T                       0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
