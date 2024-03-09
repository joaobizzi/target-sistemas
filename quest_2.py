fib = [0, 1]
num = int(input("Digite um número: "))
while True:
    if num == 1 or num == 0:
        print("Pertence")
        break
    proximo = fib[-1] + fib[-2]
    if proximo == num:
        print("Pertence à Sequência de Fibonacci")
        break
    if num < proximo:
        print("Não pertence à Sequência de Fibonacci")
        break
    fib.append(proximo)