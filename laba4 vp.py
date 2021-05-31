from random import normalvariate as nd, expovariate as ed, uniform
import numpy as np
import matplotlib.pyplot as plt


def corr_func(v, text):
    r = []
    for t in range(int(len(v) / 4) + 1):
        s = 0
        for j in range(len(v) - t):
            s += (v[j + t] - np.mean(v)) * (v[j] - np.mean(v))
        r.append(s / (len(v) - t))
    r = np.array(r) / r[0]
    plt.plot(r, lw=1)
    plt.plot([0, 250], [1.96 / np.sqrt(len(v)), 1.96 / np.sqrt(len(v))], lw=1, color='C0')
    plt.plot([0, 250], [-1.96 / np.sqrt(len(v)), -1.96 / np.sqrt(len(v))], lw=1, color='C0')
    plt.title(text)
    plt.show()


# Реализация гармонического сигнала со случайной фазой
Nx, A, w1, w2, Fi = 1000, 5, 5, 24, uniform(0, 2 * np.pi)
harm_sig_1 = [A * np.cos(w1 * 2 * np.pi * t / Nx + Fi) for t in range(1, Nx + 1)]
print('Гармонический сигнал. Частота w1 = 5. Значение характеристик процесса:',
      f'Среднее арифметическое значение = {np.around(np.mean(harm_sig_1), decimals=3)}' +
      f' выборочная дисперсия = {np.around(np.var(harm_sig_1), decimals=3)}', sep='\n')
plt.plot(harm_sig_1, lw=1)
plt.axis([0, 400, -6, 6])
plt.title('Гармонический сигнал. Выборочная реализация процесса.\nЧастота w1 = 5')
plt.show()

harm_sig_2 = [A * np.cos(w2 * 2 * np.pi * t / Nx + Fi) for t in range(1, Nx + 1)]
print('Гармонический сигнал. Частота w2 = 24. Значение характеристик процесса:',
      f'Среднее арифметическое значение = {np.around(np.mean(harm_sig_2), decimals=3)}' +
      f' выборочная дисперсия = {np.around(np.var(harm_sig_2), decimals=3)}', sep='\n')
plt.plot(harm_sig_2, lw=1)
plt.axis([0, 400, -6, 6])
plt.title('Гармонический сигнал. Выборочная реализация процесса.\nЧастота w2 = 24')
plt.show()

plt.hist(harm_sig_1, edgecolor='black', lw=0.5, color='orange')
plt.title('Гармонический сигнал. Гистограмма.\nЧастота w1 = 5')
plt.show()

plt.hist(harm_sig_2, edgecolor='black', lw=0.5, color='orange')
plt.title('Гармонический сигнал. Гистограмма.\nЧастота w2 = 24')
plt.show()

corr_func(harm_sig_1, 'Гармонический сигнал.\nВыборочная номированная корреляционная функция.\nЧастота w1 = 5')
corr_func(harm_sig_2, 'Гармонический сигнал.\nВыборочная номированная корреляционная функция.\nЧастота w2 = 24')

plt.plot([np.cos(w1 * k) for k in range(250)], lw=1)
plt.title('Гармонический сигнал. Теоретическая корреляционная функция.\nЧастота w1 = 5')
plt.show()

plt.plot([np.cos(w2 * k) for k in range(250)], lw=1)
plt.title('Гармонический сигнал. Теоретическая корреляционная функция.\nЧастота w1 = 24')
plt.show()


# Реализация телеграфного сигнала
lambda1, lambda2, tel_sig_1, k, t = 2, 1 / 5, [], 1, 0
while t < 1000:
    tau = int(np.rint(uniform(0, ed(lambda1)) * 10))
    tel_sig_1 += [k for _ in range(tau)]
    k *= -1
    t += tau

plt.plot(tel_sig_1, lw=0.8)
plt.title('Обобщенный телеграфный сигнал. Выборочная реализация процесса.\nИнтенсивность lambda1 = 2.')
plt.show()

print('Обобщенный телеграфный сигнал. Интенсивность lambda1 = 2. Значение характеристик процесса:',
      f'Среднее арифметическое значение = {np.around(np.mean(tel_sig_1), decimals=3)},'
      f' выборочная дисперсия= {np.around(np.var(tel_sig_1), decimals=3)}', sep='\n')

t, k, tel_sig_2 = 0, 1, []
while t < 1000:
    tau = int(np.rint(uniform(0, ed(lambda2)) * 10))
    tel_sig_2 += [k for _ in range(tau)]
    k *= -1
    t += tau

plt.plot(tel_sig_2, lw=1)
plt.title('Обобщенный телеграфный сигнал. Выборочная реализация процесса.\nИнтенсивность lambda2 = 1/5.')
plt.show()

print('Обобщенный телеграфный сигнал. Интенсивность lambda2 = 1/5. Значение характеристик процесса:',
      f'Среднее арифметическое значение = {np.around(np.mean(tel_sig_2), decimals=3)},'
      f' выборочная дисперсия= {np.around(np.var(tel_sig_2), decimals=3)}', sep='\n')

plt.hist(tel_sig_1, ec='black', lw=0.5, color='orange', bins=[-1, 0, 1])
plt.title('Обобщенный телеграфный сигнал. Гистограмма.\nИнтенсивность lambda1 = 2.')
plt.show()

plt.hist(tel_sig_2, ec='black', lw=0.5, color='orange', bins=[-1, 0, 1])
plt.title('Обобщенный телеграфный сигнал. Гистограмма.\nИнтенсивность lambda2 = 1/5.')
plt.show()

corr_func(tel_sig_1,
          'Обобщенный телеграфный сигнал.\n'
          'Выборочная номированная корреляционная функция.\n'
          'Интенсивность lambda1 = 2.')
corr_func(tel_sig_2,
          'Обобщенный телеграфный сигнал.\n'
          'Выборочная номированная корреляционная функция.\n'
          'Интенсивность lambda2 = 1/5.')

plt.plot([np.exp(-2 * lambda1 * np.abs(k)) for k in range(250)], lw=1)
plt.title('Обобщенный телеграфный сигнал.\nТеоретическая корреляционная функция.\nИнтенсивность lambda1 = 2')
plt.show()

plt.plot([np.exp(-2 * lambda2 * np.abs(k)) for k in range(250)], lw=1)
plt.title('Обобщенный телеграфный сигнал.\nТеоретическая корреляционная функция.\nИнтенсивность lambda1 = 1/5')
plt.show()


# Реализация авторегрессии 1-го порядка
fi1, fi2, sigma = 0.11, -0.5, 5 / 2
auto_reg_1, auto_reg_2 = [nd(0, sigma)], [nd(0, sigma)]
for t in range(Nx - 1):
    auto_reg_1.append(fi1 * auto_reg_1[t] + nd(0, sigma))
print('Процесс авторегрессии 1-го порядка. Параметр авторегрессии fi1 = 0.11. Значение характеристик процесса:',
      f'Среднее арифметическое значение = {np.around(np.mean(auto_reg_1), decimals=3)}' +
      f' выборочная дисперсия = {np.around(np.var(auto_reg_1), decimals=3)}', sep='\n')
plt.plot(auto_reg_1, lw=1)
plt.title('Процесс авторегрессии 1-го порядка.\nВыборочная реализация процесса.\nПараметр авторегрессии fi1 = 0.11')
plt.show()

for t in range(Nx - 1):
    auto_reg_2.append((fi2 * auto_reg_2[t]) + nd(0, sigma))
print('Процесс авторегрессии 1-го порядка. Параметр авторегрессии fi2 = -0.5. Значение характеристик процесса:',
      f'Среднее арифметическое значение = {np.around(np.mean(auto_reg_2), decimals=3)}' +
      f' выборочная дисперсия = {np.around(np.var(auto_reg_2), decimals=3)}', sep='\n')
plt.plot(auto_reg_2, lw=1)
plt.title('Процесс авторегрессии 1-го порядка.\nВыборочная реализация процесса.\nПараметр авторегрессии fi2 = -0.5')
plt.show()

plt.hist(auto_reg_1, ec='black', lw=0.5, color='orange')
plt.title('Процесс авторегрессии 1-го порядка. Гистограмма.\nПараметр авторегрессии fi1 = 0.11.')
plt.show()

plt.hist(auto_reg_2, ec='black', lw=0.5, color='orange')
plt.title('Процесс авторегрессии 1-го порядка. Гистограмма.\nПараметр авторегрессии fi2 = -0.5.')
plt.show()

corr_func(auto_reg_1,
          'Процесс авторегрессии 1-го порядка.\n'
          'Выборочная номированная корреляционная функция.\n'
          'Параметр авторегрессии fi1 = 0.11.')
corr_func(auto_reg_2,
          'Процесс авторегрессии 1-го порядка.\n'
          'Выборочная номированная корреляционная функция.\n'
          'Параметр авторегрессии fi2 = -0.5.')

plt.plot([fi1 ** k for k in range(250)], lw=1)
plt.title('Процесс авторегрессии 1-го порядка.\n'
          'Теоретическая корреляционная функция.\nПараметр авторегрессии fi1 = 0.11.')
plt.show()

plt.plot([fi2 ** k for k in range(250)], lw=1)
plt.title('Процесс авторегрессии 1-го порядка.\n'
          'Теоретическая корреляционная функция.\nПараметр авторегрессии fi2 = -0.5.')
plt.show()


# Реализация последовательности независимых случайных величин
a1, b1, a2, b2 = -5, 5, 0, 2.5
ind_rand_vars_1, ind_rand_vars_2 = [uniform(a1, b1) for _ in range(Nx)], [nd(a2, b2) for _ in range(Nx)]
print(
    'Последовательность независимых случайных величин распределенных равным законом с параметрами a1 = -5, b1 = 5.'
    '\nЗначение характеристик процесса:\n' +
    f'Среднее арифметическое значение = {np.around(np.mean(ind_rand_vars_1), decimals=3)}' +
    f' выборочная дисперсия = {np.around(np.var(ind_rand_vars_1), decimals=3)}', sep='\n')
plt.plot(ind_rand_vars_1, lw=1)
plt.title(
    'Последовательность независимых случайных величин.\nВыборочная реализация процесса.'
    '\nРавномерный закон распределения с параметрами a1 = -5, b1 = 5')
plt.show()

print(
    'Последовательность независимых случайных величин распределенных нормальным законом с параметрами a2 = 0, b2 = 2.5.'
    '\nЗначение характеристик процесса:',
    f'Среднее арифметическое значение = {np.around(np.mean(ind_rand_vars_2), decimals=3)}' +
    f' выборочная дисперсия = {np.around(np.var(ind_rand_vars_2), decimals=3)}', sep='\n')
plt.plot(ind_rand_vars_2, lw=1)
plt.title(
    'Последовательность независимых случайных величин.\nВыборочная реализация процесса.'
    '\nНормальный закон распределения с параметрами a2 = 0, b2 = 2.5')
plt.show()

plt.hist(ind_rand_vars_1, ec='black', lw=0.5, color='orange')
plt.title('Последовательность независимых случайных величин. Гистограмма.\n'
          'Равномерный закон распределения с параметрами a1 = -5, b1 = 5.')
plt.show()

plt.hist(ind_rand_vars_2, ec='black', lw=0.5, color='orange')
plt.title('Последовательность независимых случайных величин. Гистограмма.\n'
          'Нормальный закон распределения с параметрами a2 = 0, b2 = 2.5.')
plt.show()

corr_func(ind_rand_vars_1,
          'Пследовательность независимых случайных величин.\n'
          'Выборочная номированная корреляционная функция.\n'
          'Равномерный закон распределения с параметрами a1 = -5, b1 = 5.')
corr_func(ind_rand_vars_2,
          'Последовательность независимых случайных величин.\n'
          'Выборочная номированная корреляционная функция.\n'
          'Нормальный закон распределения с параметрами a2 = 0, b2 = 2.5.')

plt.plot([(1 if k == 0 else 0) for k in range(250)], lw=1)
plt.title('Последовательность независимых случайных величин.\n'
          'Теоретическая корреляционная функция.\nРавномерный закон распределения с параметрами a1 = -5, b1 = 5.')
plt.show()

plt.plot([(1 if k == 0 else 0) for k in range(250)], lw=1)
plt.title('Последовательность независимых случайных величин.\n'
          'Теоретическая корреляционная функция.\nНормальный закон распределения с параметрами a2 = 0, b2 = 2.5.')
plt.show()
