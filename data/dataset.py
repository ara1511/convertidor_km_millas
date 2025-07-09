import numpy as np

class Dataset:
    def __init__(self):
        self.km = np.array([0, 1, 2, 3, 5, 10, 20, 30, 50, 100], dtype=np.float32)
        self.millas = np.array([0, 0.621, 1.242, 1.864, 3.107, 6.213, 12.427, 18.641, 31.069, 62.137], dtype=np.float32)

    def get_data(self):
        return self.km, self.millas
