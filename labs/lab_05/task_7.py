def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = "BMSTU"
string2 = "BUTSM"
if are_anagrams(string1, string2):
    print(f'"{string1}" и "{string2}" являются анаграммами.')
else:
    print(f'"{string1}" и "{string2}" не являются анаграммами.')
