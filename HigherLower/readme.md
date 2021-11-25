# Higher lower game. 

> A simple game, comparing who has more followers on Instagram (Numbers not actual from Insta, roughly)
You can use it by simply stating A or B has more followers, and it increments a score.

## Example
```py
def play(actual_score):
  score = actual_score
  right_answer = True
  while right_answer:
    score_1 = comparing_list[0]["follower_count"]
    score_2 = comparing_list[1]["follower_count"]
    if score_1 == score_2:
      comparing_list[1] = generate_candidate()
      score_2 = comparing_list[1]["follower_count"]
    higher = compare_scores(score_1,score_2)
    print(f'Compare A: {comparing_list[0]["name"]}, a {comparing_list[0]["description"]}, from {comparing_list[0]["country"]} ')
    print(f"{vs}")
    print(f'Against B: {comparing_list[1]["name"]}, a {comparing_list[1]["description"]}, from {comparing_list[1]["country"]} ')
    choice = input("\nWho has more followers ? Type 'A' or 'B': ").lower()
    if choice == "a" or choice == "b":
      if choice == higher:
        clear()
        print(logo)
        score += 1
        print(f"You are correct! Current score {score}\n")
        comparing_list[0] = comparing_list[1]
        comparing_list[1] = generate_candidate()  
      elif higher == False:
        right_answer = False
      else:
        clear()
        print(logo)
        print(f"You lost! With final score {score}")
        right_answer = False
        return
    else:
      clear()
      print("You typed something different, try again!\n")
  return      
```