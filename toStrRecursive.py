def toStr(number, base):
    basenum = '0123456789ABCDEF'

    if number < base:
        return basenum[number]

    return toStr(number//base, base) + basenum[number%base]

if __name__ == "__main__":
    print toStr(1453,16)
