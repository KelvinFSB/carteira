def calcular_juros_compostos(valor_principal, tempo_meses):
    taxa_mensal = 0.02
    juros_compostos = valor_principal * (1 + taxa_mensal) ** tempo_meses
    juros_compostos /= tempo_meses #valor que terei que pagar mesnalente

    return juros_compostos


