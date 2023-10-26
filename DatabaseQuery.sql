create database ChecadorPython
use ChecadorPython

create table Empleado(
Matricula int primary key,
NombreEmpleado varchar(30),
ApellidoP varchar(30),
ApellidoM varchar(30),
RFC varchar(15) unique,
Telefono int,
Puesto varchar(30),
Salario decimal(7,2)
)

create table Asistencia (
MatriculaEmp int,
Hora time,
Fecha date

foreign key (MatriculaEmp) references Empleado(Matricula)
)
alter table Empleado alter column Salario int
alter table Asistencia alter column Hora varchar(6)
alter table Asistencia alter column Fecha varchar(20)
insert into Empleado values
(1,'Juan','Medina','Ramos','MEJOR1',664590234,'Operador',1200),
(2,'José','Mendoza','Reyes','MEJ3D1',66450343,'Ingeniero',12000),
(3,'Alan','Rodriguez','Camacho','RACMO3R',66423234,'Soporte',4300),
(4,'Lucas','King','Alvarez','LAUCK2E3D',664433234,'Ingeniero',12000),
(5,'Ramon','Ayala','Mendoza','ARAM3L4',664754580,'RH',5600),
(6,'Erika','Alvarez','Rosas','EAMRL35',66494043,'Operador',4200)
insert into Asistencia values 
(1,'11:37','10/27/2023'),
(2,'12:57','11/29/2023'),
(3,'09:30','11/26/2023'),
(4,'12:40','09/26/2023'),
(5,'11:37','10/26/2023')
