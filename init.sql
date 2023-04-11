CREATE TABLE taxidata (
  VendorID INTEGER,
  tpep_pickup_datetime TIMESTAMP,
  tpep_dropoff_datetime TIMESTAMP,
  passenger_count FLOAT,
  trip_distance FLOAT,
  RatecodeID FLOAT,
  store_and_fwd_flag TEXT,
  PULocationID INTEGER,
  DOLocationID INTEGER,
  payment_type INTEGER,
  fare_amount FLOAT,
  extra FLOAT,
  mta_tax FLOAT,
  tip_amount FLOAT,
  tolls_amount FLOAT,
  improvement_surcharge FLOAT,
  total_amount FLOAT,
  congestion_surcharge FLOAT,
  airport_fee FLOAT
);
COPY taxidata FROM '/tmp/taxidata.csv' DELIMITER ',' CSV HEADER;
