import timeit

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    results = []
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            results.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return results

# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    i = j = p = t = 0
    h = 1
    results = []

    for i in range(M-1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            if j + 1 == M:
                results.append(i)

        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t += q
    return results

# Алгоритм Боєра-Мура
def boyer_moore_search(text, pattern):
    def bad_char_heuristic(pattern):
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    bad_char = bad_char_heuristic(pattern)
    m = len(pattern)
    n = len(text)
    results = []
    s = 0

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            results.append(s)
            s += (m - bad_char.get(text[s + m], -1) if s + m < n else 1)
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return results

# Тексти
text1 = "Використання алгоритмів у бібліотеках мов програмування..."
text2 = "Методи та структури даних для реалізації бази даних рекомендаційної системи соціальної мережі..."

# Підрядки
real_substring = "бібліотеках мов програмування"
fake_substring = "марсіанська база"

# Заміри часу
def time_algorithm(algo, text, substring):
    setup_code = f"from __main__ import {algo}"
    stmt = f"{algo}('{text}', '{substring}')"
    times = timeit.repeat(setup=setup_code, stmt=stmt, number=10, repeat=3)
    return min(times)

# Вивід результатів
algorithms = ['kmp_search', 'rabin_karp_search', 'boyer_moore_search']
for algo in algorithms:
    for text, txt_name in [(text1, "Text 1"), (text2, "Text 2")]:
        for sub, name in [(real_substring, "Real"), (fake_substring, "Fake")]:
            time_taken = time_algorithm(algo, text, sub)
            print(f"{algo} time for {name} substring in {txt_name}: {time_taken:.6f}s")
