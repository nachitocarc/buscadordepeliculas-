import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCompleter
from PySide6.QtCore import Qt
from modelopeliculas import ModeloPeliculas
from vistapeliculas import UiMainWindow, DetallesPeliculaDialog


class MainWindow(QMainWindow):
    def __init__(self, modelo):
        super().__init__()
        self._ui = UiMainWindow()
        self._ui._setup_ui(self)

        self._modelo = modelo

        self.__cargar_peliculas()

        self.__configurar_completer(self._modelo.obtener_titulos(), self._ui.line_edit)

        self._ui.boton_buscar_pelicula.clicked.connect(self.__buscar_pelicula)
        self._ui.boton_buscar_por_actores.clicked.connect(self.__abrir_buscar_por_actores)
        self._ui.list_widget.itemClicked.connect(self.__mostrar_detalles_pelicula)

    def __cargar_peliculas(self):
        peliculas = self._modelo.obtener_peliculas()
        self._ui.list_widget.clear()
        for pelicula in peliculas:
            self._ui.list_widget.addItem(pelicula['titulo'])

    def __configurar_completer(self, opciones, line_edit):
        completer = QCompleter(opciones, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        line_edit.setCompleter(completer)

    def __buscar_pelicula(self):
        nombre_pelicula = self._ui.line_edit.text()
        self._ui.list_widget.clear()
        peliculas_encontradas = self._modelo.buscar_pelicula(nombre_pelicula)

        for pelicula in peliculas_encontradas:
            self._ui.list_widget.addItem(pelicula['titulo'])

    def __mostrar_detalles_pelicula(self, item):
        titulo_pelicula = item.text()
        pelicula = self._modelo.obtener_informacion_pelicula(titulo_pelicula)

        if pelicula:
            detalles_dialog = DetallesPeliculaDialog(pelicula, self)
            detalles_dialog.exec()

    def __abrir_buscar_por_actores(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Buscar por Actores")
        layout = QVBoxLayout(dialog)

        label = QLabel("Ingresa el nombre del actor:", dialog)
        layout.addWidget(label)

        actor_input = QLineEdit(dialog)
        layout.addWidget(actor_input)

        self.__configurar_completer(self._modelo.obtener_actores(), actor_input)

        boton_buscar = QPushButton("Buscar", dialog)
        layout.addWidget(boton_buscar)

        boton_buscar.clicked.connect(lambda: self.__buscar_por_actor(actor_input.text()))

        dialog.setLayout(layout)
        dialog.exec()

    def __buscar_por_actor(self, actor):
        peliculas_encontradas = self._modelo.buscar_por_actor(actor)
        self._ui.list_widget.clear()
        for titulo in peliculas_encontradas:
            self._ui.list_widget.addItem(titulo)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    modelo = ModeloPeliculas("peliculas.json")
    window = MainWindow(modelo)
    window.show()

    sys.exit(app.exec())
