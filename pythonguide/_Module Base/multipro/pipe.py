import time
from datetime import datetime
from multiprocessing import Process, Pipe, Queue

# from mul1 import mul1


def mul0(conn=False):
    list_x = []
    for i in range(10):
        x = datetime.now()
        list_x.append(x)
        if conn:
            conn.send(["mul0", x, i])
        time.sleep(1)
    # conn.poll()
    # conn.close()
    return conn.close()


def mul1(conn=False):
    list_x = []
    for i in range(10):
        x = datetime.now()
        list_x.append(x)
        if conn:
            conn.send(["mul1", x, i])
        time.sleep(1)
    # conn.poll()
    # conn.close()
    return conn.close()


if __name__ == "__main__":
    parrent_conn, child0_conn = Pipe(False)
    parrent_conn, child1_conn = Pipe(False)
    p = Process(target=mul0, args=(child0_conn,))
    p1 = Process(target=mul1, args=(child1_conn,))
    p.start()
    p1.start()
    while True:

        tc0 = child0_conn.recv()
        tc1 = child1_conn.recv()
        dtime = tc0[1] - tc1[1]

        print(f"{datetime.now()} : {tc0[2]} {tc1[2]} {dtime}")
        time.sleep(0.1)
    p.join()
    p1.join()

