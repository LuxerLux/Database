import mysql.connector

mydb = mysql.connector.connect(
    host="containers-us-west-102.railway.app",
    user="root",
    port="####",
    password="###########",
    database="railway"
)
futbol = mydb.cursor()


#################    SE CREAN LAS TABLAS    #################

# futbol.execute("CREATE TABLE Equipos (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Liga_eq INT NOT NULL, Nombre_eq VARCHAR(50) NOT NULL, PJ_eq INT(7) NOT NULL, Victorias_eq INT(5) NOT NULL, Derrotas_eq INT(5) NOT NULL, Empates_eq INT(5) NOT NULL, GF_eq INT(5) NOT NULL, GC_eq INT(5) NOT NULL, Puntos_eq INT(7) NOT NULL, FOREIGN KEY (ID_Liga_eq) REFERENCES Liga (ID))")

# futbol.execute("CREATE TABLE Jugadores (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Liga_ju INT NOT NULL, ID_Equipos_ju INT NOT NULL, Nombre_ju VARCHAR(50) NOT NULL, PJ_ju INT(5) NOT NULL, Goles_ju INT(4) NOT NULL, Asistencias_ju INT(4) NOT NULL, Rojas_ju INT(3) NOT NULL, Amarillas_ju INT(3) NOT NULL, FOREIGN KEY (ID_Liga_ju) REFERENCES Liga(ID), FOREIGN KEY (ID_Equipos_ju) REFERENCES Equipos (ID))")

# futbol.execute("CREATE TABLE Liga (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Nombre_li VARCHAR(50) NOT NULL, País_li VARCHAR(50) NOT NULL, N_Edición_li INT(4) NOT NULL, N_Jornada_li INT(2) NOT NULL)")

# futbol.execute("CREATE TABLE Patrocinadores (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Equipos_pa INT NOT NULL, Nombre_pa VARCHAR(50) NOT NULL, Fecha_Inicio_pa YEAR NOT NULL, Fecha_Final_pa YEAR NOT NULL, Dinero_Anual_pa INT(15) NOT NULL, FOREIGN KEY (ID_Equipos_pa) REFERENCES Equipos (ID))")

# futbol.execute("CREATE TABLE Trofeos (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Equipos_tr INT NOT NULL, Nombre_tr VARCHAR(50) NOT NULL, Tipo_tr VARCHAR(50) NOT NULL, Fecha_Inicio_tr YEAR NULL, Fecha_Final_tr YEAR NULL, G_Anterior_tr VARCHAR(50) NULL, FOREIGN KEY (ID_Equipos_tr) REFERENCES Equipos (ID))")

###############    SE INSERTAN LOS VALORES     ##################

# insertEquipos = "INSERT INTO Equipos (ID, Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# valoresEquipos = [
#   ('1', 'Real Madrid CF', '14', '11', '1', '2', '33', '14', '35'),
#   ('1', 'FC.Barcelona', '14', '12', '1', '1', '33', '5', '37'),
#   ('2', 'Manchester City FC', '14', '10', '2', '2', '40', '14', '32'),
#   ('3', 'Bayern Munich', '15', '10', '1', '4', '49', '13', '34'),
#   ('3', 'Eintracht Fráncfort', '15', '8', '4', '3', '32', '24', '27')
# ]
# futbol.executemany(insertEquipos, valoresEquipos)
# mydb.commit()

# insertJugadores = "INSERT INTO Jugadores (ID, Id_Liga_ju, Id_Equipos_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"
# valoresJugadores = [
#   ('1', '1', 'Karim Benzema', '7', '5', '1', '0', '0'),
#   ('1', '2', 'Pedro González (Pedri)', '14', '3', '0', '0', '0'),
#   ('2', '3', 'Erling Haaland', '13', '18', '3', '0', '2'),
#   ('3', '4', 'Christopher Nkunku', '15', '12', '2', '0', '1'),
#   ('3', '5', 'Mario Gotze', '15', '2', '1', '0', '0')
# ]
# futbol.executemany(insertJugadores, valoresJugadores)
# mydb.commit()

# insertLiga = "INSERT INTO Liga (ID, Nombre_li, País_li, N_Edición_li, N_Jornada_li) VALUES (NULL, %s, %s, %s, %s)" ###En VALUES el id primary key se pone null para que sea autoincrement
# valoresLiga = [
#   ('LaLiga', 'España', '92', '14'),
#   ('Premier League', 'Reino Unido', '124', '16'),
#   ('Bundesliga', 'Alemania', '59', '15')
# ]
# futbol.executemany(insertLiga, valoresLiga)
# mydb.commit()

# insertPatrocinadores = "INSERT INTO Patrocinadores (ID, Id_Equipos_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa) VALUES (NULL, %s, %s, %s, %s, %s)"
# valoresPatrocinadores = [
#   ('1', 'Adidas', '1998', '2028', '110000000'),
#   ('1', 'Fly Emirates', '2011', '2027', '70000000'),
#   ('2', 'Nike', '1998', '2028', '105000000'),
#   ('2', 'Spotify', '2022', '2026', '60000000'),
#   ('3', 'Puma', '2019', '2029', '74000000')
# ]
# futbol.executemany(insertPatrocinadores, valoresPatrocinadores)
# mydb.commit()

# insertTrofeos = "INSERT INTO Trofeos (ID, Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr) VALUES (NULL, %s, %s, %s, %s, %s, %s)"
# valoresTrofeos = [
#   ('1', 'Champions League', 'Internacional', '2021', '2022', 'Chelsea'),
#   ('5', 'Europa League', 'Internacional', '2021', '2022', 'Villareal'),
#   ('1', 'Copa LaLiga', 'Nacional', '2021', '2022', 'Atlético de Madrid'),
#   ('3', 'Copa Premier League', 'Nacional', '2021', '2022', 'Manchester City'),
#   ('4', 'Copa Bundesliga', 'Nacional', '2021', '2022', 'Bayern Múnich')
# ]
# futbol.executemany(insertTrofeos, valoresTrofeos)
# mydb.commit()

####################          VER TABLAS BASE DE DATOS         #####################

def ver_tablas():
    futbol = mydb.cursor()
    verTablas = '''SHOW TABLES FROM railway'''
    futbol.execute(verTablas)
    tablas = futbol.fetchall()
    print("\nTablas de la base de datos:")
    for indices, nombre in enumerate(tablas):     #permite enumerar los indices y los nombres de las tablas uno a uno
        print("{}. {}".format(indices + 1,nombre[0]))
    return tablas

#######################          CONSULTAR TABLA          ##########################

def consulta_tabla(tabla):
    futbol = mydb.cursor()
    consultarTabla = '''SELECT * FROM {}'''.format(tabla)
    futbol.execute(consultarTabla)
    datos = futbol.fetchall()
    for indices, nombres in enumerate(datos):
        print("{}. {}".format(indices + 1,nombres))
    return datos

########################         BUSCAR         #######################

def buscar_Equipos(Id_Equipos_eq):
    futbol = mydb.cursor()
    buscarEquipos= "SELECT * FROM Equipos WHERE ID = {}".format(Id_Equipos_eq)
    futbol.execute(buscarEquipos)
    datosEquipos = futbol.fetchone()
    futbol.close()
    return datosEquipos

def buscar_Jugadores(Id_Jugadores_ju):
    futbol = mydb.cursor()
    buscarJugadores= "SELECT * FROM Jugadores WHERE ID = {}".format(Id_Jugadores_ju)
    futbol.execute(buscarJugadores)
    datosJugadores = futbol.fetchone()
    futbol.close()
    return datosJugadores

def buscar_Liga(Id_Liga_li):
    futbol = mydb.cursor()
    buscarLiga= "SELECT * FROM Liga WHERE ID = {}".format(Id_Liga_li)
    futbol.execute(buscarLiga)
    datosLiga = futbol.fetchone()
    futbol.close()
    return datosLiga

def buscar_Patrocinadores(Id_Patrocinadores_pa):
    futbol = mydb.cursor()
    buscarPatrocinadores= "SELECT * FROM Patrocinadores WHERE ID = {}".format(Id_Patrocinadores_pa)
    futbol.execute(buscarPatrocinadores)
    datosPatrocinadores = futbol.fetchone()
    futbol.close()
    return datosPatrocinadores

def buscar_Trofeos(Id_Trofeos_tr):
    futbol = mydb.cursor()
    buscarTrofeos= "SELECT * FROM Trofeos WHERE ID = {}".format(Id_Trofeos_tr)
    futbol.execute(buscarTrofeos)
    datosTrofeos = futbol.fetchone()
    futbol.close()
    return datosTrofeos

def buscar_Entrenadores(Id_Entrenadores_en):
    futbol = mydb.cursor()
    buscarEntrenadores= "SELECT * FROM Entrenadores WHERE ID = {}".format(Id_Entrenadores_en)
    futbol.execute(buscarEntrenadores)
    datosEntrenadores = futbol.fetchone()
    futbol.close()
    return datosEntrenadores

def buscar_Presidentes(Id_Presidentes_pr):
    futbol = mydb.cursor()
    buscarPresidentes= "SELECT * FROM Presidentes WHERE ID = {}".format(Id_Presidentes_pr)
    futbol.execute(buscarPresidentes)
    datosPresidentes = futbol.fetchone()
    futbol.close()
    return datosPresidentes

########################        INSERTAR         #######################

def insertar_Equipos(Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq):                                                      ### Las tres comillas permite insertar un string con todas las líneas que deseemos
    futbol = mydb.cursor()
    intertEquipos='''INSERT INTO Equipos (Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)  
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq) ###.format permite incluir en una cadena, texto ordinario y int, float, etc
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

def insertar_Liga(Nombre_li, País_li, N_Edición_li, N_Jornada_li):
    futbol = mydb.cursor()                                                                      
    intertLiga='''INSERT INTO Liga (Nombre_li, País_li, N_Edición_li, N_Jornada_li)
    VALUES('{}', '{}', '{}', '{}')'''.format(Nombre_li, País_li, N_Edición_li, N_Jornada_li)    
    futbol.execute(intertLiga)
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

def insertar_Trofeos(Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr):
    futbol = mydb.cursor()
    intertTrofeos='''INSERT INTO Trofeos (Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
    VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
    futbol.execute(intertTrofeos)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def insertar_Entrenadores(Id_Liga_en, Id_Equipos_en, Nombre_en, PJ_en, Rojas_en, Amarillas_en):
    futbol = mydb.cursor()
    modificarEntrenadores='''INSERT INTO Entrenadores (Id_Liga_en, Id_Equipos_en, Nombre_en, PJ_ju, Rojas_en, Amarillas_en)
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Id_Liga_en, Id_Equipos_en, Nombre_en, PJ_en, Rojas_en, Amarillas_en)
    futbol.execute(modificarEntrenadores)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def insertar_Presidentes(Id_Equipos_pr, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr):
    futbol = mydb.cursor()
    modificarPresidentes='''INSERT INTO Presidentes (Id_Equipos_pr, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr)
    VALUES('{}', '{}', '{}', '{}', '{}')'''.format(Id_Equipos_pr, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr)
    futbol.execute(modificarPresidentes)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

########################    ELIMINAR   ###########################

def borrar_DatoTabla(tabla,numId):
    futbol = mydb.cursor()
    eliminarDato='''DELETE FROM {} WHERE ID = {}'''.format(tabla,numId)
    futbol.execute(eliminarDato)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

########################       MODIFICAR      ###########################

def modifica_Equipos(ID, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq):
    futbol = mydb.cursor()
    modificarEquipos='''UPDATE Equipos SET Nombre_eq='{}', PJ_eq='{}', Victorias_eq='{}', Derrotas_eq='{}', Empates_eq='{}', GF_eq='{}', GC_eq='{}',
    Puntos_eq='{}' WHERE ID={}'''.format(Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq, ID)
    futbol.execute(modificarEquipos)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Jugadores(ID, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju):
    futbol = mydb.cursor()
    modificarJugadores='''UPDATE Jugadores SET Nombre_ju='{}', PJ_ju='{}', Goles_ju='{}', Asistencias_ju='{}', Rojas_ju='{}',
    Amarillas_ju='{}' WHERE ID={}'''.format(Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju, ID)
    futbol.execute(modificarJugadores)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Liga(ID, Nombre_li, País_li, N_Edición_li, N_Jornada_li):
    futbol = mydb.cursor()
    modificarLiga='''UPDATE Liga SET Nombre_li='{}', País_li='{}', N_Edición_li='{}',
    N_Jornada_li='{}' WHERE ID={}'''.format(Nombre_li, País_li, N_Edición_li, N_Jornada_li, ID)
    futbol.execute(modificarLiga)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Patrocinadores(ID, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa):
    futbol = mydb.cursor()
    modificarPatrocinadores='''UPDATE Patrocinadores SET Nombre_pa='{}', Fecha_Inicio_pa='{}', Fecha_Final_pa='{}',
    Dinero_Anual_pa='{}' WHERE ID={}'''.format(Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa, ID)
    futbol.execute(modificarPatrocinadores)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Trofeos(ID, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr):
    futbol = mydb.cursor()
    modificarTrofeos='''UPDATE Trofeos SET Nombre_tr='{}', Tipo_tr='{}', Fecha_Inicio_tr='{}', Fecha_Final_tr='{}',
    G_Anterior_tr='{}' WHERE ID={}'''.format(Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr, ID)
    futbol.execute(modificarTrofeos)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Entrenadores(ID, Nombre_en, PJ_en, Rojas_en, Amarillas_en):
    futbol = mydb.cursor()
    modificarEntrenadores='''UPDATE Entrenadores SET Nombre_en='{}', PJ_en='{}', Rojas_en='{}',
    Amarillas_en='{}' WHERE ID={}'''.format(Nombre_en, PJ_en,Rojas_en, Amarillas_en, ID)
    futbol.execute(modificarEntrenadores)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def modifica_Presidentes(ID, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr):
    futbol = mydb.cursor()
    modificarPresidentes='''UPDATE Presidentes SET Nombre_pr='{}', Fecha_Inicio_pr='{}', Fecha_Final_pr='{}',
    Dinero_Anual_pr='{}' WHERE ID={}'''.format(Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr, ID)
    futbol.execute(modificarPresidentes)
    n=futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

#####################    CREAR TABLA     ############################

def crear_TablaEquipos():
    futbol = mydb.cursor()
    crearTabla= '''CREATE TABLE IF NOT EXISTS Equipos 
    (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Liga_eq INT NOT NULL, Nombre_eq VARCHAR(50) NOT NULL, PJ_eq INT(7) NOT NULL, Victorias_eq INT(5) NOT NULL, Derrotas_eq INT(5) NOT NULL, 
    Empates_eq INT(5) NOT NULL, GF_eq INT(5) NOT NULL, GC_eq INT(5) NOT NULL, Puntos_eq INT(7) NOT NULL, 
    FOREIGN KEY (ID_Liga_eq) REFERENCES Liga (ID))'''
    futbol.execute(crearTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def crear_TablaJugadores():
    futbol = mydb.cursor()
    crearTabla= '''CREATE TABLE IF NOT EXISTS Jugadores 
    (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Liga_ju INT NOT NULL, ID_Equipos_ju INT NOT NULL, Nombre_ju VARCHAR(50) NOT NULL, PJ_ju INT(5) NOT NULL, Goles_ju INT(4) NOT NULL, 
    Asistencias_ju INT(4) NOT NULL, Rojas_ju INT(3) NOT NULL, Amarillas_ju INT(3) NOT NULL, 
    FOREIGN KEY (ID_Liga_ju) REFERENCES Liga(ID), FOREIGN KEY (ID_Equipos_ju) REFERENCES Equipos (ID))'''
    futbol.execute(crearTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def crear_TablaLiga():
    futbol = mydb.cursor()
    crearTabla= '''CREATE TABLE IF NOT EXISTS Liga 
    (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Nombre_li VARCHAR(50) NOT NULL, País_li VARCHAR(50) NOT NULL, N_Edición_li INT(4) NOT NULL, N_Jornada_li INT(2) NOT NULL)'''
    futbol.execute(crearTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def crear_TablaPatrocinadores():
    futbol = mydb.cursor()
    crearTabla= '''CREATE TABLE IF NOT EXISTS Patrocinadores 
    (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Equipos_pa INT NOT NULL, Nombre_pa VARCHAR(50) NOT NULL, Fecha_Inicio_pa YEAR NULL, Fecha_Final_pa YEAR NULL, Dinero_Anual_pa INT(15) NOT NULL, 
    FOREIGN KEY (ID_Equipos_pa) REFERENCES Equipos (ID))'''
    futbol.execute(crearTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def crear_TablaTrofeos():
    futbol = mydb.cursor()
    crearTabla= '''CREATE TABLE IF NOT EXISTS Trofeos 
    (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Equipos_tr INT NOT NULL, Nombre_tr VARCHAR(50) NOT NULL, Tipo_tr VARCHAR(50) NOT NULL, Fecha_Inicio_tr YEAR NULL, Fecha_Final_tr YEAR NULL, G_Anterior_tr VARCHAR(50) NULL, 
    FOREIGN KEY (ID_Equipos_tr) REFERENCES Equipos (ID))'''
    futbol.execute(crearTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def crear_TablaEntrenadores():
    futbol = mydb.cursor()
    crearTabla= '''CREATE TABLE IF NOT EXISTS Entrenadores 
    (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Liga_en INT NOT NULL, ID_Equipos_en INT NOT NULL, Nombre_en VARCHAR(50) NOT NULL, Rojas_en INT(3) NOT NULL, Amarillas_en INT(3) NOT NULL, 
    FOREIGN KEY (ID_Liga_en) REFERENCES Liga (ID), FOREIGN KEY (ID_Equipos_en) REFERENCES Equipos (ID))'''
    futbol.execute(crearTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

def crear_TablaPresidentes():
    futbol = mydb.cursor()
    crearTabla= '''CREATE TABLE IF NOT EXISTS Presidentes 
    (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Equipos_pr INT NOT NULL, Nombre_pr VARCHAR(50) NOT NULL, Fecha_Inicio_pr YEAR NULL, Fecha_Final_pr YEAR NULL, Dinero_Anual_pr INT(15) NOT NULL, 
    FOREIGN KEY (ID_Equipos_pr) REFERENCES Equipos (ID))'''
    futbol.execute(crearTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

####################    ELIMINAR TABLA    ########################

def eliminar_Tabla(tabla):
    futbol = mydb.cursor()
    borrarTabla= "DROP TABLE {}".format(tabla)
    futbol.execute(borrarTabla)
    n = futbol.rowcount
    mydb.commit()
    futbol.close()
    return n

# ####################         MENUS         #######################


menuAdmin='''\n
        MENU ADMIN

*  1) Ver tablas           *
*  2) Consultar tabla      *
*  3) Insertar dato        *
*  4) Borrar dato          *
*  5) Modificar dato       *
*  6) Crear Tabla          *
*  7) Eliminar Tabla       *
*  8) Usuarios             *
*  9) Salir                *
'''

menusubAdmin='''\n
        MENU ADMIN

*  1) Ver Usuarios        *
*  2) Borrar Usuario      *
*  3) Modificar Usuario   *
*  4) Crear Usuario       *
*  5) Borrar Rol          *
*  6) Modificar Rol       *
*  7) Crear Rol           *
*  9) Salir               *
'''

menuEditor='''\n
        MENU EDITOR

*  1) Ver tablas           *
*  2) Consultar tabla      *
*  3) Insertar dato        *
*  4) Borrar dato          *
*  5) Modificar dato       *
*  6) Crear Tabla          *
*  7) Eliminar Tabla       *
*  9) Salir                *
'''

menuLector='''\n
        MENU Lector

*  1) Ver tablas           *
*  2) Consultar tabla      *
*  3) Insertar dato        *
*  4) Borrar dato          *
*  5) Modificar dato       *
*  9) Salir                *
'''

menuDesarrollador='''\n
     MENU Desarrollador

*  1) Ver tablas           *
*  2) Consultar tabla      *
*  3) Crear Tabla          *
*  4) Eliminar Tabla       *
*  9) Salir                *
'''

menuTabla='''\n
        MENU TABLAS

*  1) Equipo              *
*  2) Jugadores           *
*  3) Liga                *
*  4) Trofeo              *
*  5) Patrocinador        *
*  6) Entrenadores        *
*  7) Presidentes         *
'''

################         USUARIOS / ROLES / PERMISOS         ###################

listaUsuarios = []
r = False
conectado = r
tiposRoles = ["lector","editor","admin"]

def conectar():
    intentos = 5 
    passwordIngresada= input("Ingrese contraseña: ").lower()
    if passwordIngresada == passwordLista:
        print("\n-> Contraseña correcta")
        conectado = True
        return conectado
    else:
        intentos -= 1
        if intentos > 0:
            print("\n-> Incorrecto, vuelva a escribirla")
            print("Te quedan ",intentos, " intentos (º.º)\n")
            conectar()
        else:
            print("-> Has superado el limite de intentos\n")
            iniciarSesion()
            registrarUsuario()
    

def iniciarSesion():
    print("\n¿Que usuario desea usar?")
    for elemento in listaUsuarios:
        print ("\nUsuario: {}\nContraseña: {}\nRol: {}".format(elemento["usuario"], elemento["password"], elemento["rol"]))
    n = input("\nIngrese usuario para iniciar sesión: ").lower()
    for elemento in listaUsuarios:
        global nombreLista
        nombreLista = elemento["usuario"]
        global passwordLista
        passwordLista = elemento["password"]
        if n == nombreLista: 
            conectar()
            break
    else:
        print("\nNo hay usuarios, vamos a ver si te registras")
        registrarUsuario()

def registrarUsuario():
    while True:
        # Solicita el nombre de usuario, contraseña y rol
        global nombresUsuario 
        nombresUsuario = input("\nIngrese el nombre de usuario: ")
        global passwordsUsuario
        passwordsUsuario = input("Ingrese la contraseña: ")
        global rol
        rol = input("Ingrese el rol (lector, editor o admin): ")
        if rol not in ["lector", "editor", "admin"]:
            print("\nRol inválido, ingresa todo de nuevo y fijate bien (º.º)")
            continue
        
        # Crea un usuario
        perfil= {
            "usuario": nombresUsuario,
            "password": passwordsUsuario,
            "rol": rol
        }
        
        listaUsuarios.append(perfil)
        
        # Pregunta al usuario si desea agregar otro usuario
        p = input("\n¿Desea agregar otro usuario? (s/n): ")
        if p.lower() != "s":
            break
        
    print("\nSe ha registrado el usuario")

def trampa():
    print("\nPon el usuario y contraseña anteriro:")
    n = input("\nIngrese usuario para iniciar sesión: ").lower()
    p = input("\nIngrese contraseña para iniciar sesión: ").lower()
    print("Ya no te acuerdas verdad (º.º)")
    return n, p
    


###################       APP       #######################

def main():
    
    while (True):
        s = input("\nSi quieres iniciar sesión (1) / Si quieres registrarte pulsa (2)\n")
        if s== "1":
            iniciarSesion()
            break
        elif s== "2":
            registrarUsuario()      
  
    ######################################       ADMIN      ##################################################

    for roles in listaUsuarios:
        if roles["rol"] == "admin":
            opcion='0'
            while opcion != "9": 
                print(menuAdmin)
                opcion = input("\n¿Que opción deseas realizar?\n")

                #####  Ver tablas  #####
                if opcion == '1':
                    ver_tablas()

                #####  Consultar tablas  #####
                elif opcion == '2':
                    while (True):
                        try:
                            ver_tablas()
                            tabla = input("\nNombre de la tabla: \n")
                            consulta_tabla(tabla)
                            break
                        except:
                            print("\n-> No existe esa tabla, lo habrás escrito mal, fíjate en el nombre de arriba (º.º), inténtalo otra vez...\n")

                #####  Insertar datos  #####
                elif opcion == '3':   
                    ver_tablas()
                    subopcionInsertar = input("\n¿En que tabla deseas insertar los datos? Pon el nombre o pon x para volver al menu principal\n").lower()
                    if subopcionInsertar == 'equipos':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Equipos\n")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        print("\nInsertar datos Equipos")
                        tabla = input("\nPon Liga para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Liga_eq = input("\nEl ID de la liga, que es el segundo numero empezando por la izquierda: \n")
                                Nombre_eq = input("Nombre del equipo: \n")
                                PJ_eq = input("Numero de partidos jugados: \n")
                                Victorias_eq = input("Victorias: \n")
                                Derrotas_eq = input("Derrotas: \n")
                                Empates_eq = input("Empates: \n")
                                GF_eq = input("Goles a favor: \n")
                                GC_eq = input("Goles en contra: \n")
                                Puntos_eq = input("Puntos en la liga: \n")
                                r =insertar_Equipos(Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")

                    elif subopcionInsertar == 'jugadores':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Jugadores")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Liga para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Liga_ju = input("El ID de la liga: \n")
                                Id_Equipos_ju = input("El ID del equipo: \n")
                                Nombre_ju = input("Nombre del jugador: ")
                                PJ_ju = input("Partidos jugados: ")
                                Goles_ju = input("Goles metidos: ")
                                Asistencias_ju = input("Asistencias dadas: ")
                                Rojas_ju = input("Tarjetas rojas: ")
                                Amarillas_ju = input("Tarjetas amarillas: ")
                                r = insertar_Jugadores(Id_Liga_ju, Id_Equipos_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionInsertar == 'liga':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Liga\n")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Nombre_li = input("Nombre de la la liga: \n")
                                País_li = input("País donde se juega: \n")
                                N_Edición_li = input("Numero actual de temporada desde que se fundo: \n")
                                N_Jornada_li = input("Numero de partido del año: \n")
                                r = insertar_Liga(Nombre_li, País_li, N_Edición_li, N_Jornada_li)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n") 
                    elif subopcionInsertar == 'patrocinadores':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Patrocinadores")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Equipos_pa = input("El ID del equipo que patrocina: \n")
                                Nombre_pa = input("Nombre del patrocinador: \n")
                                Fecha_Inicio_pa = input("Año en el que comenzó el patrocinio: \n")
                                Fecha_Final_pa = input("Año del final del patrocinio: \n")
                                Dinero_Anual_pa = input("Dinero aportado: \n")
                                r = insertar_Patrocinadores(Id_Equipos_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")                
                    elif subopcionInsertar == 'trofeos':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Trofeos")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Equipos_tr = input("El ID del equipo: \n")
                                Nombre_tr = input("Nombre del trofeo: \n")
                                Tipo_tr = input("Es nacional o internacional: \n")
                                Fecha_Inicio_tr = input("Año de inicio del torneo: \n")
                                Fecha_Final_tr = input("Año del final del torneo: \n")
                                G_Anterior_tr = input("Ganador anterior del torneo: \n")
                                r = insertar_Trofeos(Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionInsertar == 'entrenadores':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Entrenadores")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Liga para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Liga_en = input("El ID de la liga: \n")
                                Id_Equipos_en = input("El ID del equipo: \n")
                                Nombre_en = input("Nombre del jugador: ")
                                PJ_en = input("Partidos jugados: ")
                                Rojas_en = input("Tarjetas rojas: ")
                                Amarillas_en = input("Tarjetas amarillas: ")
                                r = insertar_Entrenadores(Id_Liga_en, Id_Equipos_en, Nombre_en, PJ_en, Rojas_en, Amarillas_en)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionInsertar == 'presidentes':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Presidentess")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Equipos_pr = input("El ID del equipo que patrocina: \n")
                                Nombre_pr = input("Nombre del patrocinador: \n")
                                Fecha_Inicio_pr = input("Año en el que comenzó el patrocinio: \n")
                                Fecha_Final_pr = input("Año del final del patrocinio: \n")
                                Dinero_Anual_pr = input("Dinero aportado: \n")
                                r = insertar_Presidentes(Id_Equipos_pr, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n") 
                    elif subopcionInsertar == 'x':
                        print("\nVolver al menu")
                        print(menuAdmin)
                        opcion = input("\n¿Que opción deseas?")
                    else:
                        ver_tablas()
                        subopcionInsertar = input("\n¿En que tabla deseas insertar los datos? Pon el nombre o pon x para volver al menu principal\n").lower()           
                    
                #####  Borrar datos  #####
                elif opcion == '4':
                    print("\nTabla de los datos que desea eliminar")
                    ver_tablas()
                    tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                    consulta_tabla(tabla)
                    numId = int(input("\nIntroduce el numero del id, siendo el primer número que aparece por la izquierda: \n"))
                    r = borrar_DatoTabla(tabla,numId)
                    if(r==0):
                        print("\n-> No existe")
                    else:
                        print("\n-> Se eliminó correctamente")

                #####  Modificar datos  #####
                elif opcion == '5':
                    ver_tablas()
                    subopcionModificar = input("\n¿En que tabla deseas modificar los datos? Pon el nombre o pon x para volver al menu principal\n").lower()         
                    if subopcionModificar == 'equipo':
                        print("\nModificar Equipos")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Equipos_eq = int(input("\nIntroduce el Id del equipo que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Equipos(Id_Equipos_eq)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_eq = input("Introduce el nuevo nombre del equipo: ")
                                    PJ_eq = input("Introduce el nuevo numero partidos jugados: ")
                                    Victorias_eq = input("Introduce el nuevo numero de victorias: ")
                                    Derrotas_eq = input("Introduce el nuevo numero de derrotas: ")
                                    Empates_eq = input("Introduce el nuevo numero de empates: ")
                                    GF_eq = input("Introduce el nuevo numero de goles a favor: ")
                                    GC_eq = input("Introduce el nuevo numero de goles en contra: ")
                                    Puntos_eq = input("Introduce el nuevo numero de puntos: ")
                                    r = modifica_Equipos(Id_Equipos_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'jugadores':
                        print("\nModificar Jugadores")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Jugadores_ju = int(input("\nIntroduce el Id del jugador que desea modificar, que es el primer número empezando por la izquierda:\n "))
                        p = buscar_Jugadores(Id_Jugadores_ju)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_ju = input("Introduce el nuevo nombre del jugador: ")
                                    PJ_ju = input("Introduce el nuevo numero de partidos jugados: ")
                                    Goles_ju = input("Introduce el nuevo numero de golres que ha marcado: ")
                                    Asistencias_ju = input("Introduce el nuevo numero de asistencias que ha dado: ")
                                    Rojas_ju = input("Introduce el nuevo numero de tarjetas rojas: ")
                                    Amarillas_ju = input("Introduce el nuevo numero de tarjetas amarillas: ")
                                    r = modifica_Jugadores(Id_Jugadores_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'liga':
                        print("\nModificar Liga")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Liga_li = int(input("\nIntroduce el Id de la liga que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Liga(Id_Liga_li)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_li = input("Introduce el nuevo nombre de la liga: ")
                                    País_li = input("Introduce el nuevo país donde se juega: ")
                                    N_Edición_li = input("Introduce el nuevo numero de temporada en que se fundo: ")
                                    N_Jornada_li = input("Introduce el nuevo numero de partido del año: ")
                                    r = modifica_Liga(Id_Liga_li, Nombre_li, País_li, N_Edición_li, N_Jornada_li)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'patrocinadores':
                        print("\nModificar Patrocinadores")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Patrocinadores_pa = int(input("\nIntroduce el Id de patrocinador que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Patrocinadores(Id_Patrocinadores_pa)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_pa = input("Introduce el nombre de la liga: ")
                                    Fecha_Inicio_pa = input("Introduce el año de inicio: ")
                                    Fecha_Final_pa = input("Introduce el año que termina: ")
                                    Dinero_Anual_pa = input("Introduce el dinero ofrecido: ")
                                    r = modifica_Patrocinadores(Id_Patrocinadores_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'trofeos':
                        print("\nModificar Trofeos")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Trofeos_tr = int(input("\nIntroduce el Id de trofeo que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Trofeos(Id_Trofeos_tr)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_tr = input("Introduce el nuevo nombre del trofeo: ")
                                    Tipo_tr = input("Introduce si es nacional o internacional: ")
                                    Fecha_Inicio_tr = input("Introduce el año de inicio: ")
                                    Fecha_Final_tr = input("Introduce el año que termina: ")
                                    G_Anterior_tr = input("Introduce el ganador anterior: ")
                                    r = modifica_Trofeos(Id_Trofeos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'entrenadores':
                        print("\nModificar Entrenadores")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Entrenadores_en = int(input("\nIntroduce el Id del entrenador que desea modificar, que es el primer número empezando por la izquierda:\n "))
                        p = buscar_Entrenadores(Id_Entrenadores_en)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_en = input("Introduce el nuevo nombre del entrenador: ")
                                    PJ_en = input("Introduce el nuevo numero de partidos: ")
                                    Rojas_en = input("Introduce el nuevo numero de tarjetas rojas: ")
                                    Amarillas_en = input("Introduce el nuevo numero de tarjetas amarillas: ")
                                    r = modifica_Entrenadores(Id_Entrenadores_en, Nombre_en, PJ_en, Rojas_en, Amarillas_en)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'presidentes':
                        print("\nModificar Presidentes")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Presidentes_pr = int(input("\nIntroduce el Id de presidente que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Presidentes(Id_Presidentes_pr)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_pr = input("Introduce el nombre del presidente ")
                                    Fecha_Inicio_pr = input("Introduce el año de inicio: ")
                                    Fecha_Final_pr = input("Introduce el año que termina: ")
                                    Dinero_Anual_pr = input("Introduce el dinero ofrecido: ")
                                    r = modifica_Presidentes(Id_Presidentes_pr, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n") 
                    elif subopcionModificar == 'x':
                        print("\nVolver al menu")
                        print(menuAdmin)
                        opcion = input("\n¿Que opción deseas?")
                    else:
                        ver_tablas()
                        subopcionModificar = input("\n¿En que tabla deseas modificar los datos? Pon el nombre o pon x para volver al menu principal\n").lower() 

                ######  Crear tabla  ######
                elif opcion == '6':
                    ver_tablas()
                    print("\nEstas son las tablas que se pueden crear\n")   
                    print(menuTabla)
                    while (True):
                        try:
                            subopcionCrear = input("\n¿Que tabla quieres crear? Pon el nombre\n").lower()
                            if subopcionCrear == 'equipos':
                                crear_TablaEquipos() 
                            elif subopcionCrear == 'jugadores':
                                crear_TablaJugadores() 
                            elif subopcionCrear == 'liga':
                                crear_TablaLiga() 
                            elif subopcionCrear == 'patrocinadores':
                                crear_TablaPatrocinadores()      
                            elif subopcionCrear == 'trofeos':
                                crear_TablaTrofeos()
                            elif subopcionCrear == 'entrenadores':
                                crear_TablaEntrenadores()
                            elif subopcionCrear == 'presidentes':
                                crear_TablaPresidentes()        
                            elif subopcionCrear == 'x':
                                print("\nVolver al menu")
                                print(menuAdmin)
                                opcion = input("\n¿Que opción deseas?")

                            break
                        except:
                            print("\nTe has confundido en el nombre ...")

                ######  Eliminar tabla  ######
                elif opcion == '7':
                    print("\n¿Que tabla quieres borrar?")
                    ver_tablas()
                    tabla = input("\nEscribe el nombre de la tabla:")
                    eliminar_Tabla(tabla)
                    print("\n->Se eliminó correctamente")
                
                ######  Usuarios  ######
                elif opcion == '8':  
                    print(menusubAdmin)
                    subopcionUsuarios = input("\n¿Que quieres hacer con que usuario)\n").lower()
                    if subopcionUsuarios == '1':
                        for elemento in listaUsuarios:
                            print ("\nUsuario: {}\nRol: {}".format(elemento["usuario"], elemento["rol"]))       
                    if subopcionUsuarios == '2':
                        for elemento in listaUsuarios:
                            print ("\nUsuario: {}".format(elemento["usuario"]))
                        p = input("\n¿Que usuario deseas borrar? pon el nombre: ")
                        for usuario in listaUsuarios:   
                            if usuario["usuario"] == p:
                                try:
                                    listaUsuarios.remove(usuario)
                                except ValueError:
                                    print("El valor ingresado no existe en la lista")
                            else:
                                subopcionUsuarios    
                    elif subopcionUsuarios == '3':
                        for elemento in listaUsuarios:
                            print ("\nUsuario: {}\nRol: {}".format(elemento["usuario"], elemento["rol"]))  
                        p = input("\n¿Que usuario deseas modificar? pon el nombre: ") 
                        for usuario in listaUsuarios:
                            if usuario['usuario'] == p:
                                while True:
                                    nuevoUsuario = input("Ingrese el nuevo nombre: ")
                                    nuevaContraseña = input("Ingrese la nueva contraseña: ")
                                    print("\nRoles actuales:")
                                    for rol in tiposRoles:
                                        print("Rol de: {}".format(rol))
                                    nuevoRol = input("Ingrese el nuevo rol: ")

                                    usuario['usuario'] = nuevoUsuario
                                    usuario['password'] = nuevaContraseña
                                    usuario['rol'] = nuevoRol
                                    if nuevoRol not in ["lector", "editor", "admin", "desarrollador"]:
                                        print("\nRol inválido, ingresa todo de nuevo y fijate bien (º.º)")
                                        continue
                                    break
                            else:
                                subopcionUsuarios
                    elif subopcionUsuarios == '4':             
                        print("\nQue usuario deseas crear: \n")
                        while True:
                            nombresUsuario = input("Ingrese el nombre de usuario: ")
                            passwordsUsuario = input("Ingrese la contraseña: ")
                            print("\nRoles actuales:")
                            for rol in tiposRoles:
                                print("Rol de: {}".format(rol))
                            rol = input("Ingrese el rol: ")
                            if rol not in ["lector", "editor", "admin", "desarrollador"]:
                                print("\nRol inválido, ingresa todo de nuevo y fijate bien (º.º)")
                                continue
                            perfil= {
                                "usuario": nombresUsuario,
                                "password": passwordsUsuario,
                                "rol": rol
                            }
                            listaUsuarios.append(perfil)
                            break           
                    elif subopcionUsuarios == '5':
                        print("\nEl rol de que usuario deseas eliminar:")
                        for elemento in listaUsuarios:
                            print ("\nUsuario: {}\nRol: {}".format(elemento["usuario"], elemento["rol"]))     
                        nombre = input("\nIngrese el nombre del usuario: ")
                        for usuario in listaUsuarios:
                            if usuario["usuario"] == nombre:
                                del usuario["rol"]
                                print("\nEl rol del usuario {} ha sido eliminado.".format(nombre))
                                break
                        print("\nAgregale otro rol al usuario:")
                        print("\nRoles actuales:")
                        for rol in tiposRoles:
                            print("Rol de: {}".format(rol))
                        rol = input("Ingrese el nuevo rol del usuario: ")
                        if rol not in ["lector", "editor", "admin", "desarrollador"]:
                            print("\nRol inválido, ingresa todo de nuevo y fijate bien (º.º)")
                            continue
                        for usuario in listaUsuarios:
                            if usuario["usuario"] == nombre:
                                usuario["rol"] = rol
                                print("\nEl rol {} ha sido añadido al usuario {}".format(rol,nombre))
                                break
                            else:
                                subopcionUsuarios
                    elif subopcionUsuarios == '6':
                        print("\nA que rol deseas implementar una modificación de reinicio:")
                        print("\nRoles actuales:")
                        for rol in tiposRoles:
                            print("Rol de: {}".format(rol))
                        if rol not in ["lector", "editor", "admin", "desarrollador"]:
                            print("\nRol inválido, ingresa todo de nuevo y fijate bien (º.º)")
                            continue
                        for usuario in listaUsuarios:
                            if usuario['usuario'] == nombreLista:
                                while True:
                                    print("\nEres una pulguilla, ya no entrarás más (º.º)")
                                    trampa()
                            else:
                                subopcionUsuarios
                    elif subopcionUsuarios == '7':
                        print("\nCrea un rol:")
                        print("\nRoles actuales:")
                        for rol in tiposRoles:
                            print("Rol de: {}".format(rol))
                        print("\nLos roles que se pueden crear son: lector, editor, admin, desarrollador") 
                        r = input("\nIngrese el rol: ")
                        tiposRoles.append(r)
                    elif subopcionUsuarios == 'X':
                        print("\nVolver al menu")
                        print(menuAdmin)
                        opcion = input("\n¿Que opción deseas?") 

                #####  Salir  #####
                elif opcion == '9':
                    print("\n-> Saliendo del sistema")
                    main()

                else:
                    print("\n-> Opción no válida")


    ########################################       LECTOR      ###############################################
            
        elif roles["rol"] == "lector":
            opcion='0'
            while opcion != "9":
                print(menuLector)
                opcion = input("\n¿Que opción deseas realizar?\n")

                #####  Ver tablas  #####
                if opcion == '1':
                    ver_tablas()

                #####  Consultar tablas  #####
                elif opcion == '2':
                    while (True):
                        try:
                            ver_tablas()
                            tabla = input("\nNombre de la tabla: \n")
                            consulta_tabla(tabla)
                            break
                        except:
                            print("\n-> No existe esa tabla, lo habrás escrito mal, fíjate en el nombre de arriba (º.º), inténtalo otra vez...\n")

                #####  Insertar datos  #####
                elif opcion == '3':   
                    ver_tablas()
                    subopcionInsertar = input("\n¿En que tabla deseas insertar los datos? Pon el nombre o pon x para volver al menu principal\n").lower()
                    if subopcionInsertar == 'equipos':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Equipos\n")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        print("\nInsertar datos Equipos")
                        tabla = input("\nPon Liga para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Liga_eq = input("\nEl ID de la liga, que es el segundo numero empezando por la izquierda: \n")
                                Nombre_eq = input("Nombre del equipo: \n")
                                PJ_eq = input("Numero de partidos jugados: \n")
                                Victorias_eq = input("Victorias: \n")
                                Derrotas_eq = input("Derrotas: \n")
                                Empates_eq = input("Empates: \n")
                                GF_eq = input("Goles a favor: \n")
                                GC_eq = input("Goles en contra: \n")
                                Puntos_eq = input("Puntos en la liga: \n")
                                r =insertar_Equipos(Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")

                    elif subopcionInsertar == 'jugadores':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Jugadores")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Liga para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Liga_ju = input("El ID de la liga: \n")
                                Id_Equipos_ju = input("El ID del equipo: \n")
                                Nombre_ju = input("Nombre del jugador: ")
                                PJ_ju = input("Partidos jugados: ")
                                Goles_ju = input("Goles metidos: ")
                                Asistencias_ju = input("Asistencias dadas: ")
                                Rojas_ju = input("Tarjetas rojas: ")
                                Amarillas_ju = input("Tarjetas amarillas: ")
                                r = insertar_Jugadores(Id_Liga_ju, Id_Equipos_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionInsertar == 'liga':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Liga\n")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Nombre_li = input("Nombre de la la liga: \n")
                                País_li = input("País donde se juega: \n")
                                N_Edición_li = input("Numero actual de temporada desde que se fundo: \n")
                                N_Jornada_li = input("Numero de partido del año: \n")
                                r = insertar_Liga(Nombre_li, País_li, N_Edición_li, N_Jornada_li)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n") 
                    elif subopcionInsertar == 'patrocinadores':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Patrocinadores")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Equipos_pa = input("El ID del equipo que patrocina: \n")
                                Nombre_pa = input("Nombre del patrocinador: \n")
                                Fecha_Inicio_pa = input("Año en el que comenzó el patrocinio: \n")
                                Fecha_Final_pa = input("Año del final del patrocinio: \n")
                                Dinero_Anual_pa = input("Dinero aportado: \n")
                                r = insertar_Patrocinadores(Id_Equipos_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")                
                    elif subopcionInsertar == 'trofeos':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Trofeos")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Equipos_tr = input("El ID del equipo: \n")
                                Nombre_tr = input("Nombre del trofeo: \n")
                                Tipo_tr = input("Es nacional o internacional: \n")
                                Fecha_Inicio_tr = input("Año de inicio del torneo: \n")
                                Fecha_Final_tr = input("Año del final del torneo: \n")
                                G_Anterior_tr = input("Ganador anterior del torneo: \n")
                                r = insertar_Trofeos(Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionInsertar == 'entrenadores':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Entrenadores")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Liga para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Liga_en = input("El ID de la liga: \n")
                                Id_Equipos_en = input("El ID del equipo: \n")
                                Nombre_en = input("Nombre del jugador: ")
                                PJ_en = input("Partidos jugados: ")
                                Rojas_en = input("Tarjetas rojas: ")
                                Amarillas_en = input("Tarjetas amarillas: ")
                                r = insertar_Entrenadores(Id_Liga_en, Id_Equipos_en, Nombre_en, PJ_en, Rojas_en, Amarillas_en)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionInsertar == 'presidentes':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Presidentess")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Equipos_pr = input("El ID del equipo que patrocina: \n")
                                Nombre_pr = input("Nombre del patrocinador: \n")
                                Fecha_Inicio_pr = input("Año en el que comenzó el patrocinio: \n")
                                Fecha_Final_pr = input("Año del final del patrocinio: \n")
                                Dinero_Anual_pr = input("Dinero aportado: \n")
                                r = insertar_Presidentes(Id_Equipos_pr, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n") 
                    elif subopcionInsertar == 'x':
                        print("\nVolver al menu")
                        print(menuLector)
                        opcion = input("\n¿Que opción deseas?")
                    else:
                        ver_tablas()
                        subopcionInsertar = input("\n¿En que tabla deseas insertar los datos? Pon el nombre o pon x para volver al menu principal\n").lower()           
                    
                #####  Borrar datos  #####
                elif opcion == '4':
                    print("\nTabla de los datos que desea eliminar")
                    ver_tablas()
                    tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                    consulta_tabla(tabla)
                    numId = int(input("\nIntroduce el numero del id, siendo el primer número que aparece por la izquierda: \n"))
                    r = borrar_DatoTabla(tabla,numId)
                    if(r==0):
                        print("\n-> No existe")
                    else:
                        print("\n-> Se eliminó correctamente")

                #####  Modificar datos  #####
                elif opcion == '5':
                    ver_tablas()
                    subopcionModificar = input("\n¿En que tabla deseas modificar los datos? Pon el nombre o pon x para volver al menu principal\n").lower()         
                    if subopcionModificar == 'equipos':
                        print("\nModificar Equipos")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Equipos_eq = int(input("\nIntroduce el Id del equipo que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Equipos(Id_Equipos_eq)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_eq = input("Introduce el nuevo nombre del equipo: ")
                                    PJ_eq = input("Introduce el nuevo numero partidos jugados: ")
                                    Victorias_eq = input("Introduce el nuevo numero de victorias: ")
                                    Derrotas_eq = input("Introduce el nuevo numero de derrotas: ")
                                    Empates_eq = input("Introduce el nuevo numero de empates: ")
                                    GF_eq = input("Introduce el nuevo numero de goles a favor: ")
                                    GC_eq = input("Introduce el nuevo numero de goles en contra: ")
                                    Puntos_eq = input("Introduce el nuevo numero de puntos: ")
                                    r = modifica_Equipos(Id_Equipos_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'jugadores':
                        print("\nModificar Jugadores")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Jugadores_ju = int(input("\nIntroduce el Id del jugador que desea modificar, que es el primer número empezando por la izquierda:\n "))
                        p = buscar_Jugadores(Id_Jugadores_ju)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_ju = input("Introduce el nuevo nombre del jugador: ")
                                    PJ_ju = input("Introduce el nuevo numero de partidos jugados: ")
                                    Goles_ju = input("Introduce el nuevo numero de golres que ha marcado: ")
                                    Asistencias_ju = input("Introduce el nuevo numero de asistencias que ha dado: ")
                                    Rojas_ju = input("Introduce el nuevo numero de tarjetas rojas: ")
                                    Amarillas_ju = input("Introduce el nuevo numero de tarjetas amarillas: ")
                                    r = modifica_Jugadores(Id_Jugadores_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'liga':
                        print("\nModificar Liga")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Liga_li = int(input("\nIntroduce el Id de la liga que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Liga(Id_Liga_li)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_li = input("Introduce el nuevo nombre de la liga: ")
                                    País_li = input("Introduce el nuevo país donde se juega: ")
                                    N_Edición_li = input("Introduce el nuevo numero de temporada en que se fundo: ")
                                    N_Jornada_li = input("Introduce el nuevo numero de partido del año: ")
                                    r = modifica_Liga(Id_Liga_li, Nombre_li, País_li, N_Edición_li, N_Jornada_li)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'patrocinadores':
                        print("\nModificar Patrocinadores")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Patrocinadores_pa = int(input("\nIntroduce el Id de patrocinador que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Patrocinadores(Id_Patrocinadores_pa)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_pa = input("Introduce el nombre de la liga: ")
                                    Fecha_Inicio_pa = input("Introduce el año de inicio: ")
                                    Fecha_Final_pa = input("Introduce el año que termina: ")
                                    Dinero_Anual_pa = input("Introduce el dinero ofrecido: ")
                                    r = modifica_Patrocinadores(Id_Patrocinadores_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'trofeos':
                        print("\nModificar Trofeos")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Trofeos_tr = int(input("\nIntroduce el Id de trofeo que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Trofeos(Id_Trofeos_tr)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_tr = input("Introduce el nuevo nombre del trofeo: ")
                                    Tipo_tr = input("Introduce si es nacional o internacional: ")
                                    Fecha_Inicio_tr = input("Introduce el año de inicio: ")
                                    Fecha_Final_tr = input("Introduce el año que termina: ")
                                    G_Anterior_tr = input("Introduce el ganador anterior: ")
                                    r = modifica_Trofeos(Id_Trofeos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'entrenadores':
                        print("\nModificar Entrenadores")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Entrenadores_en = int(input("\nIntroduce el Id del entrenador que desea modificar, que es el primer número empezando por la izquierda:\n "))
                        p = buscar_Entrenadores(Id_Entrenadores_en)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_en = input("Introduce el nuevo nombre del entrenador: ")
                                    PJ_en = input("Introduce el nuevo numero de partidos: ")
                                    Rojas_en = input("Introduce el nuevo numero de tarjetas rojas: ")
                                    Amarillas_en = input("Introduce el nuevo numero de tarjetas amarillas: ")
                                    r = modifica_Entrenadores(Id_Entrenadores_en, Nombre_en, PJ_en, Rojas_en, Amarillas_en)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'presidentes':
                        print("\nModificar Presidentes")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Presidentes_pr = int(input("\nIntroduce el Id de presidente que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Presidentes(Id_Presidentes_pr)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_pr = input("Introduce el nombre del presidente ")
                                    Fecha_Inicio_pr = input("Introduce el año de inicio: ")
                                    Fecha_Final_pr = input("Introduce el año que termina: ")
                                    Dinero_Anual_pr = input("Introduce el dinero ofrecido: ")
                                    r = modifica_Presidentes(Id_Presidentes_pr, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n") 
                    elif subopcionModificar == 'x':
                        print("\nVolver al menu")
                        print(menuLector)
                        opcion = input("\n¿Que opción deseas?")
                    else:
                        ver_tablas()
                        subopcionModificar = input("\n¿En que tabla deseas modificar los datos? Pon el nombre o pon x para volver al menu principal\n").lower()  

                #####  Salir  #####
                elif opcion == '9':
                    print("\n-> Saliendo del sistema")
                    main()

                else:
                    print("\n-> Opción no válida")
                    


    ########################################       EDITOR      ###############################################

        elif roles["rol"] == "editor":
            opcion='0'
            while opcion != "9":
                print(menuEditor)
                opcion = input("\n¿Que opción deseas realizar?\n")

                #####  Ver tablas  #####
                if opcion == '1':
                    ver_tablas()

                #####  Consultar tablas  #####
                elif opcion == '2':
                    while (True):
                        try:
                            ver_tablas()
                            tabla = input("\nNombre de la tabla: \n")
                            consulta_tabla(tabla)
                            break
                        except:
                            print("\n-> No existe esa tabla, lo habrás escrito mal, fíjate en el nombre de arriba (º.º), inténtalo otra vez...\n")

                #####  Insertar datos  #####
                elif opcion == '3':   
                    ver_tablas()
                    subopcionInsertar = input("\n¿En que tabla deseas insertar los datos? Pon el nombre o pon x para volver al menu principal\n").lower()
                    if subopcionInsertar == 'equipos':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Equipos\n")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        print("\nInsertar datos Equipos")
                        tabla = input("\nPon Liga para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Liga_eq = input("\nEl ID de la liga, que es el segundo numero empezando por la izquierda: \n")
                                Nombre_eq = input("Nombre del equipo: \n")
                                PJ_eq = input("Numero de partidos jugados: \n")
                                Victorias_eq = input("Victorias: \n")
                                Derrotas_eq = input("Derrotas: \n")
                                Empates_eq = input("Empates: \n")
                                GF_eq = input("Goles a favor: \n")
                                GC_eq = input("Goles en contra: \n")
                                Puntos_eq = input("Puntos en la liga: \n")
                                r =insertar_Equipos(Id_Liga_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")

                    elif subopcionInsertar == 'jugadores':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Jugadores")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Liga para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Liga_ju = input("El ID de la liga: \n")
                                Id_Equipos_ju = input("El ID del equipo: \n")
                                Nombre_ju = input("Nombre del jugador: ")
                                PJ_ju = input("Partidos jugados: ")
                                Goles_ju = input("Goles metidos: ")
                                Asistencias_ju = input("Asistencias dadas: ")
                                Rojas_ju = input("Tarjetas rojas: ")
                                Amarillas_ju = input("Tarjetas amarillas: ")
                                r = insertar_Jugadores(Id_Liga_ju, Id_Equipos_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionInsertar == 'liga':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Liga\n")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Nombre_li = input("Nombre de la liga: \n")
                                País_li = input("País donde se juega: \n")
                                N_Edición_li = input("Numero actual de temporada desde que se fundo: \n")
                                N_Jornada_li = input("Numero de partido del año: \n")
                                r = insertar_Liga(Nombre_li, País_li, N_Edición_li, N_Jornada_li)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n") 
                    elif subopcionInsertar == 'patrocinadores':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Patrocinadores")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> insertar: ")
                                Id_Equipos_pa = input("El ID del equipo que patrocina: \n")
                                Nombre_pa = input("Nombre del patrocinador: \n")
                                Fecha_Inicio_pa = input("Año en el que comenzó el patrocinio: \n")
                                Fecha_Final_pa = input("Año del final del patrocinio: \n")
                                Dinero_Anual_pa = input("Dinero aportado: \n")
                                r = insertar_Patrocinadores(Id_Equipos_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")                
                    elif subopcionInsertar == 'trofeos':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Trofeos")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Equipos_tr = input("El ID del equipo: \n")
                                Nombre_tr = input("Nombre del trofeo: \n")
                                Tipo_tr = input("Es nacional o internacional: \n")
                                Fecha_Inicio_tr = input("Año de inicio del torneo: \n")
                                Fecha_Final_tr = input("Año del final del torneo: \n")
                                G_Anterior_tr = input("Ganador anterior del torneo: \n")
                                r = insertar_Trofeos(Id_Equipos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionInsertar == 'entrenadores':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Entrenadores")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Liga para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Liga_en = input("El ID de la liga: \n")
                                Id_Equipos_en = input("El ID del equipo: \n")
                                Nombre_en = input("Nombre del jugador: ")
                                PJ_en = input("Partidos jugados: ")
                                Rojas_en = input("Tarjetas rojas: ")
                                Amarillas_en = input("Tarjetas amarillas: ")
                                r = insertar_Entrenadores(Id_Liga_en, Id_Equipos_en, Nombre_en, PJ_en, Rojas_en, Amarillas_en)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionInsertar == 'presidentes':
                        print("\nPara insertar datos vamos a hacer primero una consulta en la tabla Presidentess")
                        tabla = input("Nombre de la tabla: \n")
                        consulta_tabla(tabla)
                        tabla = input("\nPon Equipos para repasar el ID de la tabla: \n")
                        consulta_tabla(tabla)
                        while (True):
                            try:
                                print("\n-> Insertar: ")
                                Id_Equipos_pr = input("El ID del equipo que patrocina: \n")
                                Nombre_pr = input("Nombre del patrocinador: \n")
                                Fecha_Inicio_pr = input("Año en el que comenzó el patrocinio: \n")
                                Fecha_Final_pr = input("Año del final del patrocinio: \n")
                                Dinero_Anual_pr = input("Dinero aportado: \n")
                                r = insertar_Presidentes(Id_Equipos_pr, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr)
                                break
                            except:
                                print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n") 
                    elif subopcionInsertar == 'x':
                        print("\nVolver al menu")
                        print(menuEditor)
                        opcion = input("\n¿Que opción deseas?")
                    else:
                        ver_tablas()
                        subopcionInsertar = input("\n¿En que tabla deseas insertar los datos? Pon el nombre o pon x para volver al menu principal\n").lower()           
                    
                #####  Borrar datos  #####
                elif opcion == '4':
                    print("\nTabla de los datos que desea eliminar")
                    ver_tablas()
                    tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                    consulta_tabla(tabla)
                    numId = int(input("\nIntroduce el numero del id, siendo el primer número que aparece por la izquierda: \n"))
                    r = borrar_DatoTabla(tabla,numId)
                    if(r==0):
                        print("\n-> No existe")
                    else:
                        print("\n-> Se eliminó correctamente")

                #####  Modificar datos  #####
                elif opcion == '5':
                    ver_tablas()
                    subopcionModificar = input("\n¿En que tabla deseas modificar los datos? Pon el indice o pon x para volver al menu principal\n").lower()         
                    if subopcionModificar == 'equipos':
                        print("\nModificar Equipos")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Equipos_eq = int(input("\nIntroduce el Id del equipo que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Equipos(Id_Equipos_eq)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_eq = input("Introduce el nuevo nombre del equipo: ")
                                    PJ_eq = input("Introduce el nuevo numero partidos jugados: ")
                                    Victorias_eq = input("Introduce el nuevo numero de victorias: ")
                                    Derrotas_eq = input("Introduce el nuevo numero de derrotas: ")
                                    Empates_eq = input("Introduce el nuevo numero de empates: ")
                                    GF_eq = input("Introduce el nuevo numero de goles a favor: ")
                                    GC_eq = input("Introduce el nuevo numero de goles en contra: ")
                                    Puntos_eq = input("Introduce el nuevo numero de puntos: ")
                                    r = modifica_Equipos(Id_Equipos_eq, Nombre_eq, PJ_eq, Victorias_eq, Derrotas_eq, Empates_eq, GF_eq, GC_eq, Puntos_eq)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'jugadores':
                        print("\nModificar Jugadores")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Jugadores_ju = int(input("\nIntroduce el Id del jugador que desea modificar, que es el primer número empezando por la izquierda:\n "))
                        p = buscar_Jugadores(Id_Jugadores_ju)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_ju = input("Introduce el nuevo nombre del jugador: ")
                                    PJ_ju = input("Introduce el nuevo numero de partidos jugados: ")
                                    Goles_ju = input("Introduce el nuevo numero de golres que ha marcado: ")
                                    Asistencias_ju = input("Introduce el nuevo numero de asistencias que ha dado: ")
                                    Rojas_ju = input("Introduce el nuevo numero de tarjetas rojas: ")
                                    Amarillas_ju = input("Introduce el nuevo numero de tarjetas amarillas: ")
                                    r = modifica_Jugadores(Id_Jugadores_ju, Nombre_ju, PJ_ju, Goles_ju, Asistencias_ju, Rojas_ju, Amarillas_ju)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'liga':
                        print("\nModificar Liga")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Liga_li = int(input("\nIntroduce el Id de la liga que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Liga(Id_Liga_li)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_li = input("Introduce el nuevo nombre de la liga: ")
                                    País_li = input("Introduce el nuevo país donde se juega: ")
                                    N_Edición_li = input("Introduce el nuevo numero de temporada en que se fundo: ")
                                    N_Jornada_li = input("Introduce el nuevo numero de partido del año: ")
                                    r = modifica_Liga(Id_Liga_li, Nombre_li, País_li, N_Edición_li, N_Jornada_li)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'patrocinadores':
                        print("\nModificar Patrocinadores")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Patrocinadores_pa = int(input("\nIntroduce el Id de patrocinador que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Patrocinadores(Id_Patrocinadores_pa)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_pa = input("Introduce el nombre de la liga: ")
                                    Fecha_Inicio_pa = input("Introduce el año de inicio: ")
                                    Fecha_Final_pa = input("Introduce el año que termina: ")
                                    Dinero_Anual_pa = input("Introduce el dinero ofrecido: ")
                                    r = modifica_Patrocinadores(Id_Patrocinadores_pa, Nombre_pa, Fecha_Inicio_pa, Fecha_Final_pa, Dinero_Anual_pa)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'trofeos':
                        print("\nModificar Trofeos")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Trofeos_tr = int(input("\nIntroduce el Id de trofeo que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Trofeos(Id_Trofeos_tr)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_tr = input("Introduce el nuevo nombre del trofeo: ")
                                    Tipo_tr = input("Introduce si es nacional o internacional: ")
                                    Fecha_Inicio_tr = input("Introduce el año de inicio: ")
                                    Fecha_Final_tr = input("Introduce el año que termina: ")
                                    G_Anterior_tr = input("Introduce el ganador anterior: ")
                                    r = modifica_Trofeos(Id_Trofeos_tr, Nombre_tr, Tipo_tr, Fecha_Inicio_tr, Fecha_Final_tr, G_Anterior_tr)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'entrenadores':
                        print("\nModificar Entrenadores")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Entrenadores_en = int(input("\nIntroduce el Id del entrenador que desea modificar, que es el primer número empezando por la izquierda:\n "))
                        p = buscar_Entrenadores(Id_Entrenadores_en)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_en = input("Introduce el nuevo nombre del entrenador: ")
                                    PJ_en = input("Introduce el nuevo numero de partidos: ")
                                    Rojas_en = input("Introduce el nuevo numero de tarjetas rojas: ")
                                    Amarillas_en = input("Introduce el nuevo numero de tarjetas amarillas: ")
                                    r = modifica_Entrenadores(Id_Entrenadores_en, Nombre_en, PJ_en, Rojas_en, Amarillas_en)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n")
                    elif subopcionModificar == 'presidentes':
                        print("\nModificar Presidentes")
                        tabla = str(input("\nIntroduce el nombre de la tabla: \n"))
                        consulta_tabla(tabla)
                        Id_Presidentes_pr = int(input("\nIntroduce el Id de presidente que desea modificar, que es el primer número empezando por la izquierda: \n"))
                        p = buscar_Presidentes(Id_Presidentes_pr)
                        if p == None:
                            print("\n-> No existe")
                        else:
                            print("\n-> Modificar: ")
                            while (True):
                                try:
                                    Nombre_pr = input("Introduce el nombre del presidente ")
                                    Fecha_Inicio_pr = input("Introduce el año de inicio: ")
                                    Fecha_Final_pr = input("Introduce el año que termina: ")
                                    Dinero_Anual_pr = input("Introduce el dinero ofrecido: ")
                                    r = modifica_Presidentes(Id_Presidentes_pr, Nombre_pr, Fecha_Inicio_pr, Fecha_Final_pr, Dinero_Anual_pr)
                                    break
                                except:
                                    print("\n-> Lo has escrito mal, fíjate BIEN (º.º), inténtalo otra vez...\n") 
                    elif subopcionModificar == 'x':
                        print("\nVolver al menu")
                        print(menuEditor)
                        opcion = input("\n¿Que opción deseas?")
                    else:
                        ver_tablas()
                        subopcionModificar = input("\n¿En que tabla deseas modificar los datos? Pon el indice o pon x para volver al menu principal\n").lower() 

                ######  Crear tabla  ######
                elif opcion == '6':   
                    ver_tablas()
                    print("\nEstas son las tablas que se pueden crear\n")   
                    print(menuTabla)
                    while (True):
                        try:
                            subopcionCrear = input("\n¿Que tabla quieres crear? Pon el nombre\n").lower()
                            if subopcionCrear == 'equipos':
                                crear_TablaEquipos() 
                            elif subopcionCrear == 'jugadores':
                                crear_TablaJugadores() 
                            elif subopcionCrear == 'liga':
                                crear_TablaLiga() 
                            elif subopcionCrear == 'patrocinadores':
                                crear_TablaPatrocinadores()      
                            elif subopcionCrear == 'trofeos':
                                crear_TablaTrofeos()
                            elif subopcionCrear == 'entrenadores':
                                crear_TablaEntrenadores()
                            elif subopcionCrear == 'presidentes':
                                crear_TablaPresidentes()        
                            elif subopcionCrear == 'x':
                                print("\nVolver al menu")
                                print(menuAdmin)
                                opcion = input("\n¿Que opción deseas?")
                            break
                        except:
                            print("\nTe has confundido en el nombre ...")

                ######  Eliminar tabla  ######
                elif opcion == '7':
                    print("\n¿Que tabla quieres borrar?")
                    ver_tablas()
                    tabla = input("\nEscribe el nombre de la tabla:")
                    eliminar_Tabla(tabla)
                    print("\n->Se eliminó correctamente")

                #####  Salir  #####
                elif opcion == '9':
                    print("\n-> Saliendo del sistema")
                    main()

                else:
                    print("\n-> Opción no válida")

    ########################################       DESARROLLADOR      ###############################################

        elif roles["rol"] == "desarrollador":
            opcion='0'
            while opcion != "9":
                print(menuDesarrollador)
                opcion = input("\n¿Que opción deseas realizar?\n")

                #####  Ver tablas  #####
                if opcion == '1':
                    ver_tablas()

                #####  Consultar tablas  #####
                elif opcion == '2':
                    while (True):
                        try:
                            ver_tablas()
                            tabla = input("\nNombre de la tabla: \n")
                            consulta_tabla(tabla)
                            break
                        except:
                            print("\n-> No existe esa tabla, lo habrás escrito mal, fíjate en el nombre de arriba (º.º), inténtalo otra vez...\n")

                ######  Crear tabla  ######
                elif opcion == '3':   
                    ver_tablas()
                    print("\nEstas son las tablas que se pueden crear\n")   
                    print(menuTabla)
                    while (True):
                        try:
                            subopcionCrear = input("\n¿Que tabla quieres crear? Pon el nombre\n").lower()
                            if subopcionCrear == 'equipos':
                                crear_TablaEquipos() 
                            elif subopcionCrear == 'jugadores':
                                crear_TablaJugadores() 
                            elif subopcionCrear == 'liga':
                                crear_TablaLiga() 
                            elif subopcionCrear == 'patrocinadores':
                                crear_TablaPatrocinadores()      
                            elif subopcionCrear == 'trofeos':
                                crear_TablaTrofeos()
                            elif subopcionCrear == 'entrenadores':
                                crear_TablaEntrenadores()
                            elif subopcionCrear == 'presidentes':
                                crear_TablaPresidentes()        
                            elif subopcionCrear == 'x':
                                print("\nVolver al menu")
                                print(menuAdmin)
                                opcion = input("\n¿Que opción deseas?")
                            break
                        except:
                            print("\nTe has confundido en el nombre ...")

                ######  Eliminar tabla  ######
                elif opcion == '4':
                    print("\n¿Que tabla quieres borrar?")
                    ver_tablas()
                    tabla = input("\nEscribe el nombre de la tabla:")
                    eliminar_Tabla(tabla)
                    print("\n->Se eliminó correctamente")

                #####  Salir  #####
                elif opcion == '9':
                    print("\n-> Saliendo del sistema")
                    main()
                else:
                    print("\n-> Opción no válida")


if __name__ == "__main__":
    main()

