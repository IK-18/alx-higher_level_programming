#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    if not roman_string:
        return res
    for i in range(len(roman_string)):
        if roman_string[i] not in list(rom):
            return 0
        if i != 0 and rom[roman_string[i]] > rom[roman_string[i - 1]]:
            continue
        if i != len(roman_string) - 1:
            if rom[roman_string[i]] < rom[roman_string[i + 1]]:
                res += rom[roman_string[i + 1]] - rom[roman_string[i]]
                i = i + 2
                continue
        res += rom[roman_string[i]]
    return res
