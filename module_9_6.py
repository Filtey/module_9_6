def all_variants(text):
    for val in range(len(text)):
        for val2 in range(val + 1, len(text) + 1):
            yield text[val:val2]

a = all_variants("abc")
for i in a:
    print(i)
