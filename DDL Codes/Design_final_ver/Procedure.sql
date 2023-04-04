
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