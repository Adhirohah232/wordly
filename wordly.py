import random
import re

print("🙏WELCOME🙏, to WORDLY❤️")
limit = int(input('enter question limit: '))
sum = 0
for i in range(limit):  # Use range(limit) instead of limit
  terms = {}
  with open('./words.txt', 'r', encoding='utf-8') as file:
    result = file.readlines()

  for line in result:
    if '. ' in line:
      serial, definition = line.split('. ')
      term, meaning = definition.split(': ')
      terms[term.strip()] = meaning.strip()

# below 2 func are for ques
  def get_random_word(terms):
    keys = list(terms.keys())
    random.shuffle(keys)
    random_index = random.randint(0, len(keys) - 1)
    return keys[random_index]
  
  def get_randomanyword_fromvalues(terms):
    anyword = random.choice(list(terms.values()))
    anyword_arr = anyword.split(', ')
    random_ind = random.randint(0, len(anyword_arr) - 1)
    result = anyword_arr[random_ind]
    if '(' in result and ')' in result:
      result = re.sub(r'\([^)]*\)', '', result)
    return result

  askword = get_random_word(terms)
  askword2 = get_randomanyword_fromvalues(terms)
  def get_askword():
    ask_arr = [askword, askword2]
    random_word = random.randint(0, len(ask_arr)-1)
    return ask_arr[random_word]

  getaskword = get_askword()
  askword_keys = list(terms.keys())

  # print(getaskword)

  def get_anyword_forchoice2(terms):
    anyword = random.choice(list(terms.values()))
    anyword_arr = anyword.split(', ')
    random_ind = random.randint(0, len(anyword_arr) - 1)
    result = anyword_arr[random_ind]
    if '(' in result and ')' in result:
      result = re.sub(r'\([^)]*\)', '', result)
    return result

  def get_anyword_forchoice3(terms):
    anyword = random.choice(list(terms.values()))
    anyword_arr = anyword.split(', ')
    random_ind = random.randint(0, len(anyword_arr) - 1)
    result = anyword_arr[random_ind]
    if '(' in result and ')' in result:
      result = re.sub(r'\([^)]*\)', '', result)
    return result

  def get_anyword_forchoice4(terms):
    anyword = random.choice(list(terms.values()))
    anyword_arr = anyword.split(', ')
    random_ind = random.randint(0, len(anyword_arr) - 1)
    result = anyword_arr[random_ind]
    if '(' in result and ')' in result:
      result = re.sub(r'\([^)]*\)', '', result)
    return result

  


  print('.................................')
  print(f'{i+1}) choose the correct synonym/alternative of: {getaskword.upper()}')
  answord = terms[askword]

  if '(' in answord and ')' in answord:
    answord = re.sub(r'\([^)]*\)', '', answord)

  if(getaskword in askword_keys):
    answord_arr = answord.split(', ')
    random_ind = random.randint(0, len(answord_arr) - 1)
    choice1 = answord_arr[random_ind]
    choice2 = get_anyword_forchoice2(terms)
    choice3 = get_anyword_forchoice3(terms)
    choice4 = get_anyword_forchoice4(terms)

    print('your choices: ')
    user_choices = [choice1, choice2, choice3, choice4]
    random.shuffle(user_choices)

    for i in range(4):
        print(f'{i+1}. {user_choices[i]}')

    user_inpt = int(input('your ans: '))
    if user_inpt < 1 or user_inpt > 4:
        print('Invalid choice. Please choose a number between 1 and 4.')
        continue

    if user_choices[user_inpt - 1] in answord_arr:
        sum = sum + 1
        print('CORRECT!!😊')
        print('.................................\n')
    else:
        commn_ele = set(user_choices) & set(answord_arr)
        result = list(commn_ele)
        print(f'INCORRECT🥲, correct synonym: {result[0]}\n')
        print('.................................\n')
  else:
    def remove_content_inside_parentheses(text):
      return re.sub(r'\([^)]*\)', '', text)

    def remove_content_in_dict(terms):
      cleaned_terms = {}
      for key, value in terms.items():
          cleaned_value = remove_content_inside_parentheses(value)
          cleaned_terms[key] = cleaned_value.strip()
      return cleaned_terms

    clearedparan_terms = remove_content_in_dict(terms)
    print('asking from value-check phase')
    target_value = getaskword
    answord = next(key for key, value in clearedparan_terms.items() if target_value in value)

    choice1 = next(key for key, value in clearedparan_terms.items() if target_value in value)
    choice2 = get_anyword_forchoice2(terms)
    choice3 = get_anyword_forchoice3(terms)
    choice4 = get_anyword_forchoice4(terms)

    print('your choices: ')
    user_choices = [choice1, choice2, choice3, choice4]
    random.shuffle(user_choices)    

    for i in range(4):
        print(f'{i+1}. {user_choices[i]}')

    user_inpt = int(input('your ans: '))
    if user_inpt < 1 or user_inpt > 4:
        print('Invalid choice. Please choose a number between 1 and 4.')
        continue

    if user_choices[user_inpt - 1]==answord:
      sum = sum + 1
      print('CORRECT!!😊')
      print('.................................\n')
    else:
      print(f'INCORRECT🥲\n')
      
    






if (limit == 1):
    if (sum == limit):
        print('🎉🎉congrats, champion🎉🎉')
        print('you got it right😊')
    else:
        print('sorry😔, need to practise')
else:
    print(f'score: {sum}/{limit}')
    if (sum == limit):
        print('🎉🎉congrats, champion🎉🎉')
        print('you got all of them correct😊')
    elif (sum >= limit / 2):
        print('you did well👍')
    else:
        print('you need to practice more😔')



















#  just in case, if the above code doesn't work, use 👇


# import random
# import re
# print("🙏WELCOME🙏, to WORDLY❤️")
# limit = int(input('enter question limit: '))
# for i in range(limit):  # Use range(limit) instead of limit
#     terms = {}
#     with open('./words.txt', 'r', encoding='utf-8') as file:
#         result = file.readlines()

#     for line in result:
#         serial, definition = line.split('. ')
#         term, meaning = definition.split(': ')
#         terms[term.strip()] = meaning.strip()

#     def get_random_word(terms):
#         keys = list(terms.keys())
#         random_index = random.randint(0, len(keys) - 1)
#         return keys[random_index]

#     def get_anyword_forchoice2(terms):
#         anyword = random.choice(list(terms.values()))
#         anyword_arr = anyword.split(', ')
#         random_ind = random.randint(0, len(anyword_arr)-1)
#         result = anyword_arr[random_ind]
#         if '(' in  result and ')' in result:
#             result = re.sub(r'\([^)]*\)', '', result)
#         return result

#     def get_anyword_forchoice3(terms):
#         anyword = random.choice(list(terms.values()))
#         anyword_arr = anyword.split(', ')
#         random_ind = random.randint(0, len(anyword_arr)-1)
#         result = anyword_arr[random_ind]
#         if '(' in  result and ')' in result:
#             result = re.sub(r'\([^)]*\)', '', result)
#         return result

#     def get_anyword_forchoice4(terms):
#         anyword = random.choice(list(terms.values()))
#         anyword_arr = anyword.split(', ')
#         random_ind = random.randint(0, len(anyword_arr)-1)
#         result = anyword_arr[random_ind]
#         if '(' in  result and ')' in result:
#             result = re.sub(r'\([^)]*\)', '', result)
#         return result

#     askword = get_random_word(terms)
#     print('.................................')
#     print(f'choose the correct synonym/alternative of: {askword.upper()}')
#     answord = terms[askword]

#     if '(' in  answord and ')' in answord:
#         answord = re.sub(r'\([^)]*\)', '', answord)

#     answord_arr = answord.split(', ')
#     random_ind = random.randint(0, len(answord_arr)-1)
#     choice1 = answord_arr[random_ind]
#     choice2 = get_anyword_forchoice2(terms)
#     choice3 = get_anyword_forchoice3(terms)
#     choice4 = get_anyword_forchoice4(terms)

#     print('your choices: ')
#     user_choices = [choice1, choice2, choice3, choice4]
#     random.shuffle(user_choices)

#     for i in range(4):
#         print(f'{i+1}. {user_choices[i]}')

#     user_inpt = int(input('your ans: '))
#     if user_inpt < 1 or user_inpt > 4:
#         print('Invalid choice. Please choose a number between 1 and 4.')
#         continue

#     if user_choices[user_inpt-1] in answord_arr:
#         print('CORRECT!!😊')
#         print('.................................\n')
#     else:
#         commn_ele = set(user_choices) & set(answord_arr)
#         result = list(commn_ele)
#         print(f'INCORRECT🥲, correct synonym: {result[0]}\n')
#         print('.................................\n')






