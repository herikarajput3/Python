print("Welcome to Mini ChatGPT! Ask me something.\n")

question = input("You: ").lower()

if question == "hi" or question == "hello":
    print("Bot: Hello! How are you?")

elif question == "what is your name?":
    print("Bot: I am Mini ChatGPT, your Python-made chatbot!")

elif question == "how are you?":
    print("Bot: I am doing great, thank you for asking!")
    
elif question == "who created you?":
    print("Bot: I was created by a Python programmer.")
    
elif question == "what can you do?":
    print("Bot: I can chat with you and answer simple questions.")

elif question == "tell me a joke?":
    print("Bot: Why did the scarecrow win an award? Because he was outstanding in his field!")

elif question == "what is your favorite color?":
    print("Bot: My favorite color is blue!")

elif question == "what is your favorite food?":
    print("Bot: I love pizza!")

elif question == "what is your favorite hobby?":
    print("Bot: I enjoy chatting with you!")

elif question == "bye":
    print("Bot: Goodbye! Have a great day!")

else:
    print("Bot: Sorry, I don't understand that question.")
