# Код начинается здесь ...
a = [-1, 3, 9, -6, 12, 3, 0, -18, 4, 'o', 'O', 0, 12, 'e', 'u']
with open("result_m_24_3.txt", "w", encoding="utf-8") as file:
    for item in a:
        if not str(item).isalpha() and int(item) < 0:
            file.write(str(item) + " ")
