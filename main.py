def main():
    try:
        bill_value = float(input("Digite o valor da conta: "))
        percentage = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))
        tip = bill_value * (percentage / 100)
        print(f"Gorjeta: R$ {tip:.2f}")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")


if __name__ == "__main__":
    main()
