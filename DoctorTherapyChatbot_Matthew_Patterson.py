"""
File: DoctorTherapyChatbot_StartingCode.py

Conducts an interactive session of nondirective psychotherapy.
"""

import random

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.",
          "You Don't say. What else can you tell me?",
          "I don't think that's fair. Why was it said?"
          )

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ",
              "What does this mean to you, ",
              "Have you seen help before for ")

replacements = {"i":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours","they":"thier",
                "He":"Him", "our":"you","you":"I","You":"I" }

def reply(sentence):
    """Implements two different reply strategies."""
    probability = random.randint(1, 4)
    if probability == 1:
        # Just hedge: choice() is a function that randomly picks one of the elements from a list or tuple.
        answer = random.choice(hedges)
    else:
        # Transform the current input
        answer = random.choice(qualifiers) + changePerson(sentence)
    return answer

def changePerson(sentence):
    """Replaces first person pronouns with second person pronouns."""
    words = sentence.split()
    replyWords = []
    check =0
    for word in words:
        word = word.lower()
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        elif sentence.upper() == "STOP":
            print("Have a nice day!")
            break
        print(reply(sentence))
main()

