import os
import time
import psutil


def kill_process(name: str):
    for process in psutil.process_iter():
        if process.name() == name:
            process.kill()


kill_process('omp-server.exe')
os.startfile('omp-server.exe')
time.sleep(999999)
