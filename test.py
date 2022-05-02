import numpy as np
a = np.int8(25)
print(a)

print(np.iinfo(np.int64))

print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
print(np.uint8(-456))

arr = np.array([1,5,2,9,10])
print(arr.dtype)
# dtype('int64')

#С каким шагом сгенерируется массив из 60 чисел от -6 до 21 включительно? Ответ округлите до двух знаков после точки.
arr, step = np.linspace(-6, 21, 60, endpoint=True, retstep=True)
print(round(step, 2))

#С каким шагом сгенерируется массив из 60 чисел от -6 (включительно) до 21 (не включительно)? 
# Ответ округлите до 2 знаков после точки.
arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(round(step, 2))

print(pd.__name__)