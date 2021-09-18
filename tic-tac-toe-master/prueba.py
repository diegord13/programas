import numpy as np
def print_board(self):
    for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

    #@staticmethod  
def print_board_nums():
        # 0 | 1 | 2
    #number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    #print(number_board)
    #for row in number_board:
    #    print('| ' + ' | '.join(row) + ' |')

    array1=np.arange(9).reshape(3,3)
    array1 = array1*0
    for a in range(0,3):
        for b in range (0,3):
            
            array = array1
            if array[a,b] == 0:
                print('escoja posicion')

    print(array)
    #print(array1[0,0])


def make_board():
    return [' ' for _ in range(9)]

 #   def print_board(self):
    for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

#print_board_nums()

"""

"""

class Player():
    def __init__(self, letter):
        self.letter = letter



class perro():

  def __init__(self, nombre, size, raza):
      self.nombre=nombre
      self.size=size
      self.raza=raza

  def ladra(self):

    s=""
    for l in self.nombre:
        s+="wof"
    print(s)


#chucho=perro("chucho","grande","husky")
#chucho.ladra()

#wofwofwofwofwofwof

#cloe=perro("cloe","mini","chihuahua")
#cloe.ladra()


class alumno:

    def __init__(self, nombre, nota_alumno):
        self.nombre = nombre
        self.nota_alumno = nota_alumno
    
    def resultado(self):
        if self.nota_alumno > 5:
            print('El estudiante {}, saco nota {} pasando la materia'.format(self.nombre,self.nota_alumno))
        else:
            print('El estudiante {} , saco nota {} perdiendo la materia'.format(self.nombre,self.nota_alumno))



estudiante = alumno('diego',7)
estudiante.resultado()