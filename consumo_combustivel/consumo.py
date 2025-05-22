def calcular_consumo_medio(distancia, combustivel):

    if combustivel <= 0:
        raise ValueError("A quantidade de combustível deve ser maior que zero.")
    if distancia <= 0:
        raise ValueError("A distância deve ser maior que zero.")
    return distancia / combustivel

if __name__ == "__main__":
    try:
        print("\n" + "_-" * 25)
        distancia = float(input("Digite a distância percorrida (em km): "))
        combustivel = float(input("Digite a quantidade de combustível consumido (em litros): "))
        
        consumo_medio = calcular_consumo_medio(distancia, combustivel)
        print(f"\n{'*' * 50}")
        print(f"O consumo médio do veículo é: {consumo_medio:.2f} km/l")
    except ValueError as e:
        print(e)
