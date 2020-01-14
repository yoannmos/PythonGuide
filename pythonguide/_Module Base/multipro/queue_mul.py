import time
import logging
from datetime import datetime
from multiprocessing import Process, Queue
import queue

# Logging
FORMAT = "[%(levelname)s]  %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


def pro1(q=None, qperiod=0):
    logging.info("pro1 : Program Start")
    tq = time.time()
    i = 0
    while True:
        try:
            i += 1
            # --Do Stuff--
            time.sleep(0.2)
            # ------------
            t1 = time.time()
            tfreq = t1 - tq
            if q and tfreq >= qperiod:
                tq = time.time()
                q.put(["pro1", round(t1, 3), " -> ", i])
        except ValueError:
            logging.error("pro1 : ValueError")
            break
        except KeyboardInterrupt:
            logging.warning("pro1 : KeyboardInterrupt")
            break
        except Exception as e:
            logging.error(f"pro1 : {e}")
    return


def pro2(in_list, in_period, q=None, qperiod=0):
    logging.info("pro2 : Program Start")
    tq = time.time()
    time.sleep(5)
    for i in in_list:
        try:
            time.sleep(in_period)
            t1 = time.time()
            tfreq = t1 - tq
            if q and tfreq >= qperiod:
                tq = time.time()
                q.put(["pro2", round(t1, 3), i])
        except ValueError:
            logging.error("pro2 : ValueError")
            break
        except KeyboardInterrupt:
            logging.warning("pro2 : KeyboardInterrupt")
            break
        except Exception as e:
            logging.error(f"pro2 : {e}")
    logging.info("pro2 : Closing connection")
    return


if __name__ == "__main__":
    # ------------INPUT-------------
    in_period = 2  # [s]
    in_list = [p for p in range(0, 10, in_period)]
    # -----------OUTPUT-------------
    pr1_period = 1  # [s]
    pr2_period = 2  # [s]
    if pr2_period:
        assert in_period <= pr2_period and pr2_period % in_period == 0
    # ----------PROCESS-------------
    TIMEOUT = 40  # [s]
    q = Queue()
    p1 = Process(target=pro1, args=(q, pr1_period,))
    p2 = Process(target=pro2, args=(in_list, in_period, q, pr2_period,))
    p1.start()
    p2.start()
    logging.info("main : Program Start")
    ts = time.time()
    dt = 0
    # ----------MAINLOOP------------
    while p1.is_alive() and p2.is_alive():
        ta = time.time()
        dt = ta - ts
        try:
            qcontent = q.get(0)
            logging.info(f"{qcontent}")
            if dt > TIMEOUT:
                logging.warning("main : Timeout")
                break

        except queue.Empty:
            qcontent = None
            logging.debug("main : Queue is Empty")

        except queue.Full:
            logging.warning("main :Queue is full")

        except KeyboardInterrupt:
            logging.warning("main : KeyboardInterrupt")
            break

    p1.terminate()
    p2.terminate()
    logging.info("main : Closing connection")
    tf = time.time()
    logging.info(f"main : Program done in : {round(tf-ts, 2)} [s]")
