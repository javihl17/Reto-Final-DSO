# Access MySQL CLI
# mysql -u root -p ''

# create database
create database iot_data;

# Create a new user (only with local access) and grant privileges to this user on the new database:
grant all privileges on iot_data.* TO 'iot_user'@'%' identified by '9R[-RP#64nY7*E*H';

# After modifying the MariaDB grant tables, execute the following command in order to apply the changes:
flush privileges;

#Change to the created database
use iot_data;

# create table for sensor data
CREATE TABLE sensor_data (
 	id MEDIUMINT NOT NULL AUTO_INCREMENT,
 	device_id varchar(50) NOT NULL,
 	humidity float NOT NULL, 
 	temperature float NOT NULL,
 	time_stamp float NOT NULL,
 	PRIMARY KEY (id)
 );

# query over table sensor_data
#SELECT temperature, humidity FROM sensor_data ORDER BY id DESC LIMIT 1;

# create table for storing device IDs
CREATE TABLE devices (
 	id MEDIUMINT NOT NULL AUTO_INCREMENT, 
 	device_id varchar(50) NOT NULL,
 	status varchar(20) NOT NULL DEFAULT 'activo',
 	latitude float,
    longitude float,
    time_stamp float NOT NULL,
 	UNIQUE (device_id), 
 	PRIMARY KEY (id)
 );

# query over table sensor_data
#SELECT * FROM devices ORDER BY id DESC LIMIT 1;

#Implementación de un trigger en mariadb
delimiter $
CREATE TRIGGER add_devices 
BEFORE INSERT ON devices 
FOR EACH ROW 
BEGIN
if (select device_id from devices where device_id = new.device_id) is not null then
update devices 
set devices.status = 'inactivo' where device_id = new.device_id;
end if;
end
delimiter ;

#Evitando la tabla mutante: 
delimiter $
CREATE TRIGGER add_devices2 
BEFORE INSERT ON devices 
FOR EACH ROW 
begin
declare aux boolean
if (select device_id from devices where device_id = new.device_id) is not null then
set aux TRUE;
end if;

if aux is TRUE then
update 
set new.status = 'inactivo';
end if;
end;
delimiter ;
