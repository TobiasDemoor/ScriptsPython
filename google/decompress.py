def decompress(inpt: str) -> str:
    subinpt = inpt[:]
    res = ""

    while '[' in subinpt:
        a, b = 0, subinpt.index('[')

        while (not subinpt[a:b].isnumeric()) and (a < b):
            res += subinpt[a]
            a += 1

        if a < b:
            n = int(subinpt[a:b])
            c = subinpt.index(']')
            i = 0

            while subinpt.count('[', b+1, c) > i:
                c = subinpt.index(']', c+1)
                i += 1

            res += n*decompress(subinpt[b+1:c])
            subinpt = subinpt[c+1:]
        else:
            raise Exception('BadFormat')

    return res + subinpt

assert decompress("hola") == "hola"
assert decompress("3[a]") == "aaa"
assert decompress("3[2[ab]]") == "abababababab"
assert decompress('a10[b]') == "abbbbbbbbbb"
assert decompress("3[abc]4[ab]c") == "abcabcabcababababc"
