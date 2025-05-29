text = input("Pls Enter String: ")


n = len(text)


for length in [2, 3, 4, 5]:
    print(f"\nThe Sub{length}:")
    for i in range(n - length + 1):
        substr = text[i:i+length]
        print(substr)
