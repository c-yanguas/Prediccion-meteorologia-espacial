# Scripts para extraer los datos de Omniweb
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv
import os
import pandas as pd

# Opciones de navegacion (que si muestre la ventana)

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('headless');

driver_path = 'D:\\UNIVERSIDAD\\Cuarto_curso\\Segundo_Cuatrimestre\\Modelos avanzados de bases de datos\\Laboratorio\\Practica1\\Sripts\\Web Scraping\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)

#PROBADOR PARA COMPROBAR COMO SE VAN REALIZANDO LAS ACCIONES
# Inicializar google chrome en la pantalla 2

driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

def obtener_pagina_base():
    # 1-Inicializamos el navegador
    driver.get('https://omniweb.gsfc.nasa.gov/form/omni_min.html')
    # 2-Seleccionamos 5 minutos
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/form/p[1]/input[1]'))) \
        .click()
    # 3-Deseleccionamos 1 minuto
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/form/p[1]/input[2]'))) \
        .click()
    # 4-Seleccionamos Create file
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/form/input[3]'))) \
        .click()
    # 4.1-Deseleccionamos las variables inicialmente marcadas
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/form/p[4]/b/table/tbody/tr[4]/th[1]/table/tbody/tr[1]/td/input'))) \
        .click()
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/form/p[4]/b/table/tbody/tr[6]/th[1]/table/tbody/tr[1]/td/input'))) \
        .click()
    #5.1 Limpiamos el campo de fecha inicio
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/form/p[3]/b/input[1]'))) \
        .clear()
    #6.1 Limpiamos el campo de fecha de fin
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/form/p[3]/b/input[2]'))) \
        .clear()

def obtener_datos(anno, nombre_variable, etiquetas_base, nombre_directorio):
    nombre_fichero = nombre_directorio + "/" + nombre_variable + "_" + str(anno) + ".csv"
    if not(os.path.isfile(nombre_fichero)):
        etiquetas = etiquetas_base + [nombre_variable]
        datos = driver.find_element_by_xpath('/html/body/pre')
        datos = datos.text.split('\n')
        #print(datos)
        nombre_fichero = nombre_directorio+"/"+nombre_variable+"_"+str(anno)+".csv"
        with open(nombre_fichero, 'w', newline='') as fichero:
            escritor = csv.writer(fichero)

            escritor.writerow(etiquetas)
            for fila in datos:
                fila_limpia = fila.split(' ')
                fila_limpia = list(filter(''.__ne__, fila_limpia))
                escritor.writerow(fila_limpia)


def crear_directorios_datos():
    etiquetas = ['IMF Magnitude Avg',
                 'Bx GSE-GSM',
                 'By GSM',
                 'Bz GSM',

                 'Flow Speed',
                 'Proton Density',
                 'Proton Temperature']
    for nombre_directorio in etiquetas:
        try:
            os.stat(nombre_directorio)
        except:
            os.mkdir(nombre_directorio)

def seleccion_variables():
    directorios = ['IMF Magnitude Avg',
                 'Bx GSE-GSM',
                 'By GSM',
                 'Bz GSM',

                 'Flow Speed',
                 'Proton Density',
                 'Proton Temperature']
    etiquetas_base = ['Year', 'Day', 'Hour', 'Minute']
    etiquetas = ['IMF Magnitude Avg(nT)',
                 'Bx GSE-GSM(nT)',
                 'By GSM(nT)',
                 'Bz GSM(nT)',

                 'Flow Speed(km-sec)',
                 'Proton Density(n-cc)',
                 'Proton Temperature(K)']
    variables = ["/html/body/form/p[4]/b/table/tbody/tr[4]/th[1]/table/tbody/tr[1]/td/input",
                 "/html/body/form/p[4]/b/table/tbody/tr[4]/th[1]/table/tbody/tr[2]/td/input",
                 "/html/body/form/p[4]/b/table/tbody/tr[4]/th[2]/table/tbody/tr[1]/td/input",
                 "/html/body/form/p[4]/b/table/tbody/tr[4]/th[2]/table/tbody/tr[2]/td/input",

                 "/html/body/form/p[4]/b/table/tbody/tr[6]/th[1]/table/tbody/tr[1]/td/input",
                 "/html/body/form/p[4]/b/table/tbody/tr[6]/th[2]/table/tbody/tr[1]/td/input",
                 "/html/body/form/p[4]/b/table/tbody/tr[6]/th[2]/table/tbody/tr[2]/td/input"]
    for variable in range(len(variables)):
        for ano in range(27):
            anno = str(1995+ano)
            nombre_fichero = directorios[variable] + "/" + etiquetas[variable] + "_" + str(anno) + ".csv"
            if not (os.path.isfile(nombre_fichero)):
                #Obtenemos la pagina base (con todo desselecionados y los campos listos para introducir datos)
                obtener_pagina_base()
                #Seleccionamos la variable
                WebDriverWait(driver, 5) \
                    .until(EC.element_to_be_clickable((By.XPATH,
                                                       variables[variable]))) \
                    .click()
                fecha_inicio = anno+"0101"
                if anno == '2021':
                    fecha_fin = anno+"0218"
                else:
                    fecha_fin = anno + "1231"
                # 5.2 Enviamos la fecha de inicio
                WebDriverWait(driver, 5) \
                    .until(EC.element_to_be_clickable((By.XPATH,
                                                       '/html/body/form/p[3]/b/input[1]'))) \
                    .send_keys(fecha_inicio)
                # 6.2 Enviamos la fecha de fin
                WebDriverWait(driver, 5) \
                    .until(EC.element_to_be_clickable((By.XPATH,
                                                       '/html/body/form/p[3]/b/input[2]'))) \
                    .send_keys(fecha_fin)
                #8-Le damos a enviar
                WebDriverWait(driver, 5) \
                    .until(EC.element_to_be_clickable((By.XPATH,
                                                       '/html/body/form/p[4]/b/input'))) \
                    .click()
                #9-Seleccionamos los datos
                WebDriverWait(driver, 5) \
                    .until(EC.element_to_be_clickable((By.XPATH,
                                                       '/html/body/pre/a[1]'))) \
                    .click()

                #9-Obtenemos los datos
                nombre_directorio = directorios[variable]
                obtener_datos(anno, etiquetas[variable], etiquetas_base, nombre_directorio)
    """
    #10-leemos los datos para comprobar que se han escrito de forma correcta
    with open('IMF Magnitude Avg(nT)_1996.csv') as file:
        reader = csv.reader(file)
        cont = 0
        for fila in reader:
            print(fila)
            cont += 1
            if cont > 5:
                break
    """


def juntar_datos_por_variables():
    directorios = ['IMF Magnitude Avg',
                 'Bx GSE-GSM',
                 'By GSM',
                 'Bz GSM',

                 'Flow Speed',
                 'Proton Density',
                 'Proton Temperature']
    etiquetas = ['IMF Magnitude Avg(nT)',
                 'Bx GSE-GSM(nT)',
                 'By GSM(nT)',
                 'Bz GSM(nT)',

                 'Flow Speed(km-sec)',
                 'Proton Density(n-cc)',
                 'Proton Temperature(K)']
    for directorio in range(len(directorios)):
        nombre_fichero_escritura = directorios[directorio]+"/todo_"+etiquetas[directorio]+".csv"
        if not (os.path.isfile(nombre_fichero_escritura)):
            with open(nombre_fichero_escritura, 'w', newline='') as f:
                escritor = csv.writer(f)
                for ano in range(27):
                    nombre_fichero_lectura = directorios[directorio]+"/"+etiquetas[directorio]+"_"+str(1995+ano)+".csv"
                    with open(nombre_fichero_lectura) as file:
                        nombre_columnas_annadido = 0
                        reader = csv.reader(file)
                        if ano != 0:
                            #ya se ha anadido la cabezera al cominezo del fichero, pasamos la siguiente cabecera
                            next(reader)
                            for fila in reader:
                                escritor.writerow(fila)
                        else:
                            #Introducimos todas las lineas, incluida la cabecera
                            for fila in reader:
                                escritor.writerow(fila)


def juntar_variables():
    directorios = ['IMF Magnitude Avg',
                 'Bx GSE-GSM',
                 'By GSM',
                 'Bz GSM',

                 'Flow Speed',
                 'Proton Density',
                 'Proton Temperature']
    etiquetas = ['IMF Magnitude Avg(nT)',
                 'Bx GSE-GSM(nT)',
                 'By GSM(nT)',
                 'Bz GSM(nT)',

                 'Flow Speed(km-sec)',
                 'Proton Density(n-cc)',
                 'Proton Temperature(K)']
    nombre_columnas = ['Year', 'Day', 'Hour', 'Minute',
                       'IMF(nT)', 'Bx GSM(nT)', 'By GSM(nT)', 'Bz GSM(nT)',
                       'Flow Speed(km/s)', 'Proton Density(n/cc)', 'Proton Temperature(K)']
    dataframe = pd.DataFrame(columns=nombre_columnas)

    datos = []
    for variable in range(len(etiquetas)):
        nombre_fichero = directorios[variable]+"/"+"todo_"+etiquetas[variable]+".csv"
        dato = pd.read_csv(nombre_fichero, header=0)
        if variable == 0:
            dataframe['Year'] = dato['Year']
            dataframe['Day'] = dato['Day']
            dataframe['Hour'] = dato['Hour']
            dataframe['Minute'] = dato['Minute']
        dataframe[dataframe.columns[variable + 4]] = dato[dato.columns[-1]]

    dataframe.to_csv(r'datos.csv', index=False)
    print(dataframe)

def leer_csv_final():
    dato = pd.read_csv('datos.csv', header=0)
    print("mada")
#seleccion_variables()
#juntar_datos_por_variables()
driver.close()
leer_csv_final()
#seleccion_variables()
#crear_directorios_datos()

juntar_variables()
leer_csv_final()