from random import normalvariate as nd
from statistics import mean, variance
import matplotlib.pyplot as plt
import numpy as np

mu_, phi1_, sigma_, t_ = 2.5, 0.7, 0.5, 14
a_s_v = []


def ar1(arr_signal_val, mu, t, phi1, sigma):
    arr_signal_val.append(nd(0, sigma))
    for ii in range(0, t):
        arr_signal_val.append(phi1 * (arr_signal_val[ii] - mu) + mu + nd(0, sigma))
    return arr_signal_val


Na = 14
ar1(a_s_v, mu_, Na, phi1_, sigma_)
plt.plot(a_s_v, linewidth=0.8)
plt.title("Реализация сечения. Момент времени t = 14")
plt.show()

print("Исследование процесса на стационарность:\n")
N = (10, 100, 1000)
for i in range(3):
    Am, Am1 = [], []
    for _ in range(N[i]):
        arr_signal_val_ = []
        AT = ar1(arr_signal_val_, mu_, t_, phi1_, sigma_)
        Am.append(AT[t_ - 1])
        Am1.append(AT[t_ - 2])
    m, d = mean(Am), variance(Am)
    m1, d1 = mean(Am1), variance(Am1)
    print(f"{i + 1}. N = {N[i]}:\nСреднее арифметическое: ", m,
          f"\nВыборочная дисперсия: ", d,
          f"\nВыборочный коэффициент нормированной корреляции: ",
          (sum([(Am[j] - m) * (Am1[j] - m1) for j in range(N[i])])) / (N[i] * (
                  (d * d1) ** 0.5)), end="\n\n")

arr_signal_val_, Na = [], 1000
ar1(arr_signal_val_, mu_, Na, phi1_, sigma_)
plt.plot(arr_signal_val_, linewidth=0.8)
plt.show()

print("\nИсследование процесса на эргодичность:")
sample = []
ar1(sample, mu_, N[2], phi1_, sigma_)
m, d = mean(sample), variance(sample)
print("\nСреднее арифметическое по полученной выборке: ", m,
      "\nВыборочная дисперсия: ", d,
      "\nВыборочный коэффициент нормированной автокорреляции: ",
      (sum([(sample[j] - m) * (sample[j - 1] - m) for j in range(N[2] - 1)])) / (N[2] * d), end="\n\n")

print("\nИсследование сходимости выборочных характеристик к теоретическим: ")
for i in range(3):
    ar1(sample, mu_, N[i], phi1_, sigma_)
    m, d = mean(sample), variance(sample)
    print(f"{i + 1}. N = {N[i]}:\nСреднее арифметическое по полученной выборке: ", m,
          "\nВыборочная дисперсия: ", d,
          "\nВыборочный коэффициент нормированной автокорреляции: ",
          (sum([(sample[j] - m) * (sample[j - 1] - m) for j in range(N[2] - 1)])) / (N[2] * d), end="\n\n")


def corr_func(v):
    nom = [(v[q] - mean(v)) * (v[q - 1] - mean(v)) for q in range(int(len(v) / 4), len(v))]
    denom = [(q - mean(v)) ** 2 for q in v]
    r = [f / g for f in nom for g in denom if nom.index(f) == denom.index(g)]
    x = np.arange(1, len(r) + 1)
    fig, ax = plt.subplots()
    ax.bar(x, r, color='orange', edgecolor='black', lw=0.5)
    plt.show()
    return r


carr = corr_func(a_s_v)
print(carr)
