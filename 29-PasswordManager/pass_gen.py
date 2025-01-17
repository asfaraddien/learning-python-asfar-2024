#Password Generator Project
import random
def go():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)

  nr_numbers = random.randint(2, 4)
  # for char in range(nr_letters):
  #   password_list.append(random.choice(letters))

  lett = [random.choice(letters) for char in range(nr_letters)]
  # for char in range(nr_symbols):
  #   password_list += random.choice(symbols)


  sym = [random.choice(symbols) for char1 in range(nr_symbols)]
  # for char in range(nr_numbers):
  #   password_list += random.choice(numbers)

  num = [random.choice(numbers) for char2 in range(nr_numbers)]

  password_list = lett + sym + num

  random.shuffle(password_list)

  # password = ""
  # for char in password_list:
  #   password += char
  password = "".join(password_list)
  return password




