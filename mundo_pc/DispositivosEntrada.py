class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    def __str__(self):
        return f'MARCA: {self._marca}, TIPO_ENTRADA: {self._tipo_entrada}'

    @property
    def marca(self):
        return self._marca

    @property
    def tipo_entrada(self):
        return self._tipo_entrada


if __name__ == '__main__':
    dispositivo1 = DispositivoEntrada('HP', 'USB')
    print(dispositivo1)
