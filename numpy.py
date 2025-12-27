numpy.py
# F=A*(K^0.3)*(L^0.7)
import numpy as np
def production_function(K, L, A):
    return A * (K ** 0.3) * (L ** 0.7)
if __name__ == "__main__":
    K = np.array([10])
    L = np.array([20])
    A = np.array([30])
    print("return:", production_function(K, L, A))
          

  
