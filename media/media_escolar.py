def media(*notas):
    
    if not notas:
        return 0
    return sum(notas) / len(notas)

if __name__ == "__main__":
    try:
        print("\n" + "_-" * 25)
        nome = input("\nDigite o nome do aluno: ")
        notas = []
        
        while True:
            nota = input("Digite a nota (ou 'sair' para encerrar): ")
            if nota.lower() == 'sair':
                break
            try:
                notas.append(float(nota))
            except ValueError:
                print("Nota inválida. Tente novamente.")
        
        media_final = media(*notas)
        print(f"\n{'*' * 50}")
        print(f"A média final de {nome} é: {media_final:.2f}")
    except Exception as e:
        print(e)
