from const import const_Update, reglas


class Turno:
    def __init__(self, parametros):
        self._parametros = parametros
        self._MS = 0    # MILISEGUNDOS

    def conteo(self, window):
        ''' MANTIENE ACTUALIZADO EL TIEMPO.'''
        self._MS += 100
        if self._MS == 1000:    # SI SE LLEGÓ AL SEGUNDO (MIL MILISEGUNDOS)
            self._MS = 0    # SE RESETEN LOS MILISEGUNDOS
            self._parametros.set_segundos(self._parametros.get_segundos()-1 if self._parametros.get_segundos() != 0 else self._parametros.get_tiempo_por_turno())   # SI SE LLEGÓ AL TIEMPO LÍMITE, SE REINICIA EL CONTADOR PARA EL SIGUIENTE TURNO, SINO, SE RESTA EN 1 EL TIEMPO ACTUAL
            const_Update(window, {'tiempo': self._parametros.get_segundos()})

    def fin_de_turno(self):
        ''' CAMBIA EL TURNO Y REINICIA EL TIEMPO.'''
        if len(self._parametros._palabra) == 0: # Fue turno del bot
            for letter in self._parametros._palabra_bot:
                self._parametros.dec_letra_bolsa(letter, 1)
        else:
            for pos, letter in self._parametros._palabra.items():    # Fue turno del jugador
                self._parametros.dec_letra_bolsa(letter, 1)
        self._parametros.set_turno(not self._parametros.get_turno())    # CAMBIA EL TURNO
        self._parametros.set_segundos(self._parametros.get_tiempo_por_turno())  # REINICIA EL CONTADOR A EL TIEMPO TOTAL POR TURNO
        self._MS = 900  # AL FINALIZAR EL TURNO, Y SE LLAME A conteo, SE SUMAN 100 MILISEGUNDOS Y CONTINUA NORMALMENTE
