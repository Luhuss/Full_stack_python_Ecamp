import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.Supervisor import Supervisor

class SupervisorService:
    
    def __init__(self):
        self._supervisor = self.load_supervisor()
        
    def load_supervisor(self):
        try:
            with open('supervisor.csv', 'r') as file:
                supervisor = file.readlines()
        except FileNotFoundError:
            supervisor = []
            with open('supervisor.csv', 'w') as file:
                file.writelines(supervisor)
        return supervisor
    
    def save_supervisor(self):
        with open('supervisor.csv', 'w') as file:
            for i in self._supervisor:
                file.write(str(i))
    

    def crear_supervisor(self):
        nombre    = input('Ingrese el nombre del supervisor: ')
        apellido  = input('Ingrese el apellido del supervisor: ')
        rut       = input('Ingrese el rut del supervisor: ')
        area      = input('Ingrese el área del supervisor: ')
        
        supervisor = Supervisor(nombre, apellido, rut, area)
        print(supervisor)
        
        self._supervisor.append(supervisor)
        
        self.save_supervisor()