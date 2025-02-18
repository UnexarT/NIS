from math import log2, ceil

x1 = "IF_WE_CANNOT_DO_AS_WE_WOULD_WE_SHOULD_DO_AS_WE_CAN"
x2 = "early_to_bed_and_early_to_rise_makes_a_man_wise"
x3 = "can_you_can_a_can_as_a_canner_can_can_a_can?"


def binary(char):
    bytes_data = char.encode('utf-8')

    # Преобразуем каждый байт в бинарный код
    binary_code = ' '.join(format(byte, '08b') for byte in bytes_data)

    return binary_code


def LZW(x):
    print(f"Шаг\t Словарь\t Номер слова\t Кодовые слова\t Затраты(бит)")
    # Задание переменных для алгоритма
    n = len(x)  # Длинна словаря
    X = set(char for char in x)  # Алфавит символов
    c = []  # Алфавит слов
    N = 0  # Номер символа в последовательности
    step = 1  # Счетчик шагов для вывода в таблице
    bit_sum = 0  # Счетчик затраченных бит
    zeros_len = 0
    last_code_word = ''
    last_zeros_len = 0

    while N < n:
        l = 1
        # Условие, что символ в алфавите слов
        if x[N] in c and len(c) > 0:
            cnt = 1  # Счетчик встреченных символов слов в последовательности
            j = x[N]  # Кэш обработчика

            # Цикл перебирающий последовательность на наличие слов из алфавита
            while (N + cnt != n and j in c):
                j += x[N + cnt]
                cnt += 1
                l = len(j) - 1

            if (len(j) == 1):
                num = c[:-1].index(j) + 1
                bin_N = bin(c[:-1].index(j) + 1)[2:]
                zeros_len = ceil(log2((len(c)))) - len(bin_N)
                code_word = zeros_len * '0' + bin_N
            else:
                if c[-1] != j[:-1]:
                    num = c[:-1].index(j[:-1]) + 1
                    bin_N = bin(c[:-1].index(j[:-1]) + 1)[2:]
                    zeros_len = ceil(log2((len(c)))) - len(bin_N)
                    code_word = zeros_len * '0' + bin_N
                else:
                    num = c.index(j[:-1]) + 1
                    zeros_len = ceil(log2((len(c))))
                    code_word = (zeros_len - last_zeros_len) * '0' + last_code_word
        else:
            num = 0
            j = x[N]
            if N == 0:
                code_word = binary(x[N])
            else:
                zeros_len = ceil(log2((len(c))))
                code_word = zeros_len * '0' + binary(x[N])

        last_zeros_len = zeros_len
        last_code_word = code_word
        N += l
        c.append(j)
        print(f" {step:<5} {c[step - 1]:<9} {num:>6} {code_word:>20} {len(code_word):>10}")
        bit_sum += len(code_word)
        step += 1

    print(f"Итого{bit_sum:>50}")


LZW(x1)
