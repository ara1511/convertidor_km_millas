import torch
import torch.nn as nn

class ConversionModel:
    def __init__(self):
        self.modelo = nn.Sequential(nn.Linear(1, 1))
        self.criterio = nn.MSELoss()
        self.optimizador = torch.optim.Adam(self.modelo.parameters(), lr=0.1)
        self.historial = []

    def entrenar(self, x_np, y_np, epochs=1000):
        x_train = torch.tensor(x_np).view(-1, 1)
        y_train = torch.tensor(y_np).view(-1, 1)

        for epoch in range(epochs):
            pred = self.modelo(x_train)
            loss = self.criterio(pred, y_train)
            self.optimizador.zero_grad()
            loss.backward()
            self.optimizador.step()
            self.historial.append(loss.item())

        return self.historial

    def predecir(self, valor):
        entrada = torch.tensor([[valor]], dtype=torch.float32)
        salida = self.modelo(entrada).item()
        return salida
