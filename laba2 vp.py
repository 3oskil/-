import numpy as np
from math import factorial
import random as r
import matplotlib.pyplot as plt

lambda1, mu, n = 1, 3, 4

M1 = np.array([[1, -4, 6, 0, 0],
               [0, 1, -7, 9, 0],
               [0, 0, 1, -10, 12],
               [0, 0, 0, 1, -12],
               [1, 1, 1, 1, 1]])
v1 = np.array([0, 0, 0, 0, 1])
v = list(np.linalg.solve(M1, v1))


def pk(lambda_, mu_, n_, k_):
    alpha = lambda_ / mu_
    nominator, denominator = alpha ** k_ / factorial(k_), 0
    for i in range(n_ + 1):
        denominator += alpha ** i / factorial(i)
    return nominator / denominator


pk_values = [pk(lambda1, mu, n, i) for i in range(n + 1)]


# print('Численные значения вероятностей занятости числа каналов:', list(v),
#       '\nТеоретические вероятности занятости числа каналов:', pk_values,
#       '\nРазница значений вероятностей занятости числа каналов:',
#       [v[i] - pk_values[i] for i in range(n + 1)], sep="\n")


def processing_requests(k_):
    if n_k[k][0] == 1:
        return f'\tКанал №{k} занят, время до освобождения = ' + str(abs(i - n_k[k][1] - n_k[k][2]))
    n_k[k][0], n_k[k][1], n_k[k][2] = 1, i + r.expovariate(lambda1), r.expovariate(mu)
    return f'\tПринят к обслуживанию на канале №{k}, время принятия = {n_k[k][1]}'


def channel_check(k_):
    if i - n_k[k][1] >= n_k[k][2]:
        n_k[k] = [0, 0, 0]


if __name__ == "__main__":
    T, Tk, i, number = 2, {i: 0 for i in range(n + 1)}, 0, 1
    n_k = {i: [0, 0, 0] for i in range(1, n + 1)}
    while i <= T:
        k = r.randint(1, n)
        print(str(number) + '. ' + f'Обращаемся к каналу №{k}:')
        for j in range(1, n + 1):
            channel_check(j)
        busy_channels = sum([n_k[i][0] for i in range(1, n + 1)])
        print(f'\tКоличество занятых каналов: {busy_channels}')
        Tk[busy_channels] += 0.1 / T
        print(processing_requests(k))
        number, i, = number + 1, i + 0.1
    print('\nОтношение занятости числа каналов: \n   ',
          '\t'.join([str(k) + ' каналов: ' + str(v) + '\n' for k, v in Tk.items()]))
    print('\nКаналы СМО после обслуживания:')
    for i in range(1, n + 1):
        print(f'\tКанал №{i} занят') if n_k[i][0] == 1 else print(f'\tКанал №{i} свободен')

    plt.bar(list(Tk.keys()), Tk.values(), color='g')

    fig1, ax1 = plt.subplots()
    ax1.pie(list(Tk.values()), labels=Tk.keys(), autopct='%1.1f%%')
    ax1.legend(['0 каналов',
                '1 канал',
                '2 канала',
                '3 канала',
                '4 канала'], loc='upper left', bbox_to_anchor=(1.0, 1.0))
    plt.show()

    alpha = lambda1 / mu
    Pde = list(Tk.values())[-1]
    q = 1 - Pde
    A = lambda1 * q
    k_mid = sum([Tk[0] * (alpha ** k) / (factorial(k - 1)) for k in range(1, n + 1)])
    p0_pro = (alpha ** n / factorial(n)) / sum([alpha ** k / factorial(k) for k in range(n + 1)])
    pk_pro = [p0_pro * alpha ** k / factorial(k) for k in range(1, n + 1)]
    print("\nВероятность отказа в обслуживании: ", Pde,
          "\nОтносительная пропускная способность: ", q,
          "\nАбсолютная пропускная способность: ", A,
          "\nСреднее число каналов, занятых обслуживанием: ", k_mid,
          "\nВероятность того, что все каналы заняты: ", p0_pro,
          "\nВероятность того, что в системе занято всего k каналов: ", pk_pro)