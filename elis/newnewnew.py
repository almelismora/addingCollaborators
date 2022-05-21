
# DIMENSION FOL 
# un quiz para folear a tope

#villano 
folista = cl.Mob('true folista', 100, 40, 40, 20, 20)

## jugador 
brainstorming = cl.Habilidades('Lavado de cerebro', 'veneno', (5,5), 'envenena el cerebro y quita vidas')

nerd = cl.Jugador('Nerd', 100, 50, 40, 40, 30, 30, 'un libro en persona', './sources/bearseatbeets.m4a', brainstorming)

# mini-juego 
questions = {
    'La capital de Madagaskar: ':'C',
    'Quién de los siguientes trabajadores no puede sindicarse: ':'B',
    'Qué significa FAT: ':'A',
    'Qué componente es responsable del seguimiento de las variables en tiempo de ejecución: ':'D'
}

options = [
    ['A. Chad', 'B. Jakarta', 'C. Antananarivu', 'D. Madagaskar'],
    ['A. Un autónomo que no tiene asalariados', 'B. Un miembro de la Guardia Civil', 'C. Un funcionario', 'D. Todos tienen derecho a sindicarse'],
    ['A. File Allocation Table', 'B. File Absorption Transmission', 'C. File Attenuation Table', 'D. File Allocation Transmission'],
    ['A. Editor de textos', 'B. Intérprete', 'C. Compilador', 'D. Depurador']
]


def new_game():

    sp.mihilo_quiz_theme = sp.Songhilo()
    sp.mihilo_quiz_theme.set_song('./sources/Fluffing-a-Duck.mp3')
    sp.mihilo_quiz_theme.start()

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('-----------')
        print(key)
        
        for i in options[question_num-1]:
            print(i)

        player = input('Tu respuesta es (A, B, C, D): ')
        player = player.upper()
        guesses.append(player)

        correct_guesses += check_answer(questions.get(key), player)

        question_num += 1

    display_score(correct_guesses, guesses)



def check_answer(answer, player):
    if answer == player:
        print('MUY BIEN')
        return 1
    else:
        print('CAGASTE')
        return 0


def display_score(correct_guesses, guesses):
    
    global score
    score = int((correct_guesses/len(questions))*100)
    print('Tu resultado: '+str(score)+'%')


def play_again():
    
    if score < 75:
        print('Tienes que tener por lo menos 75% pasar pasar a la siguiente dimension\nTienes otra oportunidad:')
        return True 
    else:
        return False


new_game()

while play_again():
    new_game()

print('FELICITACIONES! HAS GANADO! CHAOOOO')



def mostrar_nerd():
    print('''
---------------------------------------------------------------------------------------------
                          
    Nombre : {}              
                                   
    Ataque : {}                               .'  `'.
                                             /  _    |                                      _
    Defensa : {}                             #_/.\==/.\                                    | |
                                            (, \_/ \\_/                 _ __    ___ _ __ __| |
    Precision : {}      ( 3 )                |    -' |                  | '_ \ / _ \ '__/ _` |
                                             \   '=  /                  | | | |  __/ | | (_| |
    Velocidad : {}                           /`-.__.'                   |_| |_|\___|_|  \__,_|  
                                          .-'`-.___|__ 
    Descripcion : {}                     /    \       `. 
    
---------------------------------------------------------------------------------------------
    '''.format(nerd.nombre,nerd.ataque,nerd.defensa,nerd.precision,nerd.velocidad,nerd.descripcion))


    mihilo_mostrar_nerd = sp.Songhilo_jugadores()
    mihilo_mostrar_nerd.set_song(nerd.sonido)
    mihilo_mostrar_nerd.start()
    del mihilo_mostrar_nerd

    
