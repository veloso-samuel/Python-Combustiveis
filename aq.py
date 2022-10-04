programa = int(input("Para cálculo gasolina vs alcool digite 1, \nPara cálculo  de viagem digite 2. \n" ))

while programa > 2 or programa < 1:
        programa = int(input("Para cálculo gasolina vs Alcool digite 1, \nPara cálculo  de viagem digite 2. \n" ))

if programa == 1:
    valor_alcool = float(input("digite valor do álcool: "))
    valor_gasolina = float(input("digite valor da gasolina: "))

    melhor_opcao = valor_alcool / valor_gasolina
    melhor_opcao = "Abasteça com álcool" if melhor_opcao <= 0.7 else "Abasteça com gasolina"
    print(melhor_opcao)
    
elif programa == 2:
    distancia_viagem = float(input("Distância de Viagem em KM: "))
    preco_combustivel = float(input("Preço do combustível: "))
    print("ATENÇÃO: Alcool e Gasolina tem KM/L diferentes")
    km_litro = float(input("KM que o veículo faz por litro: "))

    custo_viagem = (distancia_viagem / km_litro) * preco_combustivel
    custo_km = preco_combustivel / km_litro
    
    print(f"O custo da viagem será: R${custo_viagem} \nMédia de R${custo_km} por litro")
