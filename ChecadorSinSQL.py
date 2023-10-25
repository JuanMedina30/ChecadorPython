#Estas librerias son meramente estéticas, el programa puede funcionar sin ellas
import os #os es el modulo que permite limpiar la pantalla
import msvcrt  
from datetime import datetime

a=True

Empleados=[]
Matriculas=[]
Registros=[]
jUAN=[1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def RegistarAsistencia():
    os.system("cls")
    print("Registrar asistencia")
    print(" ")
    i=int(input("Ingrese la matrícula del empleado:"))
    temp=i
    
    if i in Matriculas:
        Matricula=temp
        Hora=datetime.now().strftime('%H:%M')
        Fecha=datetime.now().strftime('%d-%m-%Y')
        RegistroAsistencia=(Matricula,Hora,Fecha)
        Registros.append(RegistroAsistencia)
        print("Asistencia registrada")
        print("Presione cualquer tecla para continuar")
        msvcrt.getch()
    else:
        print("El empleado no existe")
        print("Presione cualquer tecla para continuar")
        msvcrt.getch()


def ConsultarAsistencia():
    print("Consultar asistencia")
    print("-------------------")
    print("Impleados registrados")
    print(Registros)
    print("Presione cualquer tecla para continuar")
    msvcrt.getch()    
    
def ModificarAsistencia():
    print("Modificar registro de asistencia")
    print("--------------------------------")
    x=int(input("Ingrese índice de datos a modificar: "))
    Matricula=int(input("Ingrese su matrícula: "))
    Hora=input("Ingrese la hora 00:00: ")
    Fecha=input("Ingresa la fecha (dd-mm-yyyy): ")
    RegistroAsistencia=(Matricula,Hora,Fecha)
    Registros.insert(x,RegistroAsistencia)
    Registros.pop(x-1)
    print("Registro modificado")
    print("Presione cualquer tecla para continuar")
    msvcrt.getch()  

def EliminarAsistencia():
    print("Eliminar registro")
    print("-----------------")
    print("1.- Elminar por índice")
    print("2.- Elimnar todos los datos")
    print("---------------------")
    x= int(input("Seleccione una opción"))
    if 1==x:
        os.system("cls")
        y=int(input("Ingrese el índice del registro a eliminar"))
        registroEliminado=Registros[y]
        Registros.pop(y)
        print(f"Registro {registroEliminado} ha sido eliminado")
        print("Presione cualquer tecla para continuar")
        msvcrt.getch()
    elif 2==x:
        os.system("cls")
        Registros.clear()
        print("Todos los registros han sido eliminado")
        print("Presione cualquer tecla para continuar")
        msvcrt.getch()

    else:
        print("Seleccione una opción válida")
        msvcrt.getch()

def AgregarEmpleado():
    print("Agregar empleado")
    print("----------------") 
    print("Datos del empleado")
    Matricula=int(input("Ingrese la matrícula: "))
    NombreEmpleado=input("Ingrese el  nombre(s): ")
    ApellidosEmpleado=input("Ingrese los apellidos: ")
    Rfc=input("Ingrese rfc: ") 
    Teléfono =int(input	("Ingrese el teléfono: ")) 
    Puesto=input("Ingrese el puesto: ")
    Salario= float(input("Ingrese el salario: "))
    RegistroEmpleado=(Matricula,NombreEmpleado,ApellidosEmpleado,Rfc,Teléfono,Puesto,Salario)
    Empleados.append(RegistroEmpleado)
    Matriculas.append(Matricula)
    print("Empleado agregado")
    print("Presione cualquer tecla para continuar")
    msvcrt.getch()  

def ConsularEmpleado():
    print("Consultar empleado")
    print("-------------------")
    print("Empleados registrados")
    print(Empleados)
    msvcrt.getch()  
    print("Presione cualquer tecla para continuar")
  
def ModificarEmpleado():
    print("Modificar datos empleado")
    print("-----------------------")
    x=int(input("Ingrese la posición del dato a eliminar"))
    Matricula=int(input("Ingrese la matrícula: "))
    NombreEmpleado=input("Ingrese el  nombre(s): ")
    ApellidosEmpleado=input("Ingrese los apellidos: ")
    Rfc=input("Ingrese rfc: ") 
    Teléfono =int(input	("Ingrese el teléfono: ")) 
    Puesto=input("Ingrese el puesto: ")
    Salario= float(input("Ingrese el salario: "))
    RegistroEmpleado=(Matricula,NombreEmpleado,ApellidosEmpleado,Rfc,Teléfono,Puesto,Salario)
    Empleados.insert(x,RegistroEmpleado)
    Matriculas.insert(x,x+1)
    Matriculas.pop(x+1)
    Empleados.pop(x+1)
    print("Registro modificado")
    msvcrt.getch()  

def EliminarEmpleado():
    print("Eliminar empleados")
    print("---------------------")
    print("1.- Elminar por índice")
    print("2.- Elimnar todos los datos")
    print("---------------------")
    x= int(input("Seleccione una opción"))
    if 1==x:
        os.system("cls")
        y=int(input("Ingrese el índice del empleado a eliminar"))
        registroEliminado=Empleados[y]
        Empleados.pop(y)
        print(f"Registro {registroEliminado} ha sido eliminado")
        msvcrt.getch()
    elif 2==x:
        os.system("cls")
        Empleados.clear()
        print("Todos los empleados han sido eliminado")
        msvcrt.getch()
    else:
        print("Seleccione una opción válida")
        msvcrt.getch()

#"Main" del programa
while True: #El bucle, que determinará hacía dónde se movera el usuario, ademas de finalizar el programa
    try:#En caso de que el usuario no selecciona una opcion válida, o ingrese un valor no admitible
        while a ==True:#Mientras "a" sea True el ciclo se repetira, y se podrá navegar indefinidamente 
            print("Proyecto registro de asistencia")
            print("----------------")
            print("1-.Registrar asistencia")
            print("2-.Consultar asistencia")
            print("3-.Modificar asistencia")
            print("4-.Eliminar asistencia")
            print("5-.Agregar empleados")
            print("6-.Consultar empleados")
            print("7-.Modificar emplados")
            print("8-.Eliminar empleados")
            print("9-.Salir")
            print("----------------")
            opc=int(input("Seleccione una opción: "))#Aqui se tomará el valor para "navegar" por los menús

            if opc== 1:
                RegistarAsistencia()
            elif opc== 2:                           
                ConsultarAsistencia()    
            elif opc==3:
                tamaño=len(Registros)#Aqui esta comprando el tamaño del arreglo
                if tamaño==0:#Si es 0(no tiene ningún valor) no te llamará a la función modificar
                    print("No existe un dato a modificar")
                    msvcrt.getch()    
                else:
                    ModificarAsistencia()    
            elif opc==4:
                tamaño=len(Registros)#Aqui esta comprando el tamaño del arreglo
                if tamaño==0:#Si es 0(no tiene ningún valor) no te llamará a la función eliminar
                    print("No existe un dato a eliminar")
                    msvcrt.getch()    
                else:
                    EliminarAsistencia()
            if opc== 5:
                AgregarEmpleado()
            elif opc== 6:                           
                ConsularEmpleado()     
            elif opc==7:
                tamaño=len(Empleados)#Aqui esta comprando el tamaño del arreglo
                if tamaño==0:#Si es 0(no tiene ningún valor) no te llamará a la función modificar
                    print("No existe un dato a modificar")
                    msvcrt.getch()    
                else:
                    ModificarEmpleado()    
            elif opc==8:
                tamaño=len(Empleados)#Aqui esta comprando el tamaño del arreglo
                if tamaño==0:#Si es 0(no tiene ningún valor) no te llamará a la función eliminar
                    print("No existe un dato a eliminar")
                    msvcrt.getch()    
                else:
                    EliminarEmpleado()    
            elif opc==9:
                os.system ("cls") 
                print("Saliste")
                print("----------------") 
                print("Presione una tecla para continuar...")
                msvcrt.getch()     
                a=False  #Al salir el bucle finaliza, y por ende el programa también 
            else:
                os.system ("cls") 
                #print("Escribe una opción válida")  #En caso de que el usuario no haya ingresado una opción válida
                msvcrt.getch()          
    except ValueError as e: #Por si el usuario ingreso un valor INVALIDO(Un string por ejemplo)
        print("Selecciona una opción valida")
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        os.system ("cls")   
    else: 
        break #Se termina el programa
