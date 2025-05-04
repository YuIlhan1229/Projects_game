import random
import time

# Hàm để in chậm dòng chữ như trong game
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def start_game():
    slow_print("🚀 Welcome to SPACE ADVENTURE!")
    slow_print("You are the captain of a spaceship on a mission to explore a mysterious galaxy.")
    input("Press Enter to begin your journey...")

    choice1()

def choice1():
    slow_print("\n🌌 You reach a fork in space.")
    slow_print("Do you:")
    slow_print("1. Enter the dark wormhole on the left 🌀")
    slow_print("2. Head to the glowing planet on the right 🌍")
    choice = input("Your choice (1/2): ")

    if choice == '1':
        wormhole()
    elif choice == '2':
        planet()
    else:
        slow_print("Invalid choice. Try again.")
        choice1()

def wormhole():
    slow_print("\n🌀 You are sucked into the wormhole...")
    slow_print("Everything goes black for a moment...")
    time.sleep(1)
    if random.random() < 0.5:
        slow_print("You exit in a new galaxy full of friendly aliens! 🛸")
        slow_print("🎉 They throw you a party and declare you galactic ambassador!")
    else:
        slow_print("Oh no! You end up near a black hole and cannot escape... ☠️")
        slow_print("GAME OVER.")
    play_again()

def planet():
    slow_print("\n🌍 You land on a lush, green planet.")
    slow_print("A robot greets you and offers a challenge.")
    slow_print("Do you:")
    slow_print("1. Accept the challenge 🧠")
    slow_print("2. Politely decline and ask for directions home 🧭")
    choice = input("Your choice (1/2): ")

    if choice == '1':
        challenge()
    elif choice == '2':
        slow_print("The robot gives you coordinates to get back to Earth. 🛰️")
        slow_print("You return safely. Mission complete! ✅")
        play_again()
    else:
        slow_print("Invalid choice.")
        planet()

def challenge():
    slow_print("\n🤖 The robot asks: What is 7 * 8?")
    answer = input("Your answer: ")

    if answer.strip() == '56':
        slow_print("Correct! The robot gives you a treasure map. 🗺️")
        slow_print("You follow the map and find alien technology! 🎉")
    else:
        slow_print("Incorrect. The robot zaps your ship and you're stranded! 😢")
    play_again()

def play_again():
    again = input("\n🔁 Do you want to play again? (Y/N): ").strip().lower()
    if again == 'y':
        start_game()
    else:
        slow_print("👋 Thanks for playing! Safe travels, captain.")

# Bắt đầu game
if __name__ == "__main__":
    start_game()