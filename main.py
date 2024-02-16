import pyttsx3
import datetime
import os
import time


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_time():
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")
    return time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_message():
    message = "Welcome to Aayushman's Robo Speaker"
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)  
    print("\n")
    speak(message)

if __name__ == '__main__':
    clear_screen()
    welcome_message()
    
    last_message = ""
    
    while True:
        print("\nMENU:")
        print("1. Speak")
        print("2. Get current time")
        print("3. Change voice")
        print("4. Change speaking rate")
        print("5. Save audio")
        print("6. Repeat last message")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            clear_screen()
            text = input("Enter what you want me to speak: ")
            speak(text)
            last_message = text
            print("\nSpoken successfully!")
        elif choice == "2":
            clear_screen()
            current_time = get_time()
            print("Current time is:", current_time)
            speak("The current time is " + current_time)
        elif choice == "3":
            clear_screen()
            voices = engine.getProperty('voices')
            print("\nAvailable voices:")
            for idx, voice in enumerate(voices):
                print(f"{idx+1}. {voice.name}")
            voice_choice = input("Enter the number corresponding to the voice you want to use: ")
            if 0 < int(voice_choice) <= len(voices):
                engine.setProperty('voice', voices[int(voice_choice)-1].id)
                print("Voice changed successfully!")
            else:
                print("Invalid choice.")
        elif choice == "4":
            clear_screen()
            rate = int(input("Enter speaking rate (words per minute): "))
            engine.setProperty('rate', rate)
            print("Speaking rate changed successfully!")
        elif choice == "5":
            clear_screen()
            text = input("Enter the text you want to save as audio: ")
            filename = input("Enter the filename (without extension): ")
            engine.save_to_file(text, f"{filename}.mp3")
            engine.runAndWait()
            print(f"Audio saved as {filename}.mp3")
        elif choice == "6":
            clear_screen()
            print("Repeating last message:")
            if last_message:
                speak(last_message)
                print(f"Repeated last message: {last_message}")
            else:
                print("No message to repeat.")
        elif choice == "7":
            clear_screen()
            message="Exiting the Robo Speaker. Goodbye!"
            for char in message:
                print(char, end='', flush=True)
                time.sleep(0.05)  
            print("\n")
            speak(message)
            break
        else:
            clear_screen()
            print("Invalid choice. Please select a valid option.")
