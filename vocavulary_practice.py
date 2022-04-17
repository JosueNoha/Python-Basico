"""
Programa básico para practicar nuevo vocavulario en inglés

"""
import random

def choose_word(vocab):
    # elige una palabra al azar del diccionario
    i = random.randint(0, len(vocab.keys()))-1
    word = list(vocab.keys())[i]
    return word

def order_words():
    # retorna el orden de las palabras aleatorio
    num_answer = random.randint(0, 2)
    num_1 = random.randint(0, 2)
    while num_1 == num_answer:
        num_1 = random.randint(0, 2)
    sum_dict = {1:2,2:1,3:0}
    num_2 = sum_dict[num_answer+num_1]
    
    return [num_answer, num_1, num_2]

def print_english_words(answer,word_1,word_2,order):
    # imprime la palabra en inglés, las alternativas y comprueba si la respuesta es correcta
    words_dict = {order[0]:answer, order[1]:word_1, order[2]:word_2}
    print('Palabra en ingles: ')
    print(answer)
    print('\n Alternativas:')
    for i in range(3):
        print("{}) {}".format(i+1,vocavulary[words_dict[i]]) )

    m = int(input('\n Elija la opción correcta: '))

    if words_dict[m-1] == answer:
        print('\n Respuesta correcta')
    else:
        print('\n Respuesta incorrecta, la respuesta correcta es:\n {}'.format(vocavulary[answer]))

def print_spanish_words(answer,word_1,word_2,order):
    # imprime la palabra en español, las alternativas y comprueba si la respuesta es correcta
    words_dict = {order[0]:answer, order[1]:word_1, order[2]:word_2}
    print('Palabra en español: ')
    print(vocavulary[answer])
    print('\n Alternativas:')
    for i in range(3):
        print("{}) {}".format(i+1,words_dict[i]) )

    m = int(input('\n Elija la opción correcta: '))

    if words_dict[m-1] == answer:
        print('\n Respuesta correcta')
    else:
        print('\n Respuesta incorrecta, la respuesta correcta es:\n {}'.format(answer))

def select_words():
    #elige tres palabras para jugar, la primera es la respuesta correcta
    answer = choose_word(vocavulary)
    
    word_1 = choose_word(vocavulary)

    while word_1 == answer:
        word_1 = choose_word(vocavulary)

    word_2 = choose_word(vocavulary)

    while word_2 == answer or word_2 ==word_1:
        word_2 = choose_word(vocavulary)

    return answer, word_1, word_2


def elegir_modo():
    #permite elegir el modo de juego, se repite hasta tener una respuesta correcta
    mode = input('\n Elija 1 si desea jugar con palabras en inglés, 2 si desea jugar con palabras en español o 0 si desea finalizar: ')

    while mode not in ['0','1','2']:
        mode = input('\n Elija 1 si desea jugar con palabras en inglés, 2 si desea jugar con palabras en español o 0 si desea finalizar: ')

    return mode

def main():
    #programa principal, elige un modo de juego y se repite hasta elegir 0
    mode = elegir_modo()
    answer, word_1, word_2 = select_words()
    order = order_words()

    while mode in ['1','2']:
        if mode == '1':
            print_english_words(answer,word_1,word_2,order)

        elif mode == '2':
            print_spanish_words(answer,word_1,word_2,order)

        mode = elegir_modo()
        answer, word_1, word_2 = select_words()
        order = order_words()

vocavulary = {
    'crispness' : 'frescura',
    'hint' : 'indicio',
    'behead' : 'decapitar',
    'holdfast' : 'podio, grapa',
    'prickle' : 'picazón, espina',
    'skin pricke' : 'estremecimiento',
    'horns' : 'cuernos',
    'scrawny' : 'flaco',
    'furs' : 'pieles',
    'ragged' : 'harapiento (rag)',
    'faint' : 'tenue',
    'trimmed' : 'recortado (trim)',
    'grim' : 'severo',
    'dawnned' : 'amaneció (dawn)',
    'held' : 'retenido',
    'realm' : 'reino',
    'bolting' : 'empernado',
    'eagerly' : 'ansiosamente',
    'hooves' : 'pezuñas',
    'reced' : 'alejarse',
    'wrap' : 'envolver',
    'oath' : 'juramento',
    'oathbraker' : 'desertor',
    'farfeit' : 'falsificado',
    'feit' : 'falsificación',
    'bannerman' : 'abanderado',
    'waved' : 'agitar, ondear, saludar',
    'chief' : 'jefe',
    'mischief' : 'travesura',
    'grinned' : 'sonrió (grin)',
    'staind' : 'manchado',
    'bloodstaind' : 'ensangrentado',
    'glimpse' : 'vistazo',
    'gasp' : 'jadear',
    'tore' : 'razgar, quebrar',
    'nuzzle' : 'hocicar (acariciar con el hocico)',
    'whimpery' : 'lloriqueo',
    'hugged' : 'abrazado (hug)',
    'cheek' : 'mejilla',
    'frown' : 'fruncir el seño',
    'crunched' : 'triturado (crunch)',
    'throat' : 'garganta',
    'yaw' : 'guiñada',
    'yank' : 'tirón',
    'antled' : 'antílope',
    'antler' : 'cornamennta',
    'tassed' : 'probado',
    'tossed' : 'arrojado',
    'whelp' : 'parir',
    'snap' : 'quebrar',
    'tines' : 'dientes',
    'dismay' : 'consternación',
    'drown' : 'ahogar',
    'squirned' : 'retorcido',
    'furrowed' : 'surcado (furrow)',
    'stuborn' : 'obstinado',
    'sigil' : 'sigilo',
    'soak' : 'sumergir, empaparse, beber mucho',
    'kennel' : 'perrera',
    'neglect' : 'descuido',
    'despite' : 'a pesar de',
    'gather' : 'recolectar',
    'clatter' : 'estrépito',
    'swung' : 'balanceado',
    'kneel' : 'arrodillarse',
    'crawled' : 'rebajado, rastreado, arrastrado',
    'wry' : 'torcido',
    'chilling' : 'relajado, frío, escalofriante',
    'spread' : 'propagación',
    'tinkling': 'tintineo',
    'gloomy' : 'sombrio, melancólico',
    'moist' : 'húmedo',
    'oak' : 'roble',
    'branch' : 'sucursal, rama',
    'brooding' : 'melancólico, empollar',
    'censer' : 'incensario',
    'sake' : 'motivo',
    'sap' : 'savia',
    'lap': 'vuelta',
    'swalow': 'tragar',
    'mottoes' : 'lemas',
    'swatch' : 'muestra de tela',
    'glow': 'brillo',
    'rippling' : 'ondulación',
    'shudder' : 'estremecimiento',
    'bark' : 'ladrido, corteza',
    'ought' : 'debería',
    'sheath' : 'vaina',
    'grievous' : 'doloroso, penoso',
    'fastered' : 'ayunado',
    'pleaged' : 'suplicado',
    'grief': 'dolor',
    'seek' : 'buscar',
    'nodded' : 'asentir, incinar la cabeza',
    'coiled': 'enroscado',
    'swittest': 'más inteligente',
    'grimaced' : 'hacer muecas',
    'squeeze': 'exprimir'
}


if __name__ == '__main__':
    main()