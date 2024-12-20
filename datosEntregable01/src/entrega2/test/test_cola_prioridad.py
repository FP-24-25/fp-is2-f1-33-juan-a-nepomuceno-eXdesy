'''
Created on 11 nov 2024

@author: Dilyorbek Mukhiddinov
'''

from src.entrega2.tipos.cola_prioridad import Cola_prioridad

def test_cola_prioridad():
    cola = Cola_prioridad[str, int]()
    # Agregar pacientes
    cola.add('Paciente A', 3) # Dolor de cabeza leve
    cola.add('Paciente B', 2) # Fractura en la pierna
    cola.add('Paciente C', 1) # Ataque cardíaco
    # Verificar el estado de la cola
    assert cola.elements() == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto."
    # Atender a los pacientes y verificar el orden de atención
    atencion = []        
    while not cola.is_empty:
        atencion.append(cola.remove())

    assert atencion == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de atención no es correcto."
    
    print("Pruebas superadas exitosamente.")
 
if __name__ == '__main__':
    test_cola_prioridad()