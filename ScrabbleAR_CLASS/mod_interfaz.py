from pattern.es import verbs, tag, spelling, lexicon, parse
from mod_puntos import Puntaje
from mod_popups import Popups
import const


class Interfaz(Puntaje):

    def __init__(self, parametros):
        self._parametros = parametros
        self._popups = Popups()
        Puntaje.__init__(self)

    def primer_turno(self):
        if not self._parametros.get_primer_turno(): # SI NO ES EL PRIMER TURNO
            return False
        if self._parametros.get_palabra():  # SI HAY FICHAS EN LA PALABRA, ES DECIR, SE INGRESÓ UNA PALABRA
            for key in self._parametros.get_palabra():  # PARA CADA UBICACIÓN DE LAS LETRAS
                if key == (7, 7):   # SI SE UBICÓ ALGUNA EN EL CENTRO
                    self._parametros.set_primer_turno(False) # FINALIZA EL PRIMER TURNO
                    return False
        return True # SI ESTAMOS EN EL PRIMER TURNO, O HASTA ACÁ LO ESTUVIMOS (DEPENDE DE LA LÍNEA 20)

    def devolver_fichas(self, window, quien):
        palabra, atril = self._parametros.get_palabra(), getattr(self._parametros, 'get_atril_'+quien)() # EL ATRÍL SEGÚN QUIÉN, 'jugador' o 'bot'
        letras = list(palabra.values())
        for key in getattr(const, 'atril_'+quien):  # PARA CADA LLAVE EN EL ATRIL
            if atril[key] == '':    # SI LA FICHA NO TIENE LETRA
                self._parametros.add_letra_bolsa(letras[0]) # DEVOLVEMOS LA LETRA A LA BOLSA
                self._parametros.add_fichas()   # AUMENTAMOS LA CANTIDAD DE LETRAS DE LA BOLSA EN 1
                atril[key] = letras.pop(0)  # REUBICA LA LETRA EN EL ATRIL (.pop DEVUELVE Y ELIMINA EL ELEMENTO SEGÚN EL ÍNDICE, IGUAL QUE eliminar_en(pos) DE LISTAS EN ALGORITMOS)
        for key in palabra:
            self._parametros.pop_ficha_matriz(key) # BORRA LA MATRIZ
        getattr(self._parametros, 'set_atril_'+quien)(atril)  # RESETEA EL ATRIL
        const.const_Update(window, {key: '' for key in palabra}, atril)   # ACTUALIZA LA MATRIZ Y EL ATRIL

    def mover_ficha(self, window, key):
        ''' ESTA FUNCIÓN CUMPLE CON EL MOVIMIENTO DE LA FICHA
            SELECCIONADA (EN MANO) DESDE EL ATRIL HASTA LA MATRIZ.'''
        self._parametros.sacar_ficha_atril_jugador()    # SACA LA FICHA DEL ATRIL
        self._parametros.agregar_ficha_matriz(key)  # LA AGREGA A LA MATRIZ
        self._parametros.add_ficha_palabra({key: self._parametros.get_letra_ficha()})   # AGREGA LA FICHA A LA PALABRA
        const.const_Update(window, {self._parametros.get_key_ficha(): '', key: self._parametros.get_letra_ficha()}) # ACTUALIZA EL ATRIL Y LA MATRIZ
        self._parametros.set_letra_ficha('')    # BORRA LA LETRA DE LA FICHA

    def repartir_fichas(self, atril, window):
        ''' AGREGA LAS FICHAS SIN USAR A LA BOLSA. REPARTE HASTA 7 NUEVAS FICHAS.'''
        self._parametros.dec_fichas(7-len(atril))   # DECREMENTA LAS FICHAS SEGÚN LA CANTIDAD UTILIZADA, ES DECIR, RESTA LA CANTIDAD DE FICHAS UTILIZADAS
        for key in atril:   # PARA CADA UBICACIÓN EN EL ATRIL
            if atril[key] != '':
                self._parametros.add_letra_bolsa(atril[key])    # AGREGA LAS LETRAS NO UTILIZADAS
        if atril == self._parametros.get_atril_jugador():   # SI HABLAMOS DEL ATRIL DEL JUGADOR
            for i in range(7):  # SE REPARTEN LAS 7 NUEVAS FICHAS
                letra = {('jugador', i): self._parametros.letra_random()}   # GENERA UNA FICHA RANDOM
                self._parametros.agregar_ficha_atril_jugador(letra) # AGREGA LA FICHA RANDOM AL ATRIL
                self._parametros.dec_letra_bolsa(list(letra.values())[0])   # DECREMENTA LA CANTIDAD TOTAL DE FICHAS EN LA BOLSA
                const.const_Update(window, letra)   # ACTUALIZA EL ATRIL CON ESA LETRA
        else:   # SI HABLAMOS DEL ATRIL DEL BOT, LO MISMO QUE CON EL JUGADOR
            for i in range(7):
                letra = {('bot', i): self._parametros.letra_random()}
                self._parametros.agregar_ficha_atril_bot(letra)
                self._parametros.dec_letra_bolsa(list(letra.values())[0])
                const.const_Update(window, letra)
        const.const_Update(window, {'fichas_jugador': 'MIS FICHAS ~~~~~~ TOTAL DE FICHAS: '+str(self._parametros.get_fichas())})    # ACTUALIZA LA CANTIDAD TOTAL DE FICHAS EN LA VENTANA

    def _validar_palabra(self):
        ''' TRADUCE LAS FICHAS Y LAS ORDENA HORIZONTAL Y VERTICALMENTE. SI DE
            ALGUNA DE ESAS DOS MANERAS EXISTE LA PALABRA EN LOS LISTADOS DE
            PALABRAS, LA DEVUELVE, SINO, DEVUELVE UN STRING NULO "".'''
        palabra_en_x, palabra_en_y, palabra = '', '', self._parametros.get_palabra()   # DEFINIMOS LAS PALABRAS EN x E y Y LA PALABRA ACTUAL
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][0])}: # ESCRIBE LA PALABRA ORIENTADA EN x
            palabra_en_x += palabra[key]
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][1])}: # ESCRIBE LA PALABRA ORIENTADA EN y
            palabra_en_y += palabra[key]
        if palabra_en_x in lexicon or palabra_en_x in spelling or palabra_en_y in lexicon or palabra_en_y in spelling:
            if self._parametros.get_dificultad() == 'FÁCIL':
                return palabra # SI LA PALABRA EXISTE, INDEPENDIENTEMENTE DEL TIPO QUE SEA (YA QUE ESTAMOS EN DIFICULTAD FÁCIL), LA DEVUELVE, SINO, UN DICT VACÍO (DE ESTA MANERA SE PUEDE CORROVORAR SI LA PALABRA EXISTE PREGUNTANDO POR EL DICT VACIÓ O NO 'if not palabra' - 'if palabra')
            else:
                tipo = parse(str().join(list(self._parametros.get_palabra().values()))).split('/')[1]  # TIPO DE LA PALABRA. SI LA PALABRA ES UN VERBO, EL TIPO ES 'VB', SI ES UN ADJETIVO, 'JJ'. SOLO ESOS 2 TIPOS DE PALABRAS VALEN PARA 'MEDIO' O 'DIFICIL'. NO ES NECESARIO CORROVORAR SI LA PALABRA EXISTE EN SPELLING O LEXICON, PORQUE CUALFUERA ELA PALABRA, SI NO LA RECONOCE COMO VERBO 'VB' O ADJETIVO 'JJ', NO ES VÁLIDA. SOLAMENTE LAS RECONOCE COMO VERBO O ADJETIVO SI SE ENCUENTRA DENTRO DE SPELLING O LEXICON
                return palabra if tipo == 'VB' or tipo == 'JJ' else {}   # SI LA DIFICULTAD NO ES FÁCIL, INDEPENDIENTEMENTE DE LA PALABRA QUE SE HAYA ESCRITO, SI ES UN VERBO O UN ADJETIVO, LA DEVUELVE, SINO DEVUELVE UN DICT VACÍO (AL IGUAL QUE EN FÁCIL)
        else:
            return {}

    def calcular_palabra(self, window, quien):
        ''' CALCULA Y DEVUELVE EL PUNTAJE GANADO O PERDIDO AL FINALIZAR UN TURNO'''
        if len(self._parametros.get_palabra()) > 1:
            palabra = self._validar_palabra() # palabra RECIBE LA PALABRA SI ES VÁLIDA, SINO, UN DICT VACÍO (PALABRA VACÍA)
            if palabra: # ENTONCES, SI LA PALABRA ES VÁLIDA, SI palabra CONTIENE ELEMENTOS
                puntos = self.calcular_puntos(quien, palabra) # CALCULA LOS PUNTOS DE TAL PALABRA
                getattr(self._parametros, 'add_puntos_'+quien)(puntos)    # SUMA LOS PUNTOS CALCULADOS A QUIEN LE CORRESPONDA SEGÚN 'quien'
                self._parametros.add_historial('PALABRA: '+str().join(list(self._parametros.get_palabra().values())), 'VÁLIDA', ('+' if puntos > -1 else '')+str(puntos)+' PUNTOS')
                const.const_Update(window, {'puntos_'+quien: getattr(self._parametros, 'get_puntos_'+quien)()}) # ACTUALIZA EL PUNTAJE ACTUAL Y EL HISTORIAL
            else:   # SI LA PALABRA NO ES VÁLIDA
                self._parametros.add_historial('PALABRA: '+str().join(list(self._parametros.get_palabra().values())), 'INVÁLIDA', '+0 PUNTOS')
                self.devolver_fichas(window, quien)
            window.Element('historial').Update(self._parametros.get_historial())
            return True
        else:
            self._parametros.add_historial('PALABRA: '+str(str().join(list(self._parametros.get_palabra().values()))), 'INVÁLIDA', '+0 PUNTOS')
            window.Element('historial').Update(self._parametros.get_historial())
            return False

    def set_dificultad(self):
        self._set_dificultad(self._parametros.get_dificultad())

    def check_orientation(self, palabra):
        lista_posiciones = list(palabra.keys())
        firstPosition = lista_posiciones[0]
        lastPosition = lista_posiciones[-1]
        firstCol = lista_posiciones[0][0]
        lastCol = lista_posiciones[-1][0]
        if firstCol == lastCol:
            return 'Vertical'
        else:
            return 'Horizontal'
        # return 'Vertical' if list(palabra.keys())[0][0] == list(palabra.keys())[-1][0] else 'Horizontal'

    def evaluar_posicion(self, window, event, palabra):
        if palabra:
            lista_posiciones = list(palabra.keys())
            '''Si la posicion (x,y) que recibí esta fuera del rango,
               borro la letra de _palabra y actualizo el boton de la matriz '''
            if len(palabra) > 1:
                if lista_posiciones[0][0] != lista_posiciones[-1][0]:   # if self.check_orientation(palabra) == 'Horizontal':
                    if event[1] != lista_posiciones[0][1] or event[0] != lista_posiciones[-1][0]+1:
                        self._popups.popup('Error de colocacion de letra')
                        return False
                else:   # SI ES VERTICAL
                    if event[0] != lista_posiciones[0][0] or event[1] != lista_posiciones[-1][1]+1:
                        self._popups.popup('Error de colocacion de letra')
                        return False
            elif event[0] == lista_posiciones[-1][0]+1 or event[1] == lista_posiciones[-1][1]+1:
                return True
            else:
                self._popups.popup('Error de colocacion de letra')
                return False
        return True

# LINEA 119
# event = (1^, 2^)
# palabra = (5, 5^), (6, 5), (7^, 5)
# si 2^ != 5^ o 1^ != (7^+1)
#
# LOS DOS REFIEREN A SI SE COLOCAN LAS LETRAS CONSECUTIVAMENTE
#
# LINEA 123
# event = (1^, 2^)
# palabra = (5^, 5), (5, 6), (5, 7^)
# si 1^ != 5^ o 2^ != 7^+1
