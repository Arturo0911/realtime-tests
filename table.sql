

create table reading_values (
    id int(11) PRIMARY KEY auto_increment, 
    date_reading datetime NOT NULL DEFAULT current_timestamp, 
    temperature float not null, 
    humidity float not null, 
    dioxide float not null, 
    radiation float not null
);


create table levels_values(
    id int(11) PRIMARY KEY auto_increment, 
    date_reading timestamp NOT NULL DEFAULT current_timestamp, 
    temperature_min float not null, 
    temperature_max float not null, 
    humidity_min float not null, 
    humidity_max float not null, 
    dioxide_min float not null, 
    dioxide_max float not null, 
    uv_min float not null, 
    uv_max float not null
);

LOAD DATA INFILE '/home/payload/Documents/reading_values.csv' 
INTO TABLE reading_values
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;