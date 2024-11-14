words = []
length = []

for user in range(10):
    i = input("Enter a word: ")
    words.append(i)
    if any(char.isdigit() for char in i):
        print("Error!,Please enter a valid word.")

lengthinput = int(input("Enter the number of letters: "))        
    
for word in words:
    if len(word) == lengthinput:
        length.append(word)   
    else:
        continue
print(f"Here are the following words that have {lengthinput} letters:{length}")   
      