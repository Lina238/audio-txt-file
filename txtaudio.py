import pyttsx3
book=open(r"C:/Users/Lina-pc/OneDrive/Bureau/bureau/work/Book.txt")
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()