class PredictorService:
    def __init__(self, modelo):
        self.modelo = modelo

    def convertir_km_a_millas(self, km):
        resultado = self.modelo.predecir(km)
        return round(resultado, 3)
