import csv
from pymongo import MongoClient

# Conexión a MongoDB, si no la encuentra entonces la crea junto con la coleccion
client = MongoClient('localhost', 27017)
db = client['atp_tennis_db']
collection = db['atp_tennis_coleccion']


# Abre el archivo CSV
archivo = open('atp_tennis.csv', 'r', encoding='utf-8')
lineas = csv.DictReader(archivo)

#Aqui guarda los datos en la base de datos
for linea in lineas:

    # Convierto las columnas 'Rank_1', 'Rank_2', 'Pts_1', 'Pts_2' a enteros para tener varios tipos de datos.
    linea['Rank_1'] = int(linea['Rank_1'])
    linea['Rank_2'] = int(linea['Rank_2'])
    linea['Pts_1'] = int(linea['Pts_1'])
    linea['Pts_2'] = int(linea['Pts_2'])
    
    # Inserta el documento en la colección llamada 'atp_tennis_coleccion'
    collection.insert_one(linea)
    
    

# Cerrar el archivo después de terminar de leerlo
archivo.close()

print("Datos insertados en MongoDB.")

# Consulta en MongoDB para obtener todos los partidos junto con el torneo al que pertenece,
# al ganador y el marcador de ese partido con collection.find()

lineas_mongo = collection.find()
print("Consulta en MongoDB:")
for l in lineas_mongo:
    print("Torneo: %s, Round: %s, Ganador: %s, Marcador: %s\n" % (
        l["Tournament"], 
        l["Round"], 
        l["Winner"], 
        l["score"]))
        