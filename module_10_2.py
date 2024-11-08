import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        day_count = 0
        enemy_count = 100
        while enemy_count >= 0:
            enemy_count -= self.power
            day_count += 1
            time.sleep(1)
            if enemy_count >= 0:
                print(f'{self.name} сражается {day_count} дней(дня)..., осталось {enemy_count} войнов')
            if enemy_count == 0:
                print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print('Все битвы закончились!')
