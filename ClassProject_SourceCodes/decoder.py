
def base26(number):

    digit_converter = lambda x: chr(ord("A")+x)

    if number < 0:
        return "-" + base26(-number)
    (d,m) = divmod(number,26)
    if d > 0:
        return base26(d) + digit_converter(m)
    return  digit_converter(m)


def decoder(string):

    result = 0
    digit_decoder = lambda x: ord(x)-ord("A")

    for i,e in enumerate(reversed(string)):
        result+=digit_decoder(e)*26**i

    return result

#print(base26(25))
print(decoder("JOSYBK"))
