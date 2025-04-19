
RUS = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
ENG = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rus = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
space = [' ']

def encryption (text_before, key, text_after):
  for i in range(len(text_before)):
    if text_before[i] in eng:
      letter = eng.index(text_before[i])
      text_after = text_after + eng[(letter + key) % 26]
    elif text_before[i] in RUS:
        letter = RUS.index(text_before[i])
        text_after = text_after + RUS[(letter + key) % 33]
    elif text_before[i] in rus:
       letter = rus.index(text_before[i])
       text_after = text_after + rus[(letter + key) % 33]
    elif text_before[i] in ENG:
        letter = ENG.index(text_before[i])
        text_after = text_after + ENG[(letter + key) % 26]
    elif text_before[i] in space:
      text_after = text_after + ' '

  return text_after

def decryption (text_before, key, text_after):
  for i in range(len(text_before)):
    if text_before[i] in eng:
      letter = eng.index(text_before[i])
      text_after = text_after + eng[(letter - key) % 26]
    elif text_before[i] in RUS:
        letter = RUS.index(text_before[i])
        text_after = text_after + RUS[(letter - key) % 33]
    elif text_before[i] in rus:
       letter = rus.index(text_before[i])
       text_after = text_after + rus[(letter - key) % 33]
    elif text_before[i] in ENG:
        letter = ENG.index(text_before[i])
        text_after = text_after + ENG[(letter - key) % 26]
    elif text_before[i] in space:
      text_after = text_after + ' '

  return text_after

text_after = ''
message = input('HI CHUMBA\n What do you want to do?\n Feature sheet:\n 1. encode \n 2. decode \n please choose one number(1 or 2):\n')
text_before = input('Type your message, please:\n')
key = int(input('Type your key for coding: '))
while key < 0:
    key = int(input('PLEASE DONT SPOIL MY WORK! AND GIVE ME POSITIVE NUMBER: \n'))
if message=='1':
   print("Wait program will encode your new message is")
   Result_encode = encryption (text_before, key, text_after)
   print(Result_encode)
elif message=='2':
   print("Wait program will decode your message\n your new message is:")
   Result_decode = decryption (text_before, key, text_after)
   print(Result_decode)
else: 
  print("IF YOU, FOOLISH HUMAN, THINK THAT YOU CAN AVOID CHOICE, YOU MADE A MISTAKE! \n")
  print("refusal to choose is also a choice\n your new message is:")
  Result_encode = encryption (text_before, key, text_after)
  print(Result_encode)