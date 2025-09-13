class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        # Mapping of integers to Roman numerals
        value = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4,
               1]
        symbol = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV",
               "I"]

        num = self.number
        roman_num = ""
        i = 0
        while num > 0:
            for _ in range(num // value[i]):
                roman_num += symbol[i]
                num -= value[i]
            i += 1
        return roman_num


# Example usage
n = int(input("Enter an integer: "))
converter = RomanConverter(n)
print("Roman number:", converter.to_roman())
