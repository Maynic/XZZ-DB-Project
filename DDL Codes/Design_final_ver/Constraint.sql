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