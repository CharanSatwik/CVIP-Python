import time
import random
sentence_list = ["The quick brown fox jumps over the lazy dog.",
                 "Python is a versatile and powerful programming language.",
                 "Practice makes perfect when it comes to typing speed.",
                 "Programming is a valuable skill in today's world.",
                 "Learning Python is fun and rewarding."]
sentence = str(random.choices(sentence_list))
word_count = len(sentence.split())
print(sentence)
while True:
    t1 = time.time()
    input_text = str(input("Enter the text: "))
    t2 = time.time()
    acc = len(set(input_text.split()) & set(sentence.split()))
    acc = (acc/word_count)*100
    t3 = t2-t1
    wpm = (word_count / t3)*100

    print("WPM = {:.2f} Accuracy = {:.2f} Time Taken = {:.2f}s".format(
        wpm, acc, t3))
