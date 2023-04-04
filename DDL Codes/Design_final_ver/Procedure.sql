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