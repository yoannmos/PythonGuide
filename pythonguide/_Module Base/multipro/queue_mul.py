import time
from datetime import datetime
from multiprocessing import Process, Queue
import queue


class MyProcess(Process):
    def __init__(self, toExecute):
        # Call Mother Class Constructor
        Process.__init__(self)
        # Create shared Event for all process (__init__ is called in the main process)
        self.exit = Event()
        # Set method to execute
        self.toExecute = toExecute

    def run(self):
        # Children process (in same process group as main process) will
        # receive Ctrl-C signal, this is not our logical exit procedure
        # (we use shared events tested in processing loops, and proper
        # exit).
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        while not self.exit.is_set():
            self.toExecute()
        print("Process exited")


def pro0(conn=False):
    list_x = []
    # for i in range(10):
    i = 0
    while True:
        try:
            i += 1
            x = time.time()
            list_x.append(x)
            if conn:
                conn.put(["mul0", x, i])
            time.sleep(0.5)
        except ValueError:
            print("pr0 : ValueError")
            break
        except KeyboardInterrupt:
            print("pr0 : KeyboardInterrupt")
            break
        except Exception as e:
            print(f"pr0 : {e}")
    return


def pro1(conn=False):
    list_x = []
    for i in range(10):
        try:
            x = time.time()
            list_x.append(x)
            if conn:
                conn.put(["mul1", x, i])
            time.sleep(1)
        except ValueError:
            print("pr0 : ValueError")
            break
        except KeyboardInterrupt:
            print("pr0 : KeyboardInterrupt")
            break
        except Exception as e:
            print(f"pr0 : {e}")
    return


if __name__ == "__main__":
    q = Queue()
    p0 = Process(target=pro0, args=(q,))
    p1 = Process(target=pro1, args=(q,))
    p0.start()
    p1.start()
    ts = time.time()
    dt = 0
    while dt < 12:
        ta = time.time()
        dt = ta - ts
        try:
            qcontent = q.get(0)
            print(qcontent)

        except queue.Empty:
            qcontent = None
            # print("Empty")

        except queue.Full:
            print("fuuuuullll")

        except KeyboardInterrupt:
            p0.terminate()
            p1.terminate()
            print("Program stop Manually")
            break
    p0.terminate()
    p1.terminate()
    print("Program End")
    # if tc0[1] and tc1[1]:
    #     dtime = round(abs(tc0[1] - tc1[1]), 3)
    #     print(f"{datetime.now()} : {tc0[2]} {tc1[2]} {dtime}")

    # else:
    # dtime = None

    # time.sleep(0.01)
    # p0.join()
    # p1.join()

