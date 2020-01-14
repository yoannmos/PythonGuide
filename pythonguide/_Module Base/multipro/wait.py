# based on example code from https://pymotw.com/2/multiprocessing/basics.html
import multiprocessing


def spawn(num):
    print('test!', num)


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        p.join()
