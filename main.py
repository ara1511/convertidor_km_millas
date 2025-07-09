from data.dataset import Dataset
from model.modelo import ConversionModel
from services.predictor import PredictorService
from utils.visualizer import Visualizer

def main():
    dataset = Dataset()
    km, millas = dataset.get_data()

    modelo = ConversionModel()
    historial = modelo.entrenar(km, millas)

    Visualizer.mostrar_entrenamiento(historial)

    predictor = PredictorService(modelo)

    print("\n🚗 Conversor de kilómetros a millas (usando red neuronal)")
    while True:
        try:
            entrada = input("\nIngresá una cantidad de kilómetros (o escribí 'salir' para terminar): ")
            if entrada.lower() == 'salir':
                print("Gracias por usar el conversor. 👋")
                break
            km_valor = float(entrada)
            resultado = predictor.convertir_km_a_millas(km_valor)
            print(f"{km_valor} km son aproximadamente {resultado} millas.")
        except ValueError:
            print("⚠️ Por favor ingresá un número válido.")

if __name__ == "__main__":
    main()
