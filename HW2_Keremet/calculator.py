def main():
    equation=input('ВВЕДИТЕ: ').split()
    a=float(equation[0])
    b=float(equation[2])
    symbol=equation[1]
    if symbol == "+":
        print(add(a,b))
    elif symbol == "-":
        print(subtract(a,b))
    elif symbol == "*":
            print(multiply(a,b))
    elif symbol == "/":
            print(divide(a,b))
    else:
        print("Неверно выбрана математическая операция (поддерживается: +,-,*./). Попробуйте снова.")
    
if __name__ == "__main__":
    main()    