import json

class ModeloPeliculas:
    def __init__(self, peliculas_json):
        self.__peliculas = self.__cargar_peliculas(peliculas_json)

    def __cargar_peliculas(self, archivo_json):
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)

    def buscar_pelicula(self, nombre):
        nombre = nombre.lower()
        return [pelicula for pelicula in self.__peliculas if nombre in pelicula["titulo"].lower()]

    def obtener_informacion_pelicula(self, titulo):
        for pelicula in self.__peliculas:
            if pelicula["titulo"] == titulo:
                return pelicula

    def buscar_por_dos_actores(self, actor1, actor2):
        actor1 = actor1.lower()
        actor2 = actor2.lower()
        return [pelicula["titulo"] for pelicula in self.__peliculas
                if actor1 in (a.lower() for a in pelicula["actores"])
                and actor2 in (a.lower() for a in pelicula["actores"])]

    def obtener_titulos(self):
        return [pelicula["titulo"] for pelicula in self.__peliculas]

    def obtener_actores(self):
        actores = set()
        for pelicula in self.__peliculas:
            actores.update(pelicula["actores"])
        return list(actores)
