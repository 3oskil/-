import numpy as np
import matplotlib.pyplot as plt
from scipy import fft
from random import normalvariate as nd, expovariate as ed, uniform


def corr_func(v, text=None, graphic=True):
    """"Корреляционная функция"""
    r = []
    for t in range(int(len(v) / 4) + 1):
        s = 0
        for j in range(len(v) - t):
            s += (v[j + t] - np.mean(v)) * (v[j] - np.mean(v))
        r.append(s / (len(v) - t))
    r = np.array(r) / r[0]
    if graphic is True:
        plt.plot(r, lw=1)
        plt.title(text)
        plt.show()
    else:
        return r


def spectrum(v, text):
    """"Спектр сигнала"""
    abs_fourier_v = np.abs(fft.fft(v))
    plt.plot(abs_fourier_v / np.max(abs_fourier_v), lw=1)
    plt.title(text)
    plt.show()


def spectral_density(r, text):
    """Плотность спектра"""
    abs_fourier_v = np.abs(fft.fft(r))
    plt.plot(abs_fourier_v / np.max(abs_fourier_v), lw=1)
    plt.title(text)
    plt.show()


if __name__ == "__main__":
    # Реализация гармонического сигнала
    Nx, A1, A2, w1, w2 = 1000, 5, 10, 5, 24
    harm_sig = [A1 * np.cos(w1 * 2 * np.pi * t / Nx) + A2 * np.cos(w2 * 2 * np.pi * t / Nx) for t in range(1, Nx + 1)]
    plt.plot(harm_sig, lw=1)
    plt.axis([0, 400, -15, 15])
    plt.title('Гармонический сигнал. Реализация процесса.')
    plt.show()

    corr_func(harm_sig, 'Гармонический сигнал.\nНомированная корреляционная функция.\n')

    spectrum(harm_sig, 'Гармонический сигнал.\nМодуль спектра.')

    spectral_density(corr_func(harm_sig, graphic=False),
                     'Гармонический сигнал.\nСпектральная плотность, '
                     'полученная\nпреобразованием Фурье корреляционной функции')

    # Реализация телеграфного сигнала
    lambda1, tel_sig, k, t = 2, [], 1, 0
    while t < 1000:
        tau = int(np.rint(uniform(0, ed(lambda1)) * 10))
        tel_sig += [k for _ in range(tau)]
        k *= -1
        t += tau

    plt.plot(tel_sig, lw=0.5)
    plt.title('Телеграфный сигнал.')
    plt.show()

    corr_func(tel_sig, 'Телеграфный сигнал.\nНомированная корреляционная функция.\n')

    spectrum(tel_sig, 'Телеграфный сигнал.\nМодуль спектра.')

    spectral_density(corr_func(tel_sig, graphic=False),
                     'Телеграфный сигнал.\nСпектральная плотность, '
                     'полученная\nпреобразованием Фурье корреляционной функции')

    # Процесс авторегрессии 1-го порядка
    fi1 = 0.5
    auto_reg = [nd(0, 1)]
    for t in range(Nx - 1):
        auto_reg.append(fi1 * auto_reg[t] + nd(0, 1))

    plt.plot(auto_reg, lw=0.5)
    plt.title('Процесс авторегрессии 1-го порядка.')
    plt.show()

    corr_func(auto_reg, 'Процесс авторегрессии 1-го порядка.\nНомированная корреляционная функция.\n')

    spectrum(auto_reg, 'Процесс авторегрессии 1-го порядка.\nМодуль спектра.')

    spectral_density(corr_func(auto_reg, graphic=False),
                     'Процесс авторегрессии 1-го порядка.\nСпектральная плотность, '
                     'полученная\nпреобразованием Фурье корреляционной функции')

    # Зашумленнный сигнал
    A1, A2, w1, w2, fi1, auto_reg_1 = 5, 10, 5, 24, 0.5, [nd(0, 1)]
    harm_sig_1 = [A1 * np.cos(w1 * 2 * np.pi * t / Nx) + A2 * np.cos(w2 * 2 * np.pi * t / Nx) for t in range(1, Nx + 1)]
    for t in range(Nx - 1):
        auto_reg_1.append(fi1 * auto_reg_1[t] + nd(0, 1))

    noisy_signal = np.array(harm_sig_1) + 20 * np.array(auto_reg_1)

    plt.plot(noisy_signal, lw=0.5)
    plt.title('Зашумленный сигнал.')
    plt.show()

    corr_func(noisy_signal, 'Зашумленный сигнал.\nНомированная корреляционная функция.\n')

    spectrum(noisy_signal, 'Зашумленный сигнал.\nМодуль спектра.')

    spectral_density(corr_func(noisy_signal, graphic=False),
                     'Зашумленный сигнал.\nСпектральная плотность, '
                     'полученная\nпреобразованием Фурье корреляционной функции')