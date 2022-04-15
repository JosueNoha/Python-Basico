"""
Programa básico para practicar nuevo vocavulario en inglés

"""
import random

def choose_word(vocab):
    # elige una palabra al azar del diccionario
    i = random.randint(0, len(vocab.keys()))
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

def print_words(answer,word_1,word_2,order):
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
    'hugged' : 'abrazodo (hug)',
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
    'clatter' : 'estrépido',
    'swung' : 'balanceado',
    'kneel' : 'arrodillarse',
    'crawled' : 'rebajado, rastreado, arrastrado',
    'wry' : 'torcido',
    'chilling' : 'relajado, frío, escalofriante'
}


if __name__ == '__main__':
    answer = choose_word(vocavulary)
    word_1 = choose_word(vocavulary)
    word_2 = choose_word(vocavulary)
    order = order_words()
    print_words(answer,word_1,word_2,order)