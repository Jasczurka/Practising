string = " " + input()
palindromes = [string[i:j + 1] for i in range(1, len(string)) for j in range(i, len(string)) if string[i:j + 1] == string[j:i - 1:-1]]
print(palindromes)
