import time
from datetime import datetime


def mul1(conn=False):
    list_x = []
    for i in range(10):
        x = datetime.now()
        list_x.append(x)
        if conn:
            conn.send(["mul1", x, i])
        time.sleep(0.5)
    conn.close()
    return list_x


if __name__ == "__main__":
    mul1()
