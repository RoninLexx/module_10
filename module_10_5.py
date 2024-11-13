import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

    return all_data


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    linear_time = datetime.datetime.now() - start_time
    print(f"{linear_time} (линейный)")

    # Многопроцессный
    # start_time = datetime.datetime.now()
    # with multiprocessing.Pool() as pool:
    #     pool.map(read_info, filenames)
    # multi_process_time = datetime.datetime.now() - start_time
    # print(f"{multi_process_time} (многопроцессный)")
