create table users(
    username varchar(255) not null,    
    user_role varchar(255) not null,
    member_id SERIAL PRIMARY KEY
);

create table members(
    member_username varchar(255) not null,    
    member_name varchar(255) not null,
    current_weight int,
    current_height int,
    member_id SERIAL PRIMARY KEY
);

create table trainers(
    trainer_username varchar(255) not null,    
    trainer_name varchar(255) not null,
    trainer_id SERIAL PRIMARY KEY
);

create table admins(
    admin_username varchar(255) not null,    
    admin_name varchar(255) not null,
    admin_id SERIAL PRIMARY KEY
);

create table fitness_acheivments(
    member_username varchar(255) not null,    
    goal_weight int, 
    goal_deadline date,
    acheivment_id SERIAL PRIMARY KEY
);

create table metrics(
    member_username varchar(255) not null,    
    metric_type varchar(255) not null,
    metric_measure int,
    date_measured date,
    metric_id SERIAL PRIMARY KEY
);

create table exercise_routine(
    member_username varchar(255) not null,    
    routine_name varchar(255) not null,
    routine_description varchar(255) not null,
    duration int,
    routine_id SERIAL PRIMARY KEY
);

create table availability(
    trainer_username varchar(255) not null,    
    avail_time timestamp,
    availability_id SERIAL PRIMARY KEY
);

create table pt_sessions(
    trainer_username varchar(255) not null,    
    member_username varchar(255) not null,    
    session_time timestamp,
    session_id SERIAL PRIMARY KEY
);

create table group_fitness_classes(
    class_name varchar(255) not null,   
    trainer_username varchar(255) not null,    
    class_time timestamp,
    class_id SERIAL PRIMARY KEY
);

create table group_fitness_participants(
    member_username varchar(255) not null,
    class_id int PRIMARY KEY
);

create table room_bookings(
    room_number int,   
    booker_username varchar(255) not null,    
    booking_time timestamp,
    booking_id SERIAL PRIMARY KEY
);

create table rooms(
    room_number int PRIMARY KEY,   
    room_capacity int
);

create table billings(
    member_username varchar(255) not null,
    amount int,    
    billing_description varchar(255) not null,
    billing_date date,
    billing_id SERIAL PRIMARY KEY
);

create table payments(
    member_username varchar(255) not null,   
    amount int,    
    payment_description varchar(255) not null,
    payment_date date,
    transaction_id SERIAL PRIMARY KEY
);

INSERT INTO users (username, user_role) VALUES
('jdoe', 'Trainer'),
('somesmith', 'Trainer'),
('thetrainer', 'Trainer');

INSERT INTO trainers (trainer_username, trainer_name) VALUES
('jdoe', 'John'),
('somesmith', 'Smith'),
('thetrainer', 'Omair');

INSERT INTO availability (trainer_username, avail_time) VALUES
('jdoe', '2024-04-10 09:00:00'),  
('jdoe', '2024-04-11 10:00:00'),  
('somesmith', '2024-04-10 10:30:00'), 
('somesmith', '2024-04-11 11:30:00'),  
('thetrainer', '2024-04-10 12:00:00'),
('thetrainer', '2024-04-10 13:00:00');

INSERT INTO group_fitness_classes (class_name, trainer_username, class_time) VALUES
('Cycling', 'jdoe', '2024-04-11 10:00:00'),
('Boxing', 'somesmith', '2024-04-10 12:00:00');

INSERT INTO rooms(room_number, room_capacity) VALUES
(1, 5),
(2, 3),
(3, 10);

INSERT INTO admins(admin_username, admin_name) VALUES
('bgates', 'Bill'),
('melon', 'Melon Tusk');

INSERT INTO users (username, user_role) VALUES
('bgates', 'Admin'),
('melon', 'Admin');