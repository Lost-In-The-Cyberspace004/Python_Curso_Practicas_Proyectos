create database SistemaGestorDeInventarios;
use SistemaGestorDeInventarios;

drop table if exists Inventario;

create table Inventario(
	personID int primary Key auto_increment,
    Producto varchar(30) not null,
    Precio float,
    Cantidad int
);

insert into Inventario(Producto, Precio, Cantidad)
values('Rinion', 40000, 100), 
('Estomago', 50000, 100),
('Ojos', 5000, 10), 
('Mandibula y dientes', 30000, 10);

select * from Inventario;