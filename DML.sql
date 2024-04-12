INSERT INTO users (username, user_role) VALUES
('omarshah', 'Member')
('jdoe', 'Trainer'),
('somesmith', 'Trainer'),
('thetrainer', 'Trainer');
('bgates', 'Admin'),
('melon', 'Admin');

INSERT INTO members (member_username, member_name, current_weight, current_height) VALUES
('omarshah', 'Omar', 135, 160);

INSERT INTO trainers (trainer_username, trainer_name) VALUES
('jdoe', 'John'),
('somesmith', 'Smith'),
('thetrainer', 'Linus');

INSERT INTO availability (trainer_username, avail_time) VALUES
('jdoe', '2024-04-10 09:00:00'),  
('jdoe', '2024-04-11 10:00:00'),  
('somesmith', '2024-04-10 10:00:00'), 
('somesmith', '2024-04-11 11:00:00'),  
('thetrainer', '2024-04-10 12:00:00'),
('thetrainer', '2024-04-10 13:00:00');

INSERT INTO group_fitness_classes (class_name, trainer_username, class_time) VALUES
('Cycling', 'jdoe', '2024-04-11 10:00:00'),
('Boxing', 'somesmith', '2024-04-10 12:00:00');

INSERT INTO group_fitness_participants(member_username, class_id) VALUES
('omarshah', 1);

INSERT INTO rooms(room_number, room_capacity) VALUES
(1, 5),
(2, 3),
(3, 10);

INSERT INTO room_bookings(room_number, booker_username, booking_time) VALUES 
(1, 'bgates', '2024-04-11 09:00:00');

INSERT INTO admins(admin_username, admin_name) VALUES
('bgates', 'Bill'),
('melon', 'Melon Tusk');

INSERT INTO equipment_maintenance(equipment_name, cost, maintenance_date) VALUES 
('Cable', 200, '2024-04-10'),
('Chest Press', 123, '2024-03-18');

INSERT INTO fitness_acheivments(member_username, goal_weight, goal_deadline) VALUES
('omarshah', 200, '2025-01-01');

INSERT INTO metrics(member_username, metric_type, metric_measure, date_measured) VALUES
('omarshah', BMI, 52, '2024-04-11');

INSERT INTO exercise_routine(member_username, routine_name, routine_description, duration) VALUES
('omarshah', 'PPL', 'a push pull legs routine', 90);

INSERT INTO pt_sessions(trainer_username, member_username, session_time) VALUES
('jdoe', 'omarshah', '2024-04-11 12:00:00');

INSERT INTO billings(member_username, amount, billing_description, billing_date) VALUES
('omarshah', 25, 'Membership Fee', '2024-04-11')