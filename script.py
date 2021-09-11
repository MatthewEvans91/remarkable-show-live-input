import re
import sys
from subprocess import PIPE, Popen, STDOUT
from threading import Thread
from queue import Queue, Empty
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


HOSTNAME = "remarkable"
OPTIONS = ""  # "--grab"


def enqueue_output(out, queue):
    for line in iter(out.readline, b""):
        queue.put(line)
    out.close()


def plot_coord(i):
    xs, ys = [], []
    while True:
        try:
            line = q.get_nowait()  # or q.get(timeout=.1)
        except Empty:
            # print("no more output")
            break

        try:
            m = re.search(r"\([0-9]+\.00/[0-9]+\.00mm\)", line.decode("utf-8"))
            x, y = [float(x) for x in m.group()[1:-3].split("/")]
            xs.append(x)
            ys.append(y)
        except Exception:
            pass

    # ax.clear()
    ax.scatter(xs, ys)


p = Popen(
    [
        "ssh",
        "-o StrictHostKeyChecking=no",
        "-t",
        HOSTNAME,
        "/usr/libexec/libinput/libinput-debug-events {}".format(OPTIONS),
    ],
    stdout=PIPE,
)
q = Queue()
t = Thread(target=enqueue_output, args=(p.stdout, q))
t.daemon = True
t.start()


fig, ax = plt.subplots()
ax.axis([0, 1500, 0, 1900])


ani = animation.FuncAnimation(fig, plot_coord, interval=200)
plt.show()
