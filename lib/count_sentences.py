#!/usr/bin/env python3

class MyString:
    def __init__(self, value=None):
      # Constructor to initialize the object with a string value
      if value is not None and not isinstance(value, str):
          # Check if the value provided is a string, if not, print an error message
          print("The value must be a string.")
          self.value = ""
      else:
         # If the value is a string or None, assign it to the instance variable
          self.value = value if value is not None else ""

    def set_value(self, value):
      # Method to set the value of the string
      if isinstance(value, str):
        # Check if the value provided is a string, if so, assign it
          self.value = value
      else:
          # If the value provided is not a string, print an error message
          print("The value must be a string.")

    def get_value(self):
       # Method to retrieve the current value of the string
       return self.value


    def is_sentence(self):
       # Method to check if the string ends with a punctuation indicating a sentence
        return self.value.endswith(".") or self.value.endswith("!") or self.value.endswith("?")

    def is_question(self):
       # Method to check if the string ends with a question mark
        return self.value.endswith("?")

    def is_exclamation(self):
       # Method to check if the string ends with an exclamation mark
        return self.value.endswith("!")

    def count_sentences(self):
        # Method to count the number of sentences in the string
        sentences = self.value.split(".") # Split the string into sentences using period as delimiter
        count = 0
        for sentence in sentences:
           # Iterating through each sentence and check if it's not empty and ends with punctuation
            if sentence.strip() and (sentence.endswith("!") or sentence.endswith("?") or sentence):
                count += 1  # To increment the count if the conditions are met
        return count

string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())
print(string.is_question())
print(string.is_exclamation())
print(string.count_sentences())

pass
