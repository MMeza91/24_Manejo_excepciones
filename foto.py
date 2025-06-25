from error import DimensionError


class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho > 1 and ancho < self.MAX:
            self.__ancho = ancho
        else:
            DimensionError("Mensaje", ancho, self.MAX)

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        self.__alto = alto