FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(num):
    str_num = str(num)
    length = len(str_num)

    def get_dozen(str_num):
        if str_num.startswith('1'):
            return SECOND_TEN[int(str_num[1])]
        elif not int(str_num):
            return ''
        elif str_num.endswith('0'):
            return OTHER_TENS[int(str_num[0])-2]
        else:
            return '%s %s' % (OTHER_TENS[int(str_num[0])-2], FIRST_TEN[int(str_num[1])-1])

    if length == 1:
        return FIRST_TEN[num-1]
    elif length == 2:
        return get_dozen(str_num)
    elif length == 3:
        return "%s %s %s" % (FIRST_TEN[int(str_num[0])-1], HUNDRED, get_dozen(str_num[1:]))
    else:
        return -1


if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"

