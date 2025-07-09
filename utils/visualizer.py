import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def mostrar_entrenamiento(historial):
        plt.plot(historial)
        plt.xlabel("Épocas")
        plt.ylabel("Pérdida")
        plt.title("Entrenamiento con PyTorch")
        plt.grid()
        plt.show()
