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