def lonelyinteger(a):
    i = 0
    while i < len(a):
        anything = a[i]
        seen = 1
        j = i + 1
        while j < len(a):
            if a[j] == anything:
                seen += 1
                del a[j]
            else:
                j += 1
        if seen == 1:
            return anything
        i += 1
