INSERT INTO users (username, user_role) VALUES
('jdoe', 'Trainer'),
('somesmith', 'Trainer'),
('thetrainer', 'Trainer');

INSERT INTO trainers (trainer_username, trainer_name) VALUES
('jdoe', 'John'),
('somesmith', 'Smith'),
('thetrainer', 'Linus');

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

INSERT INTO equipment_maintenance(equipment_name, cost, maintenance_date) VALUES 
('Cable', 200, '2024-04-10'),
('Chest Press', 123, '2024-03-18');
