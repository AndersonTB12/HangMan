import random
from stages import stages
from wordlist import words
from logo import logo

print(f"{logo}\n")

lives = 6 # Número de Vidas que o jogador começa


secret_list = [] # Lista para colocar a palavra em _
chosen_word = random.choice(words) # Escolhe aleatoriamente uma palavra da lista
for i in range(0, len(chosen_word)):
  secret_list.append("_") # Coloca a palavra em 'segredo'


while '_' in secret_list:

  
  print(stages[7 - (lives + 1)])
  print(" ".join(secret_list))
  user_guess = input("\nGuess a letter: ").lower() # Transforma o input do usuário em minúsculo
  
  if user_guess in secret_list:
    print(f"\nYou have already digited {user_guess}!")

  for letter in range(0, len(chosen_word)):
    if user_guess == chosen_word[letter]:
      secret_list[letter] = user_guess

  if not user_guess in chosen_word:
      print(f"\nThe letter {user_guess} is not in the word. You lose a life!")
      lives -= 1
  if lives == 0:
    print(stages[6])
    print("You ran out of lives. You lose!")
    print(f"The word was {chosen_word}!")
    break;

if not '_' in secret_list:
  print(stages[7 - (lives + 1)])
  print(" ".join(secret_list))
  print("Congratulations. You win.")