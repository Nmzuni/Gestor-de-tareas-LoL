'''Para mejorar la experiencia de usuario, se ha usado colores en formato ANSI. Para su correcta visualización, en Linux y Mac no hay problemas, sin embargo
en Windows, son soportados a partir de Windows update TH2 -> Información extraida de la página web de --Python 3 para principiantes-- '''
'''En mi caso, solo puedo ver los colores a través de la terminal de Visual Studio Code, en cmd no'''

# Por tanto, recomiendo la visualización de la aplicación a través de la terminal de VS Code


class Gestor_Tareas:                                                        #Creación de clase  


    
    def __init__(self, descripcion) :                                       # Creación del contructor
            self.descripcion = descripcion
            self.listaTareas=[]                                             # Creación de lista vacia


            for indice, task in enumerate (self.listaTareas):               # Enumera las tareas para usar números en la interacción
                  print(indice, task)                                       # Se usa en función mostrar_tareas



    def __str__(self):                                                      
            return f'{self.descripcion}'
    


    def agregar_tareas (self):                                               # Método para agregar una nueva tarea a la lista de tareas
            self.descripcion = input('   Escribe la nueva tarea: ')          # Se define el método de entrada de datos para usuario   

            
            if self.descripcion:
                self.listaTareas.append(self.descripcion)                    # La tarea se añade a la lista
                print(f'\033[0;32m\n   La tarea "{self.descripcion}" se ha guardado.\n \033[0m')
            else:
                  print('\033[0;31m \n   La tarea está vacia. Escribe una tarea para guardarla. \n \033[0m')  # Salida si la tarea esta vacia


            print('\n')

            


        
    def mostrar_tareas (self):


        if self.listaTareas:
            print('\n   LA LISTA DE TAREAS ES:\n')                                              
            for indice, task in enumerate(self.listaTareas):            # muestra el número de la tarea + tarea
                print(f'   {indice + 1}.{task}')                         # como python empieza por 0, le añado +1 al índice
        else:  
            print('   No hay tareas')                                      # Salida si no hay tareas



        print('\n') 

        print('\033[0;33m   ---FIN DEL LISTADO DE TAREAS---\033[0m')  

        print('\n')          


           
        
    def tarea_completada (self):
            
            print('\033[0;35m   Observa la lista para ver el número de tarea a completar:\033[0m') 


            self.mostrar_tareas()          # Para que el usuario no tenga que volver a imprimir la lista llamamos a la función mostrar tareas




            while True:                                           
                self.completada = int(input('   Escribe el número de la tarea para completarla: '))
                if self.completada >0 and self.completada <= len(self.listaTareas):    # si la tarea se encuentra entre 0 y la longitud de la lista


                    if '(\033[0;32mCOMPLETADA\033[0m) - ' in self.listaTareas[self.completada - 1]:           # si la tarea esta completada, tiene que coger índice -1
                                                                                                              # porque python cuenta desde 0
                       
                        print('\033[0;31m\n   La tarea ya está como COMPLETADA. Seleccione otra.\033[0m')     

                        print('\033[0;33m\n ¡CUIDADO!\033[0m: si tienes todas las tareas completadas pulsa 0. Si ha sido un error continua completando tareas. ')

                    else: 
                        self.listaTareas[self.completada -1] = '(\033[0;32mCOMPLETADA\033[0m) - ' + self.listaTareas[self.completada -1]   
                        print(f'\033[0;32m\n   Se marcó la tarea {self.completada} como completada:\n \033[0m')      # Salida si para la nueva tarea completada
                        break


                elif self.completada == 0:                                                                           # He añadido este elif porque haciendo pruebas
                     break                                                                                           # me he quedado encerrada en el bucle con   
                      
                                                                                                                     # todas las actividades completadas
                else:
                    print('\033[0;31m\n   Número de tarea no valido. Vuelva a ver la lista de tareas (Pulsa 3):\033[0m')


                    print('\033[0;33m\n ¡CUIDADO!\033[0m: si tienes todas las tareas completadas pulsa 0. Si ha sido un error continua completando tareas.\033[0m')
                    

                print('\n')

            self.mostrar_tareas()          # Se vuelve a mostrar la lista de tareas 





    def eliminar_tarea (self):


        if self.listaTareas:

            print('\033[0;35m   Observa la lista para ver el número de tarea a eliminar:\033[0m')                                                               
            self.mostrar_tareas()            

            
            while True:                                                                           
                self.descripcion = int(input('\n   Introduce el número de la tarea a eliminar: '))    
                                                                                                  # que la lista contenga los datos que introducimos
                                                                                                  # en el input sin que sea menor que 0 ni mayor   
                if self.descripcion <= 0 or self.descripcion > len(self.listaTareas):             # que el tamaño de la lista

                    print('\033[0;31m\n   No se encuentra el número dentro de la lista.\033[0m')   


                else:
                    del self.listaTareas [self.descripcion - 1]                             # si la opción en válida se elimina

                    print('\033[0;32m\n   La tarea ha sido eliminada\033[0m')       

                    break    


        else:                                                                                   
            print('No hay tareas.')

        print('\n')   

          
                
            

tarea = Gestor_Tareas('')  

#_______________________________________________________INTERFAZ USUARIO________________________________________________________________#

# Bucle principal
while True:

    # MENÚ DE USUARIO
    print('\033[1;37;45m' + '\n    ***---GESTOR DE TAREAS LoL---***   \n' + '\033[0m')

    print('\033[1m' + '\n       --- MENÚ PRINCIPAL ---' + '\033[0m')

    print('\n')
    

    print('\033[0;30;47m')

    print('   1. Añadir nueva tarea               ')       # Los espacios con por estética para ANSI
    print('   2. Marcar tarea como completada     ')
    print('   3. Mostrar todas las tareas         ')
    print('   4. Eliminar una tarea               ')
    print('   0. Salir                            ')

    print('\033[0m')

    print('\033[1;33m\n Desarrollado por Natalia Macías Zambrano\033[')

    print('\n')

    # Llamadas a las funciones para ejecutar los métodos a través de la entrada de números
         
    
    try:
        seleccionaOpcion = int(input('\033[0;36m   Selecciona una opción del menú: \033[0;m'))
        print('\n')

        if seleccionaOpcion == 1:
            tarea.agregar_tareas()
        elif seleccionaOpcion == 2:
            tarea.tarea_completada()    
        elif seleccionaOpcion == 3:
            tarea.mostrar_tareas()   
        elif seleccionaOpcion == 4:
            tarea.eliminar_tarea()    
        elif seleccionaOpcion == 0:
            print('Gracias por usar el software de LoL. Cerrando programa...') 
            print('\n') 
            break     
        else:
            print(f'Número de menú no válido, por favor, {seleccionaOpcion}') 

    except ValueError:
         print('\033[0;31m   \n   Entrada incorrecta, por favor, introduce un número.\n \033[0m')
        
    
