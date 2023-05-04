text= input("enter text here: ")
letters= []

text= text.lower()
letters.append(input("Enter the first letter:"))
letters.append(input("Enter the second letter:"))
letters.append(input("Enter the third letter:"))

print("\n")
print("LETTER REPETITIONS:")

letter_repetiton1= text.count(letters[0])
letter_repetiton2= text.count(letters[1])
letter_repetiton3= text.count(letters[2])

print(f" We have found the letter '{letters[0]}' repeated {letter_repetiton1} times")
print(f" We have found the letter '{letters[1]}' repeated {letter_repetiton2} times")
print(f" We have found the letter '{letters[2]}' repeated {letter_repetiton3} times")



print("\n")
print("Number of words:")
    
words_list = text.split()
num_words = len(words_list)
print(f"we have found {num_words} words in your text")


print("\n")
print("the first and last letters of the text are: ")

first_letter=text[0]
last_letter= text[-1]

print(f"the first letter of your text is '{first_letter}' and the last letter is '{last_letter}' ") 



print("\n")
print("Inverted text:  ")

words= text.split()
words.reverse()
invert_text = '  '.join(words)

print(f"If we order your text backwards it will say '{invert_text}'  ")

print("\n")
print("FINALLY! LOOKING FOR THE WORD PYTHON! ")


is_python= 'python' in text
dic= {True: "was", False: "was not"}

print(f" The word 'Python' {dic[is_python]} found in the text")