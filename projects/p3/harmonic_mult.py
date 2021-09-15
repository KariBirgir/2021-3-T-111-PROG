PROMPT = '(h)armonic, (m)ultiplication or (q)uit: '
DECIMAL_DIGITS = 4

harmonic_or_mult = input(PROMPT)
while harmonic_or_mult != 'q':

    if harmonic_or_mult == 'h':
        series_length = int(input("Series length: "))
        series_sum = 0
        for i in range(1, series_length+1):
            element = 1/i
            series_sum += element
            print(round(element, DECIMAL_DIGITS))
        print('Sum of series:', round(series_sum, DECIMAL_DIGITS))

    elif harmonic_or_mult == 'm':
        first_int = int(input("First integer: "))
        second_int = int(input("Second integer: "))

        product = 0
        while second_int > 0:
            if second_int % 2 == 1: 
                product += first_int
            print(first_int, second_int)
            first_int = first_int * 2
            second_int = second_int // 2

        print('Product:', product)
    else:
        print('Illegal choice!')

    harmonic_or_mult = input(PROMPT)

