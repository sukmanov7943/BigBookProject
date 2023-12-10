import random   #  импортируем все необходимые модули
#  обЪявляем глобальные переменные
len_digits = 3  # длинна угадываемого числа
max_guesses = 10 # количество попыток
#  инструкция main с правилами игры
def main():
    print(f'В дедуктивной логической игре <<Бейглз>> необходимо по подсказкам'
          f'угадать секретное число из {len_digits} цифр. В ответ на ваши попытки'
          f'угадать число игра выдает одну из подсказок Pico, если вы угадали правильную '
          f'цифру на неправильном месте, Fermi если в вашей догадке есть правильная цифра'
          f'на правильном месте и Bagles, если в догадке не содержится правильных цифр.'
          f'На угадывание числа у вас {max_guesses} попыток.')
    while True:     #4 основной цикл пока тру
        secret_num = getsecretNum()                             #5 создаем переменную для хранения числа
        print('Я загадал секретное число')
        print(f'У вас есть {max_guesses} попыток чтобы угадать это число')

        numGuesses=1        #открываем счетчик попыток
        while numGuesses <= max_guesses:
            guess = ''

            while len(guess) != len_digits or not guess.isdecimal():
                print('Попытка #{}: '.format(numGuesses))
                guess = input('> ')
                clues = getClues(guess, secret_num)
                print(clues)
                numGuesses += 1
            if guess == secret_num:
                break  # Правильно, выходим из цикла.
            if numGuesses > max_guesses:
                print('Вы использовали все попытки')
                print('Ответ -  {}.'.format(secret_num))
        # Спрашиваем игрока, хочет ли он сыграть еще раз.
        print('Хотите сыграть еще раз? (да или нет)')
        if not input('> ').lower().startswith('д'):
            break
        print('Спасибо за игру!!!')
def getsecretNum():#функция для создания секретного числа
    numbers=list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(len_digits):
        secret_num+=str(numbers[i])
    return secret_num


#функция для вывода подсказок
def getClues(guess,secret_num):
    if guess==secret_num:
        return 'Вы угадали!!! Поздравляю!!!!'

    clues = []           # список подсказок

    for i in range(len(guess)):
        if guess[i]==secret_num[i]: # правильное число на правильном месте
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagles'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
#
#
#
#
#
#
#
#

#
#
#

#
#
#
#
#

#
#
#
#

#
#
#
#

#
#
#
#



#
#
#
#
#
#
#
#
#

#
#
#
#
#
#

#
#



