# TODO Найдите количество книг, которое можно разместить на дискете
# Параметры дискеты
diskette_size_mb = 1.44
diskette_size_bytes = diskette_size_mb * 1024 * 1024  # 1.44 Мб в байтах

# Параметры книги
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Расчет размера одной книги
chars_per_book = pages_per_book * lines_per_page * chars_per_line
book_size_bytes = chars_per_book * bytes_per_char

# Расчет количества книг
books_count = int(diskette_size_bytes / book_size_bytes)

print("Количество книг, помещающихся на дискету:", books_count)
