import subprocess
import time

def start_backend():
    print("Running Backend ...")
    subprocess.Popen(['python3.10', 'models/base_model.py']) #The backend file in which we will initiate running/starting it
    subprocess.Popen(['python3.10', 'models/user.py'])
    subprocess.Popen(['python3.10', 'models/location.py'])
    subprocess.Popen(['python3.10', 'models/product.py'])
    subprocess.Popen(['python3.10', 'test_base_model.py'])
    print("-----NO BUGS FOUND IN THE BACKEND-----")
"""
def start_frontend():
    subprocess.Popen(['npm', 'start'], cwd='frontend_path_directory')  # Which command should we use to start frontend directory?
"""
if __name__ == "__main__":
    start_backend()
    #time.sleep(5)  # Delay for how long the backend will start. We will adjust in time
   # start_frontend()

