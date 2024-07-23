import random

word = ''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for x in range(5):
    word += random.choice(letters)

print(f'Generated word: {word}')
print(f'RULES: \n1° - If the letter is uppercase, its position is correct. \n'
      '2° - If the letter is lowercase, its position is wrong, but the letter is in the word. \n'
      "3° - If it appears as '_', the letter is not in the word. \n")

cont = 0
while(True):
    WordTry = []
    if(cont == 0):
        Try1 = input("Type your first attempt: \n")
        if(word == Try1):
            print("🎉 Congratulations!!! You won!!! 🎉")
            break

        elif(len(Try1)!=5):
            print("🚫 The word must be 5 letters long. Try again! 🚫")
            continue

        else:
            for i in range(5):
                if(Try1[i] == word[i]):
                    WordTry.append(Try1[i].upper())

                elif(Try1[i] in word):
                    WordTry.append(Try1[i])

                else:
                    WordTry.append('_')
            for i in range(5):
                print(WordTry[i], end=' ')
            print()
            WordTry.clear()
            cont += 1
    
    if(cont == 1):
        Try2 = input("Type your second attempt: \n")
        if(word == Try2):
            print("🎉 Congratulations!!! You won!!! 🎉")
            break

        elif(len(Try2)!=5):
            print("🚫 The word must be 5 letters long. Try again! 🚫")
            continue

        else:
            for i in range(5):
                if(Try2[i] == word[i]):
                    WordTry.append(Try2[i].upper())
                    
                elif(Try2[i] in word):
                    WordTry.append(Try2[i])
                
                else:
                    WordTry.append('_')
            for i in range(5):
                print(WordTry[i], end=' ')
            print()
            WordTry.clear()
            cont += 1

    if(cont == 2):
        Try3 = input("Type your third attempt: \n")
        if(word == Try3):
            print("🎉 Congratulations!!! You won!!! 🎉")
            break

        elif(len(Try3)!=5):
            print("🚫 The word must be 5 letters long. Try again! 🚫")
            continue

        else:
            for i in range(5):
                if(Try3[i] == word[i]):
                    WordTry.append(Try3[i].upper())

                elif(Try3[i] in word):
                    WordTry.append(Try3[i])

                else:
                    WordTry.append('_')
            for i in range(5):
                print(WordTry[i], end=' ')
            print()
            WordTry.clear()
            cont += 1
    
    if(cont == 3):
        Try4= input("Type your fourth attempt: \n")
        if(word == Try4):
            print("🎉 Congratulations!!! You won!!! 🎉")
            break

        elif(len(Try4)!=5):
            print("🚫 The word must be 5 letters long. Try again! 🚫")
            continue

        else:
            for i in range(5):
                if(Try4[i] == word[i]):
                    WordTry.append(Try4[i].upper())
                    
                elif(Try4[i] in word):
                    WordTry.append(Try4[i])
                
                else:
                    WordTry.append('_')
            for i in range(5):
                print(WordTry[i], end=' ')
            print()
            WordTry.clear()
            cont += 1

    if(cont == 4):
        Try5 = input("Type your fifth attempt: \n")
        if(word == Try5):
            print("🎉 Congratulations!!! You won!!! 🎉")
            break

        elif(len(Try5)!=5):
            print("🚫 The word must be 5 letters long. Try again! 🚫")
            continue

        else:
            for i in range(5):
                if(Try5[i] == word[i]):
                    WordTry.append(Try5[i].upper())

                elif(Try5[i] in word):
                    WordTry.append(Try5[i])

                else:
                    WordTry.append('_')
            for i in range(5):
                print(WordTry[i], end=' ')
            print()
            WordTry.clear()
            cont += 1

    if(cont == 5):
        print("😔 You lost! 😔")
        break