CREATE TABLE country (
id 		serial primary key,
name 	varchar(50) unique not null
);

CREATE TABLE consulate (
id 				serial primary key,
country_id 		int not null,
address 		varchar(200),
email 			varchar(70),
working_hours 	varchar(100),
phone_number_1 	varchar(20),
phone_number_2	varchar(20),
foreign key(country_id) references country(id) ON DELETE CASCADE
);

CREATE TABLE visa_application_center (
id 						serial primary key,
country_id 				int not null,
address 				varchar(200),
email 					varchar(70),
apply_working_hours_1 	varchar(100),
issue_working_hours_2	varchar(100),
phone_number 			varchar(20),
foreign key(country_id) references country(id) ON DELETE CASCADE
);

CREATE TABLE news_details (
id 		serial primary key,
title 	varchar(70),
body 	varchar(350),
link 	varchar(100)
);

CREATE TABLE news (
id 				serial primary key,
country_id 		int not null,
news_details_id int not null,
date 			timestamp,
foreign key (country_id) 		references country (id) ON DELETE CASCADE,
foreign key (news_details_id)	references news_details (id) ON DELETE CASCADE
);

CREATE TABLE category (
id 		serial primary key,
name 	varchar(50) unique not null
);

CREATE TABLE subcategory (
id 			serial primary key,
name 		varchar(50) unique not null,
category_id int not null,
foreign key (category_id) references category (id) ON DELETE CASCADE
);

CREATE TABLE appointment (
id 			serial primary key,
vac_id 		int not null,
subcat_id 	int not null,
date 		timestamp,
foreign key (vac_id) 	references visa_application_center (id) ON DELETE CASCADE,
foreign key (subcat_id) references subcategory (id) ON DELETE CASCADE
);
