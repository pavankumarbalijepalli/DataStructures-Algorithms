def reverseString(text):
    index = -1
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = list(text)
    for i in range(len(text)-1, len(text)//2, -1):
        print(text[i].lower())
        if text[i].lower() not in vowels:
            temp = text[i]

            while True:
                index += 1
                if text[index].lower() not in vowels:
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text


if __name__ == '__main__':
    print(reverseString('AiNyNp'))
