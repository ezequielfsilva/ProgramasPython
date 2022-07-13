"""Programa que calcula multa para velocidades acima de 80KM/H"""
velocidade = int(input("Digite qual a velocidade do seu carro em KM/H: "))
multa = (velocidade - 80)*7
if velocidade > 80:
    print("\033[1;31mMULTADO!\033[m")
    print("\033[1;32mVocê excedeu o limite de velocidade que é de 80KM por H.\033[m")
    print("\033[1;33mVocê deve pagar uma multa de R${:.2f}.\033[m".format(multa))

print("Tenha um bom dia! Dirija com segurança!")
