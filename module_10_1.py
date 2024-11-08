import time
import threading
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        s_n = 1
        while s_n <= word_count:
            time.sleep(0.1)
            file.write(f"Какое-то слово № {s_n}\n")
            s_n += 1
        print(f"Завершилась запись в файл {file_name}")


if __name__ == '__main__':
    start_time = datetime.now()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    end_time = datetime.now()
    w_t = end_time - start_time
    print(f'Работа потоков {w_t}')
    start_time = datetime.now()
    threads = []
    for count, name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
        thread = threading.Thread(target=write_words, args=(count, name))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = datetime.now()
    w_t = end_time - start_time
    print(f'Работа потоков {w_t}')
