#!/usr/bin/env python
# coding: utf-8


import numpy as np
def game_core_agrimony(number):
    '''мой ник в SkillFactory и в Slack - agrimony
		Сначала устанавливаем любое random число, а потом уменьшаем или
		увеличиваем его в зависимости от того, больше оно или меньше
		нужного.
		Функция принимает загаданное число и возвращает число попыток'''
		
    count = 1
    
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict = predict + step(count) #вводим переменный шаг как функцию
        elif number < predict: 
            predict = predict - step(count)
            
        if count > 50:
            break
		#если число итераций велико: что-то не так и нужно это остановить
    return(count)       # выход из цикла, если угадали


def step(count):             #функция для переменного изменения predict
    if count < 9:            #ограничиваем число итераций с переменным шагом
    #вычисляем шаг изменения как функцию числа попыток count
    #Это модификация анекдота о поиске льва в пустыне математиком:
    #https://www.anekdot.ru/id/15639/

        return int(50/count) 

    else:
        return 1 #в конце итерирования шаг должен быть минимален - т.е. 1
    

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, для воспроизводимости
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_agrimony)
