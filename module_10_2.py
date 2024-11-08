import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.day_count = 0
        self.enemy_count = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy_count >= 0:
            self.enemy_count -= self.power
            self.day_count += 1
            time.sleep(1)
            if self.enemy_count >= 0:
                print(f'{self.name} сражается {self.day_count} дней(дня)..., осталось {self.enemy_count} войнов')
            if self.enemy_count == 0:
                print(f'{self.name} одержал победу спустя {self.day_count} дней(дня)!')


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print('Все битвы закончились!')
