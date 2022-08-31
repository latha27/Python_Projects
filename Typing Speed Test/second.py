from tkinter import *
import random

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
FONT_NAME = "Ariel"
NO_OF_WORDS = 100
TIMER = 60

words = []
selected_word_list = []

def load_words():
  import requests
  global words, selected_word_list
  word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
  response = requests.get(word_site)
  words = response.content.decode('utf-8').splitlines()
  selected_word_list = random.sample(words, NO_OF_WORDS)
  for word in selected_word_list:
    word = word + "  "
    passagebox.insert(INSERT, word)
  passagebox.config(state=DISABLED, wrap=WORD)

def start_timer(count):
  #  Start timer only when user starts to type
  if len(textbox.get(1.0, END)) - 1 != 0:
    #  Count number of spaces to determine entry word to highlight
    word_entry = textbox.get(1.0, END).count(" ")
    highlight_word(word_entry)
    timer_label.config(text=f"{count}s")
    if count > 0:
      window.after(1000, start_timer, count - 1)
    else:
      textbox.config(state=DISABLED)
      check_result()
  else:
    window.after(1000, start_timer, count)

def check_result():
  incorrect_words_num = 0
  input = textbox.get("1.0", 'end-1c')
  input_list = input.split(" ")
  no_of_words = len(input_list)
  for index in range(0, len(input_list)):
    if input_list[index] != selected_word_list[index]:
      incorrect_words_num += 1
  timer_label.config(text=f"Typing speed: {no_of_words} words per minute.  "
                          f"Number of incorrect words: {incorrect_words_num}", fg=RED, font=(FONT_NAME, 12, "bold"))

def highlight_word(word_entry):
  #  Remove all highlighting first
  passagebox.tag_remove("start",  "1.0", 'end')
  pos = passagebox.search(selected_word_list[word_entry], '1.0', stopindex=END)
  starting_pos = pos
  ending_pos = pos.split(".")[0] + "." + str(int(pos.split(".")[1]) + len(selected_word_list[word_entry]))
  passagebox.tag_add("start", starting_pos, ending_pos)
  passagebox.tag_config("start", background=PINK)

window = Tk()
window.title("Test Your Typing Speed")
window.config(padx=10, pady=10, bg=YELLOW)

passage_label = Label(text="Test Passage", bg=YELLOW, fg=BLACK, font=(FONT_NAME, 14))
passage_label.grid(row=0, column=0)

passagebox = Text(window, height=10, width=100, font=(FONT_NAME, 14))
passagebox.grid(row=1, column=0, pady=(5, 20))

instruction_label = Label(text="Type below. Timer will start when you start typing.",
                          bg=YELLOW, fg=BLACK, font=(FONT_NAME, 14))
instruction_label.grid(row=2, column=0)

textbox = Text(window, height=10, width=100, font=(FONT_NAME, 14), wrap=WORD)
textbox.focus_set()
textbox.grid(row=3, column=0, pady=(5, 20))

timer_label = Label(text=f"{TIMER}s", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=4, column=0)

load_words()
start_timer(TIMER)
window.mainloop()