"""game guess the number"""

import numpy as np
def random_predict(number:int=1) -> int:
    """__game guess the number

    Args:
        number (int, optional): _загаданное число_. Defaults to 1.

    Returns:
        int: _число попыток_
    """
    count = 0
    while True:
        count +=1
        predict_number = np.random.randint(1,101) #предполагаемое число
        if number == predict_number:
            break #выход из цикла если угадали
    return(count)

def score_game(random_predict) -> int:
    """_за какое в среднем кол-во попыток угадывает из 1000 подходов_

    Args:
        random_predict (_type_): _функция угадывания_

    Returns:
        int: _среднее кол-во попыток_
    """
    count_ls =[]
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101, size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
#run
score_game(random_predict)      

