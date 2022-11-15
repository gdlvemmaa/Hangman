import random


def get_word():
    # открываем файл со списком слов и выбираем из них одно
    with open('Word_rus.txt', 'r', encoding='utf-8') as word:
        return random.choice(word.readlines())[:-1].upper()


def is_valid(letter, guessed_word):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if len(letter) == 1 or len(letter) == len(guessed_word):
        for i in range(len(letter)):
            if letter[i] not in alphabet:
                return False
        else:
            return True
    else:
        return False


def play(word):
    word_completion = list('_' * len(word))  # строка, содержащая символы _
    # на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давай поиграем в Виселицу!')
    print(*word_completion)

    while tries >= 0:
        input_letter = input('Напиши букву или слово целиком\n').upper()
        if is_valid(input_letter, word):
            if input_letter in word:
                if input_letter == word:
                    print('Поздравляем, вы угадали слово!\n', word)
                    play_again()
                    break
                if input_letter not in guessed_letters and len(
                        input_letter) == 1:
                    guessed_letters.append(input_letter)
                    count_letter = word.count(input_letter)
                    for i in range(len(word)):
                        if input_letter == word[i]:
                            word_completion[i] = input_letter
                    print(*word_completion)
                    if ''.join(word_completion) == word:
                        print('Поздравляем, вы угадали слово!\n', word)
                        play_again()
                        break
                else:
                    print('Такая буква уже открыта', *word_completion)
            else:
                if len(input_letter) > 1 and input_letter not in guessed_words:
                    guessed_words.append(input_letter)
                    print(display_hangman(tries))
                    tries -= 1
                elif len(
                        input_letter) == 1 and input_letter not in guessed_letters:
                    guessed_letters.append(input_letter)
                    print(display_hangman(tries))
                    tries -= 1
                else:
                    print('Вы уже вводили эту букву/слово')
        else:
            print('Неверный ввод\n')
    else:
        print('Вы проиграли :(\n', word)
        play_again()


def play_again():
    while True:
        again = input('Сыграть ещё раз? ;) (да/нет)\n')
        if again.lower() == 'да':
            play(get_word())
            break
        elif again.lower() == 'нет':
            print('До новых встреч!')
            break
        else:
            print('введите да или нет')


def display_hangman(tries):
    stages = [
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / \\
        |
        |  GAME OVER

        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |     
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    
        |     
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     
        |    
        |       
        |  
        '''
    ]
    return stages[tries]


play(get_word())
