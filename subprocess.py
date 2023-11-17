import subprocess
import time

def start_backend():
    subprocess.Popen(['python', 'backend.py']) #The backend file in which we will initiate running/starting it

def start_frontend():
    subprocess.Popen(['npm', 'start'], cwd='frontend_path_directory')  # Which command should we use to start frontend directory?

if __name__ == "__main__":
    start_backend()
    time.sleep(5)  # Delay for how long the backend will start. We will adjust in time
    start_frontend()

