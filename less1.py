def strcounter(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter+=1
        print(sym, counter)

def strncounter(s):
    sym_dict = {}
    for sym in s:
        sym_dict[sym] = sym_dict.get(sym, 0) + 1
    for sym, count in sym_dict.items():
        print(sym, count)
strncounter('looooooooooooooh')
strcounter('hello')










