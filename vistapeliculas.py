from PySide6.QtCore import QMetaObject
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QPushButton, QStatusBar,
                               QWidget, QListWidget, QDialog, QVBoxLayout)

class UiMainWindow:
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 600)
        self.centralwidget = QWidget(main_window)
        self.gridLayout = QGridLayout(self.centralwidget)

        self.boton_buscar_pelicula = QPushButton("Buscar", self.centralwidget)
        self.gridLayout.addWidget(self.boton_buscar_pelicula, 0, 3, 1, 1)

        self.line_edit = QLineEdit(self.centralwidget)
        self.line_edit.setPlaceholderText("Introduzca el nombre de la película")
        self.gridLayout.addWidget(self.line_edit, 0, 2, 1, 1)

        self.boton_buscar_por_actores = QPushButton("Buscar por actores", self.centralwidget)
        self.gridLayout.addWidget(self.boton_buscar_por_actores, 0, 0, 1, 1)

        self.label = QLabel("Película:", self.centralwidget)
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.catalogo = QListWidget(self.centralwidget)
        self.gridLayout.addWidget(self.catalogo, 2, 0, 1, 4)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        main_window.setStatusBar(self.statusbar)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        QMetaObject.connectSlotsByName(main_window)

class DetallesPeliculaDialog(QDialog):
    def __init__(self, datos_pelicula, parent=None):
        super().__init__(parent)
        self.setWindowTitle(datos_pelicula["titulo"])

        layout = QVBoxLayout(self)

        poster_label = QLabel(self)
        poster_pixmap = QPixmap(datos_pelicula["poster"])

        if poster_pixmap.isNull():
            poster_label.setText("No se pudo cargar el póster.")
        else:
            poster_label.setPixmap(poster_pixmap.scaled(200, 300))

        layout.addWidget(poster_label)
        layout.addWidget(QLabel(f"Título: {datos_pelicula['titulo']}", self))
        layout.addWidget(QLabel(f"Sinopsis: {datos_pelicula['sinopsis']}", self))
        layout.addWidget(QLabel(f"Puntuación: {datos_pelicula['puntuacion']}", self))
        layout.addWidget(QLabel(f"Actores: {', '.join(datos_pelicula['actores'])}", self))
        layout.addWidget(QLabel(f"Género: {datos_pelicula['genero']}", self))

        self.setLayout(layout)
