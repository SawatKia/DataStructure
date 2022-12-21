class translator:

    def deciToRoman(self, num):
        rules = (
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("XXX", 30),
            ("XX", 20),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        )
        res = ""
        for suf, val in rules:
            while num >= val:
                num -= val
                res += suf
        return res
    def romanToDeci(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in roman:
                num += roman[s[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[s[i]]
                i += 1
        return num
num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))