# Variant 7

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.imag)
    __repr__ = __str__


class ComplexCalc:

    def add(self, c1, c2):  # складання
        real = c1.real + c2.real
        imag = c1.imag + c2.imag
        return Complex(real, imag)

    def sub(self, c1, c2):  # віднімання
        real = c1.real - c2.real
        imag = c1.imag - c2.imag
        return Complex(real, imag)

    def mul(self, c1, c2):  # множення
        real = c1.real * c2.real - c1.imag * c2.imag
        imag = c1.imag * c2.real + c1.real * c2.imag
        return Complex(real, imag)

    def div(self, c1, c2):  # ділення
        real = (c1.real * c2.real + c1.imag * c2.imag) / (c2.real ** 2 + c2.imag ** 2)
        imag = (c2.real * c1.imag - c1.real * c2.imag) / (c2.real ** 2 + c2.imag ** 2)
        return Complex(real, imag)

    def abs(self, c):  # абсолютне значення
        return (c.real ** 2 + c.imag ** 2) ** 0.5


calc = ComplexCalc()

print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Absolute")
#
while True:
    # введення чисел
    choice = input("Enter choice (1, 2, 3, 4, 5):")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Введіть дійсне число першого виразу:"))
        num2 = float(input("Введіть уявне число першого виразу:"))
        num3 = float(input("Введіть дійсне число другого виразу:"))
        num4 = float(input("Введіть уявне число другого виразу:"))

        if choice == '1':
            print(calc.add(Complex(num1, num2), Complex(num3, num4)))

        elif choice == '2':
            print(calc.sub(Complex(num1, num2), Complex(num3, num4)))

        elif choice == '3':
            print(calc.mul(Complex(num1, num2), Complex(num3, num4)))

        elif choice == '4':
            print(calc.div(Complex(num1, num2), Complex(num3, num4)))

        elif choice == '5':
            print('перший вираз - ', calc.abs(Complex(num1, num2)))
            print('другий вираз - ', calc.abs(Complex(num3, num4)))
    s = 'n'
    answer = input("Продовжити обчислення? y or n:\n")
    if answer in s:
        print('вихід')
        quit()
    else:
         continue

if __name__ != "__main__":
    main()
