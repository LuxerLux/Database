import mysql.connector

mydb = mysql.connector.connect(
    host="**************************",
    user="****",
    port="*****",
    password="********************",
    database="*******"
)
futbol = mydb.cursor()


#############    Se crean las tablas         ###########

# # futbol.execute("CREATE TABLE Liga (Id_Liga_li INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Nombre_li VARCHAR(50) NOT NULL, País_li VARCHAR(50) NOT NULL, N_Edición_li INT(4) NOT NULL, N_Jornada_li INT(2) NOT NULL)")

# # futbol.execute("CREATE TABLE Equipos (Id_Equipos_eq INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Id_Liga_eq INT NOT NULL, Nombre_eq VARCHAR(50) NOT NULL, PJ_eq INT(7) NOT NULL, Victorias_eq INT(5) NOT NULL, Derrotas_eq INT(5) NOT NULL, Empates_eq INT(5) NOT NULL, GF_eq INT(5) NOT NULL, GC_eq INT(5) NOT NULL, Puntos_eq INT(7) NOT NULL, FOREIGN KEY (Id_Liga_eq) REFERENCES Liga(Id_Liga_li))")

# # futbol.execute("CREATE TABLE Jugadores (Id_Jugadores_ju INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Id_Liga_ju INT NOT NULL, Id_Equipos_ju INT NOT NULL, Nombre_ju VARCHAR(50) NOT NULL, PJ_ju INT(5) NOT NULL, Goles_ju INT(4) NOT NULL, Asistencias_ju INT(4) NOT NULL, Rojas_ju INT(3) NOT NULL, Amarillas_ju INT(3) NOT NULL, FOREIGN KEY (Id_Liga_ju) REFERENCES Liga(Id_Liga_li), FOREIGN KEY (Id_Equipos_ju) REFERENCES Equipos(Id_Equipos_eq))")

# # futbol.execute("CREATE TABLE Trofeos (Id_Trofeos_tr INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Id_Equipos_tr INT NOT NULL, Nombre_tr VARCHAR(50) NOT NULL, Tipo_tr VARCHAR(50) NOT NULL, Fecha_Inicio_tr YEAR NULL, Fecha_Final_tr YEAR NULL, G_Anterior_tr VARCHAR(50) NULL, FOREIGN KEY (Id_Equipos_tr) REFERENCES Equipos(Id_Equipos_eq))")

# # futbol.execute("CREATE TABLE Patrocinadores (Id_Patrocinadores_pa INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Id_Equipos_pa INT NOT NULL, Nombre_pa VARCHAR(50) NOT NULL, Fecha_Inicio_pa YEAR NULL, Fecha_Final_pa YEAR NULL, Dinero_Anual_pa INT(15) NOT NULL, FOREIGN KEY (Id_Equipos_pa) REFERENCES Equipos(Id_Equipos_eq))")



###########    Se insertan los valores       ################

# insertLiga = "INSERT INTO Liga (Id_Liga_li, Nombre_li, País_li, N_Edición_li, N_Jornada_li) VALUES (NULL, %s, %s, %s, %s)" ###En VALUES el id primary key se pone null para que sea autoincrement
# valoresLiga = [
#   ('LaLiga', 'España', '92', '14'),
#   ('Premier League', 'Reino Unido', '124', '16'),
#   ('Bundesliga', 'Alemania', '59', '15')
# ]
# futbol.executemany(insertLiga, valoresLiga)
# mydb.commit()


# insertEquipos = "INSERT INTO Equipos (Id_Equipos_eq, Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# valoresEquipos = [
#   ('1', 'Real Madrid CF', '14', '11', '1', '2', '33', '14', '35'),
#   ('1', 'FC.Barcelona', '14', '12', '1', '1', '33', '5', '37'),
#   ('2', 'Manchester City FC', '14', '10', '2', '2', '40', '14', '32'),
#   ('3', 'Bayern Munich', '15', '10', '1', '4', '49', '13', '34'),
#   ('3', 'Eintracht Fráncfort', '15', '8', '4', '3', '32', '24', '27')
# ]
# futbol.executemany(insertEquipos, valoresEquipos)
# mydb.commit()


# insertJugadores = "INSERT INTO Jugadores (Id_Jugadores_ju, Id_Liga_ju, Id_Equipos_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"
# valoresJugadores = [
#   ('1', '1', 'Karim Benzema', '7', '5', '1', '0', '0'),
#   ('1', '2', 'Pedro González (Pedri)', '14', '3', '0', '0', '0'),
#   ('2', '3', 'Erling Haaland', '13', '18', '3', '0', '2'),
#   ('3', '4', 'Christopher Nkunku', '15', '12', '2', '0', '1'),
#   ('3', '5', 'Mario Gotze', '15', '2', '1', '0', '0')
# ]
# futbol.executemany(insertJugadores, valoresJugadores)
# mydb.commit()


# insertTrofeos = "INSERT INTO Trofeos (Id_Trofeos_tr, Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr) VALUES (NULL, %s, %s, %s, %s, %s, %s)"
# valoresTrofeos = [
#   ('1', 'Champions League', 'Internacional', '2021', '2022', 'Chelsea'),
#   ('5', 'Europa League', 'Internacional', '2021', '2022', 'Villareal'),
#   ('1', 'Copa LaLiga', 'Nacional', '2021', '2022', 'Atlético de Madrid'),
#   ('3', 'Copa Premier League', 'Nacional', '2021', '2022', 'Manchester City'),
#   ('4', 'Copa Bundesliga', 'Nacional', '2021', '2022', 'Bayern Múnich')
# ]
# futbol.executemany(insertTrofeos, valoresTrofeos)
# mydb.commit()


# insertPatrocinadores = "INSERT INTO Patrocinadores (Id_Patrocinadores_pa, Id_Equipos_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa) VALUES (NULL, %s, %s, %s, %s, %s)"
# valoresPatrocinadores = [
#   ('1', 'Adidas', '1998', '2028', '110000000'),
#   ('1', 'Fly Emirates', '2011', '2027', '70000000'),
#   ('2', 'Nike', '1998', '2028', '105000000'),
#   ('2', 'Spotify', '2022', '2026', '60000000'),
#   ('3', 'Puma', '2019', '2029', '74000000')
# ]
# futbol.executemany(insertPatrocinadores, valoresPatrocinadores)
# mydb.commit()

#####################          CONSULTAR TABLA          ########################

def consulta_liga():
    futbol = mydb.cursor()
    futbol.execute("SELECT * FROM Liga")
    datos = futbol.fetchall()
    for datosLiga in datos:
        print(datosLiga)
    return datosLiga

def consulta_equipos():
    futbol = mydb.cursor()
    futbol.execute("SELECT * FROM Equipos")
    datos = futbol.fetchall()
    for datosEquipos in datos:
        print(datosEquipos)
    futbol.close()
    return datosEquipos

def consulta_jugadores():
    futbol = mydb.cursor()
    futbol.execute("SELECT * FROM Jugadores")
    datos = futbol.fetchall()
    for datosJugadores in datos:
        print(datosJugadores)
    futbol.close()
    return datosJugadores

def consulta_trofeos():
    futbol = mydb.cursor()
    futbol.execute("SELECT * FROM Trofeos")
    datos = futbol.fetchall()
    for datosTrofeos in datos:
        print(datosTrofeos)
    futbol.close()
    return datosTrofeos

def consulta_patrocinadores():
    futbol = mydb.cursor()
    futbol.execute("SELECT * FROM Patrocinadores")
    datos = futbol.fetchall()
    for datosPatrocinadores in datos:
        print(datosPatrocinadores)
    futbol.close()
    return datosPatrocinadores

########################         BUSCAR         #######################

def buscar_Liga(Id_Liga_li):
    futbol = mydb.cursor()
    buscarLiga= "SELECT * FROM Liga WHERE Id_Liga_li = {}".format(Id_Liga_li)
    futbol.execute(buscarLiga)
    datosLiga = futbol.fetchone()
    futbol.close()
    return datosLiga

def buscar_Equipos(Id_Equipos_eq):
    futbol = mydb.cursor()
    buscarEquipos= "SELECT * FROM Equipos WHERE Id_Equipos_eq = {}".format(Id_Equipos_eq)
    futbol.execute(buscarEquipos)
    datosEquipos = futbol.fetchone()
    futbol.close()
    return datosEquipos

def buscar_Jugadores(Id_Jugadores_ju):
    futbol = mydb.cursor()
    buscarJugadores= "SELECT * FROM Jugadores WHERE Id_Jugadores_ju = {}".format(Id_Jugadores_ju)
    futbol.execute(buscarJugadores)
    datosJugadores = futbol.fetchone()
    futbol.close()
    return datosJugadores

def buscar_Trofeos(Id_Trofeos_tr):
    futbol = mydb.cursor()
    buscarTrofeos= "SELECT * FROM Trofeos WHERE Id_Trofeos_tr = {}".format(Id_Trofeos_tr)
    futbol.execute(buscarTrofeos)
    datosTrofeos = futbol.fetchone()
    futbol.close()
    return datosTrofeos

def buscar_Patrocinadores(Id_Patrocinadores_pa):
    futbol = mydb.cursor()
    buscarPatrocinadores= "SELECT * FROM Patrocinadores WHERE Id_Patrocinadores_pa = {}".format(Id_Patrocinadores_pa)
    futbol.execute(buscarPatrocinadores)
    datosPatrocinadores = futbol.fetchone()
    futbol.close()
    return datosPatrocinadores

########################        INSERTAR         #######################

def insertar_Liga(Nombre_li, País_li, N_Edición_li, N_Jornada_li):
    futbol = mydb.cursor()                                                                      ### Las tres comillas permite insertar un string con todas las líneas que deseemos
    intertLiga='''INSERT INTO Liga (Nombre_li, País_li, N_Edición_li, N_Jornada_li)
    VALUES('{}', '{}', '{}', '{}')'''.format(Nombre_li, País_li, N_Edición_li, N_Jornada_li)    ###.format permite incluir en una cadena, texto ordinario y int, float, etc
    futbol.execute(intertLiga)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def insertar_Equipos(Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq):
    futbol = mydb.cursor()
    intertEquipos='''INSERT INTO Equipos (Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
    futbol.execute(intertEquipos)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def insertar_Jugadores(Id_Liga_ju, Id_Equipos_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju):
    futbol = mydb.cursor()
    intertJugadores='''INSERT INTO Jugadores (Id_Liga_ju, Id_Equipos_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Id_Liga_ju, Id_Equipos_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
    futbol.execute(intertJugadores)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def insertar_Trofeos(Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr):
    futbol = mydb.cursor()
    intertTrofeos='''INSERT INTO Trofeos (Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
    VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
    futbol.execute(intertTrofeos)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def insertar_Patrocinadores(Id_Equipos_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa):
    futbol = mydb.cursor()
    intertPatrocinadores='''INSERT INTO Patrocinadores (Id_Equipos_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
    VALUES('{}', '{}', '{}', '{}', '{}')'''.format(Id_Equipos_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
    futbol.execute(intertPatrocinadores)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

########################    ELIMINAR   ###########################

def elimina_Liga(Id_Liga_li):
    futbol = mydb.cursor()
    eliminarLiga='''DELETE FROM Liga WHERE Id_Liga_li = {}'''.format(Id_Liga_li)
    futbol.execute(eliminarLiga)
    n =futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def elimina_Equipos(Id_Equipos_eq):
    futbol = mydb.cursor()
    eliminarEquipos='''DELETE FROM Equipos WHERE Id_Equipos_eq = {}'''.format(Id_Equipos_eq)
    futbol.execute(eliminarEquipos)
    n =futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def elimina_Jugadores(Id_Jugadores_ju):
    futbol = mydb.cursor()
    eliminarJugadores='''DELETE FROM Jugadores WHERE Id_Jugadores_ju = {}'''.format(Id_Jugadores_ju)
    futbol.execute(eliminarJugadores)
    n =futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def elimina_Trofeos(Id_Trofeos_tr):
    futbol = mydb.cursor()
    eliminarTrofeos='''DELETE FROM Trofeos WHERE Id_Trofeos_tr = {}'''.format(Id_Trofeos_tr)
    futbol.execute(eliminarTrofeos)
    n =futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def elimina_Patrocinadores(Id_Patrocinadores_pa):
    futbol = mydb.cursor()
    eliminarPatrocinadores='''DELETE FROM Patrocinadores WHERE Id_Patrocinadores_pa = {}'''.format(Id_Patrocinadores_pa)
    futbol.execute(eliminarPatrocinadores)
    n =futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

########################       MODIFICAR      ###########################

def modifica_Liga(Id_Liga_li, Nombre_li, País_li, N_Edición_li, N_Jornada_li):
    futbol = mydb.cursor()
    modificarLiga='''UPDATE Liga SET Nombre_li='{}', País_li='{}', N_Edición_li='{}',
    N_Jornada_li='{}' WHERE Id_Liga_li={}'''.format(Nombre_li, País_li, N_Edición_li, N_Jornada_li, Id_Liga_li)
    futbol.execute(modificarLiga)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Equipos(Id_Equipos_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq):
    futbol = mydb.cursor()
    modificarEquipos='''UPDATE Equipos SET Nombre_eq='{}', PJ_eq='{}', Victorias_eq='{}', Derrotas_eq='{}', Empates_eq='{}', GF_eq='{}', GC_eq='{}',
    Puntos_eq='{}' WHERE Id_Equipos_eq={}'''.format(Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq, Id_Equipos_eq)
    futbol.execute(modificarEquipos)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Jugadores(Id_Jugadores_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju):
    futbol = mydb.cursor()
    modificarJugadores='''UPDATE Jugadores SET Nombre_ju='{}', PJ_ju='{}', Goles_ju='{}', Asistencias_ju='{}', Rojas_ju='{}',
    Amarillas_ju='{}' WHERE Id_Jugadores_ju={}'''.format(Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju, Id_Jugadores_ju)
    futbol.execute(modificarJugadores)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Trofeos(Id_Trofeos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr):
    futbol = mydb.cursor()
    modificarTrofeos='''UPDATE Trofeos SET Nombre_tr='{}', Tipo_tr='{}', Fecha_Inicio_tr='{}', Fecha_Final_tr='{}',
    G_Anterior_tr='{}' WHERE Id_Trofeos_tr={}'''.format(Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr, Id_Trofeos_tr)
    futbol.execute(modificarTrofeos)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Patrocinadores(Id_Patrocinadores_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa):
    futbol = mydb.cursor()
    modificarPatrocinadores='''UPDATE Patrocinadores SET Nombre_pa='{}', Fecha_Inicio_pa='{}', Fecha_Final_pa='{}',
    Dinero_Anual_pa='{}' WHERE Id_Patrocinadores_pa={}'''.format(Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa, Id_Patrocinadores_pa)
    futbol.execute(modificarPatrocinadores)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

################################################

def crear_Tabla(tabla):
    futbol = mydb.cursor()
    borrarTabla= "DROP TABLE {}".format(tabla)
    futbol.execute(borrarTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

################################################

def elimina_Tabla(tabla):
    futbol = mydb.cursor()
    borrarTabla= "DROP TABLE {}".format(tabla)
    futbol.execute(borrarTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

########################         MENUS         ###########################

menu='''\n
        MENU FUTBOL

*  a) Ver tablas           *
*  b) Consultar tabla      *
*  c) Insertar dato        *
*  d) Eliminar dato        *
*  e) Modificar dato       *
*  f) Borrar Tabla         *
*  g) Salir                *
'''

menuTabla='''\n
        MENU TABLA

*  1) Liga                 *
*  2) Equipos              *
*  3) Jugadores            *
*  4) Trofeos              *
*  5) Patrocinadores       *
*  6) Volver               *
'''

###################       APP       #######################

def main():

    opcion='0'
    while opcion !='G': 
        print(menu)
        opcion = input("\n¿Que opción deseas?").upper()

        ###Ver tablas
        if opcion == 'A':
            print("\nMenu tablas")

        ###Consultar tablas
        elif opcion == 'B':
            print("\nConsultar tabla")
            print(menuTabla)
            subopcionConsulta = input("\n¿Que tablas deseas consultar?").upper()
            if subopcionConsulta == '1':
                print("\nConsultar Liga")
                consulta_liga()
            elif subopcionConsulta == '2':
                print("\nConsultar Equipos")
                consulta_equipos()
            elif subopcionConsulta == '3':
                print("\nConsultar Jugadores")
                consulta_jugadores()
            elif subopcionConsulta == '4':
                print("\nConsultar Trofeos")
                consulta_trofeos()
            elif subopcionConsulta == '5':
                print("\nConsultar Patrocinadores")
                consulta_patrocinadores()
            elif subopcionConsulta == '6':
                print("\nVolver al menu")
                print(menu)
                opcion = input("\n¿Que opción deseas?").upper()

        ###Insertar datos
        elif opcion == 'C':
            print("\nInsertar datos")
            print(menuTabla)
            subopcionInsertar = input("\n¿En que tabla deseas insertar los datos?").upper()
            if subopcionInsertar == '1':
                print("\nInsertar datos Liga")
                Nombre_li = input("Nombre de la la liga: ")
                País_li = input("País donde se juega: ")
                N_Edición_li = input("Numero actual de temporada desde que se fundo: ")
                N_Jornada_li = input("Numero de partido del año: ")
                r = insertar_Liga(Nombre_li, País_li, N_Edición_li, N_Jornada_li)
                if(r==0):
                    print("\n-> No se pudo insertar...")
                else:
                    print("\n-> Se insertó correctamente")
            elif subopcionInsertar == '2':
                print("\nInsertar datos Equipos")
                print("\nConsultar Ligas para poner ID")
                consulta_liga()
                Id_Liga_eq = input("El ID de la liga: ")
                Nombre_eq = input("Nombre del equipo: ")
                PJ_eq = input("Numero de partidos jugados: ")
                Victorias_eq = input("Victorias: ")
                Derrotas_eq = input("Derrotas: ")
                Empates_eq = input("Empates: ")
                GF_eq = input("Goles a favor: ")
                GC_eq = input("Goles en contra: ")
                Puntos_eq = input("Puntos en la liga: ")
                r = insertar_Equipos(Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
                if(r==0):
                    print("\n-> No se pudo insertar...")
                else:
                    print("\n-> Se insertó correctamente")
            elif subopcionInsertar == '3':
                print("\nInsertar datos Jugadores")
                print("\nConsultar Ligas para poner ID")
                consulta_liga()
                Id_Liga_ju = input("El ID de la liga: ")
                print("\nConsultar Equipos para poner ID")
                consulta_equipos()
                Id_Equipos_ju = input("El ID del equipo: ")
                Nombre_ju = input("Nombre del jugador: ")
                PJ_ju = input("Partidos jugados: ")
                Goles_ju = input("Goles metidos: ")
                Asistencias_ju = input("Asistencias dadas: ")
                Rojas_ju = input("Tarjetas rojas: ")
                Amarillas_ju = input("Tarjetas amarillas: ")
                r = insertar_Jugadores(Id_Liga_ju, Id_Equipos_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
                if(r==0):
                    print("\n-> No se pudo insertar...")
                else:
                    print("\n-> Se insertó correctamente")
            elif subopcionInsertar == '4':
                print("\nInsertar datos Trofeos")
                print("\nConsultar Equipos para poner ID")
                consulta_equipos()
                Id_Equipos_tr = input("El ID del equipo ganador: ")
                Nombre_tr = input("Nombre del trofeo: ")
                Tipo_tr = input("Es nacional o internacional: ")
                Fecha_Inicio_tr = input("Año de inicio del torneo: ")
                Fecha_Final_tr = input("Año del final del torneo: ")
                G_Anterior_tr = input("Ganador anterior del torneo: ")
                r = insertar_Trofeos(Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
                if(r==0):
                    print("\n-> No se pudo insertar...")
                else:
                    print("\n-> Se insertó correctamente")
            elif subopcionConsulta == '5':
                print("\nInsertar datos Patrocinadores")
                print("\nConsultar Equipos para poner ID")
                consulta_equipos()
                Id_Equipos_pa = input("El ID del equipo que patrocina: ")
                Nombre_pa = input("Nombre del patrocinador: ")
                Fecha_Inicio_pa = input("Año en el que comenzó el patrocinio: ")
                Fecha_Final_pa = input("Año del final del patrocinio: ")
                Dinero_Anual_pa = input("Dinero aportado: ")
                r = insertar_Patrocinadores(Id_Equipos_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
                if(r==0):
                    print("\n-> No se pudo insertar...")
                else:
                    print("\n-> Se insertó correctamente")
            elif subopcionConsulta == '6':
                print("\nVolver al menu")
                print(menu)
                opcion = input("\n¿Que opción deseas?").upper()

        ###Eliminar datos
        elif opcion == 'D':
            print("\nEliminar datos")
            print(menuTabla)
            subopcionEliminar = input("\n¿En que tabla está el dato deseas eliminar?").upper()
            if subopcionEliminar == '1':
                print("\nEliminar datos Liga")
                consulta_liga()
                Id_Liga_li = int(input("\nIntroduce el ID de la liga que desea eliminar: "))
                r = elimina_Liga(Id_Liga_li)
                if(r==0):
                    print("\n-> No existe")
                else:
                    print("\n-> Se eliminó correctamente")
            elif subopcionEliminar == '2':
                print("\nEliminar datos Equipos")
                consulta_equipos()
                Id_Equipos_eq = int(input("\nIntroduce el ID del equipo que desea eliminar: "))
                r = elimina_Equipos(Id_Equipos_eq)
                if(r==0):
                    print("\n-> No existe")
                else:
                    print("\n-> Se eliminó correctamente")
            elif subopcionEliminar == '3':
                print("\nEliminar datos Jugadores")
                consulta_jugadores()
                Id_Jugadores_ju = int(input("\nIntroduce el ID del jugador que desea eliminar: "))
                r = elimina_Jugadores(Id_Jugadores_ju)
                if(r==0):
                    print("\n-> No existe")
                else:
                    print("\n-> Se eliminó correctamente")
            elif subopcionEliminar == '4':
                print("\nEliminar datos Trofeos")
                consulta_trofeos()
                Id_Trofeos_tr = int(input("\nIntroduce el ID del trofeo que desea eliminar: "))
                r = elimina_Trofeos(Id_Trofeos_tr)
                if(r==0):
                    print("\n-> No existe")
                else:
                    print("\n-> Se eliminó correctamente")
            elif subopcionEliminar == '5':
                print("\nEliminar datos Patrocinadoress")
                consulta_patrocinadores()
                Id_Patrocinadores_pa = int(input("\nIntroduce el ID del patrocinador que desea eliminar: "))
                r = elimina_Patrocinadores(Id_Patrocinadores_pa)
                if(r==0):
                    print("\n-> No existe")
                else:
                    print("\n-> Se eliminó correctamente")
            elif subopcionEliminar == '6':
                print("\nVolver al menu")
                print(menu)
                opcion = input("\n¿Que opción deseas?").upper()

        ###Modificar datos
        elif opcion == 'E':
            print("\nModificar datos")
            print(menuTabla)
            subopcionModificar = input("\n¿En que tabla está el dato deseas modificar?").upper()
            if subopcionModificar == '1':
                print("\nModificar Liga")
                consulta_liga()
                Id_Liga_li = int(input("Introduce el Id de la liga que desea modificar: "))
                p = buscar_Liga(Id_Liga_li)
                if p == None:
                    print("\n-> No existe")
                else:
                    print("\n-> Modificar: ")
                    Nombre_li = input("Introduce el nuevo nombre de la liga: ")
                    País_li = input("Introduce el nuevo país donde se juega: ")
                    N_Edición_li = input("Introduce el nuevo numero de temporada en que se fundo: ")
                    N_Jornada_li = input("Introduce el nuevo numero de partido del año: ")
                    r = modifica_Liga(Nombre_li, País_li, N_Edición_li, N_Jornada_li)
                    if(r==0):
                        print("\n-> Error al modificar...")
                    else:
                        print("\n-> Se modificó correctamente")
            elif subopcionModificar == '2':
                print("\nModificar Equipos")
                consulta_equipos()
                Id_Equipos_eq = int(input("Introduce el Id del equipo que desea modificar: "))
                p = buscar_Equipos(Id_Equipos_eq)
                if p == None:
                    print("\n-> No existe")
                else:
                    print("\n-> Modificar: ")
                    Nombre_eq = input("Introduce el nuevo nombre del equipo: ")
                    PJ_eq = input("Introduce el nuevo numero partidos jugados: ")
                    Victorias_eq = input("Introduce el nuevo numero de victorias: ")
                    Derrotas_eq = input("Introduce el nuevo numero de derrotas: ")
                    Empates_eq = input("Introduce el nuevo numero de empates: ")
                    GF_eq = input("Introduce el nuevo numero de goles a favor: ")
                    GC_eq = input("Introduce el nuevo numero de goles en contra: ")
                    Puntos_eq = input("Introduce el nuevo numero de puntos: ")
                    r = modifica_Equipos(Id_Equipos_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
                    if(r==0):
                        print("\n-> Error al modificar...")
                    else:
                        print("\n-> Se modificó correctamente")
            elif subopcionModificar == '3':
                print("\nModificar Jugadores")
                consulta_jugadores()
                Id_Jugadores_ju = int(input("Introduce el Id del jugador que desea modificar: "))
                p = buscar_Jugadores(Id_Jugadores_ju)
                if p == None:
                    print("\n-> No existe")
                else:
                    print("\n-> Modificar: ")
                    Nombre_ju = input("Introduce el nuevo nombre del jugador: ")
                    PJ_ju = input("Introduce el nuevo numero de partidos jugados: ")
                    Goles_ju = input("Introduce el nuevo numero de golres que ha marcado: ")
                    Asistencias_ju = input("Introduce el nuevo numero de asistencias que ha dado: ")
                    Rojas_ju = input("Introduce el nuevo numero de tarjetas rojas: ")
                    Amarillas_ju = input("Introduce el nuevo numero de tarjetas amarillas: ")
                    r = modifica_Jugadores(Id_Jugadores_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
                    if(r==0):
                        print("\n-> Error al modificar...")
                    else:
                        print("\n-> Se modificó correctamente")
            elif subopcionModificar == '4':
                print("\nModificar Trofeos")
                consulta_trofeos()
                Id_Trofeos_tr = int(input("Introduce el Id de trofeo que desea modificar: "))
                p = buscar_Trofeos(Id_Trofeos_tr)
                if p == None:
                    print("\n-> No existe")
                else:
                    print("\n-> Modificar: ")
                    Nombre_tr = input("Introduce el nuevo nombre del trofeo: ")
                    Tipo_tr = input("Introduce si es nacional o internacional: ")
                    Fecha_Inicio_tr = input("Introduce el año de inicio: ")
                    Fecha_Final_tr = input("Introduce el año que termina: ")
                    G_Anterior_tr = input("Introduce el ganador anterior: ")
                    r = modifica_Trofeos(Id_Trofeos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
                    if(r==0):
                        print("\n-> Error al modificar...")
                    else:
                        print("\n-> Se modificó correctamente")
            elif subopcionModificar == '5':
                print("\nModificar Patrocinadores")
                consulta_patrocinadores()
                Id_Patrocinadores_pa = int(input("Introduce el Id de patrocinador que desea modificar: "))
                p = buscar_Patrocinadores(Id_Patrocinadores_pa)
                if p == None:
                    print("\n-> No existe")
                else:
                    print("\n-> Modificar: ")
                    Nombre_pa = input("Introduce el nombre de la liga: ")
                    Fecha_Inicio_pa = input("Introduce el año de inicio: ")
                    Fecha_Final_pa = input("Introduce el año que termina: ")
                    Dinero_Anual_pa = input("Introduce el dinero ofrecido: ")
                    r = modifica_Patrocinadores(Id_Patrocinadores_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
                    if(r==0):
                        print("\n-> Error al modificar...")
                    else:
                        print("\n-> Se modificó correctamente")
            elif subopcionModificar == '6':
                print("\nVolver al menu")
                print(menu)
                opcion = input("\n¿Que opción deseas?")
        ##
        elif opcion == 'F':
            print("\nCrear tabla")
            print(menuTabla)
            print(input("\n¿Que tabla deseas crear?"))        
            
                
        ###Borrar tabla
        elif opcion == 'F':
            print("\n¿Que tabla quieres borrar?")
            subopcionBorrar = input("\n¿Que tabla deseas borar?").upper()
            tabla = input("\nEscribe el nombre de la tabla:")
            r = elimina_Tabla(tabla)
            print("\n-> Se eliminó correctamente")
            if subopcionBorrar == '1':
                futbol = mydb.cursor()
                borrarLiga= "DROP TABLE Liga"
                futbol.execute(borrarLiga)
                futbol.close()
            elif subopcionBorrar == '2':
                futbol = mydb.cursor()
                borrarEquipos= "DROP TABLE Equipos"
                futbol.execute(borrarEquipos)
                futbol.close()
            elif subopcionBorrar == '3':
                futbol = mydb.cursor()
                borrarJugadores= "DROP TABLE Jugadores"
                futbol.execute(borrarJugadores)
                futbol.close()
            elif subopcionBorrar == '4':
                futbol = mydb.cursor()
                borrarTrofeos= "DROP TABLE Trofeos"
                futbol.execute(borrarTrofeos)
                futbol.close()
            elif subopcionBorrar == '5':
                futbol = mydb.cursor()
                borrarPatrocinadores= "DROP TABLE Patrocinadores"
                futbol.execute(borrarPatrocinadores)
                futbol.close()
            elif subopcionBorrar == '6':
                print("\nVolver al menu")
                print(menu)
                opcion = input("\n¿Que opción deseas?").upper()

        ###Salir
        elif opcion == 'G':
            print("\n-> Saliendo del sistema")

        else:
            print("\n-> Opción no válida")


if __name__ == "__main__":
    main()


