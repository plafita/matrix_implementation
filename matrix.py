import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        if self.h == 1:
            return self[0][0]
        
        if self.h == 2:
            return self.g[0][0]*self.g[1][1]-self.g[1][0]*self.g[0][1]


    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        return sum(self[i][i] for i in range(self.h))


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.w == 1:
            inverse = [[0]]
            inverse.g[0][0] = (1/self.g[0][0])
                   
        if self.w == 2:
            inverse = [[0,0],[0,0]]
            inverse[0][0] = self.g[1][1]/self.determinant()
            inverse[0][1] = -self.g[0][1]/self.determinant()
            inverse[1][0] = -self.g[1][0]/self.determinant()
            inverse[1][1] = self.g[0][0]/self.determinant()
                   
        return Matrix(inverse)

    def dot_product(self, other, i):
        dot_result = 0
        for j in range(self.w):
            dot_result = self.g[i][j]*other.g[i][j]
        return dot_result
    

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for j in range(self.w):
            new_row = []
            for i in range(self.h):
                new_row.append(self.g[i][j])
            matrix_transpose.append(new_row)
                
            
        return Matrix(matrix_transpose)


    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):

        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        #
        # TODO - your code here
        #
        suma = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            suma.append(row)
        return Matrix(suma)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negative = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append((-1)*self.g[i][j])
            negative.append(row)
        return Matrix(negative)


    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        subs = []
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(self.g[i][j] - other.g[i][j])
            subs.append(new_row)
        return Matrix(subs)


    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if isinstance(other, numbers.Number):
            return other * self

        if self.w != other.h:
            raise(ValueError, "Matrices A and B can only be multiplied if the width of A is equal to the heigh of B")
        else:    
            mul = zeroes(self.h, other.w)
            for j in range(other.w):
                for i in range(self.h):
                    for k in range(self.w):
                        mul[i][j] += self.g[i][k] * other.g[k][j]
   
        return mul


    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        
        if isinstance(other, numbers.Number):
            pass
        
        rmul = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append((other)*self.g[i][j])
            rmul.append(row)
        return Matrix(rmul)

      
 