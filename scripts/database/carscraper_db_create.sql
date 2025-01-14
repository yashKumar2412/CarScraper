DROP TABLE IF EXISTS car_deals;

CREATE TABLE car_deals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    Brand VARCHAR(255),
    Image_URL VARCHAR(255),
    Model VARCHAR(255),
    MSRP NUMERIC,
    Monthly_Payment NUMERIC,
    Due_at_Signing NUMERIC,
    Down_Payment NUMERIC,
    Bank_Fee NUMERIC,
    Total_Payments NUMERIC,
    Purchase_Option NUMERIC,
    Termination_Fee NUMERIC,
    Excess_Mile_Fee NUMERIC,
    Miles_per_Year NUMERIC,
    Doc_Fee NUMERIC,
    Offer_Starts DATE,
    Offer_Ends DATE,
    Lease_Term NUMERIC,
    Lease_Bonus NUMERIC,
    Drivetrain VARCHAR(255),
    Trim VARCHAR(255)
);