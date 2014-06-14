\c same_page

CREATE TABLE Users (
    id serial PRIMARY KEY,
    username varchar(30),
    pw varchar(30),
    groups text,
    joined timestamp
);

CREATE TABLE Groups (
    id serial PRIMARY KEY,
    group_id varchar(20),
    group_pads text,
    created timestamp
);


