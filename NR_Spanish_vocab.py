from tkinter import *
from random import randint
from tkinter import messagebox
import vocab

hint_1 = False
hint_2 = False

root = Tk()
root.iconbitmap("images/logo_2UE_icon.ico")
root.config(highlightthickness=0)
root.title("NerdRage Apps - Spanish to English")
root.geometry("1200x400")

initial_words = [(("Click 'Choose Module' button"), ("☺☺☺"))]
final_words = [_ for _ in initial_words]
answered_words = []

# get a count of our word list
count = len(final_words)

def answer():
    global count, final_words, initial_words
    if len(my_entry.get()) == 0:
        answer_label.config(text="Maybe try typing something first!")
    elif my_entry.get().lower() == final_words[random_word][1].lower() or \
            my_entry.get().lower() == final_words[random_word][2].lower() or \
            my_entry.get().lower() == final_words[random_word][3].lower():
        hint_label.config(text=final_words[random_word][1])
        answer_label.config(text="Correct!")
        answered_words.append(final_words[random_word])
        final_words.remove(final_words[random_word])
        status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
        count -= 1
    else:
        answer_label.config(text="Wrong!")


def next():
    global hint_1, hint_2, initial_words, final_words, answered_words
    hint_1 = False
    hint_2 = False
    global hinter, hint_count, count
    # Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    # Reset Hint stuff
    hinter = ""
    hint_count = 0
    if len(final_words) == 0:
        messagebox.showinfo("Congratulations!", "You answered all questions!\nThanks for playing!")
    else:
        # Create a random variable
        global random_word
        random_word = randint(0, count - 1)
        # Update label with Spanish word
        spanish_word.config(text=final_words[random_word][0])


# Keep track of the hints
hinter = ""
hint_count = 0

def hint():
    global hint_1, hint_2
    global hint_count
    global hinter
    display = ""
    if hint_1 == False:
        if hint_count < len(final_words[random_word][1]):
            hinter = hinter + final_words[random_word][1][hint_count]
            hint_label.config(text=hinter)
            hint_count += 1
            hint_1 = True
    elif hint_2 == False:
        for n in final_words[random_word][1]:
            if n == " ":
                display += "  "
            else:
                display += "_ "
        display = display.replace(display[0], final_words[random_word][1][0], 1)
        display = display[:-2]
        num = len(final_words[random_word][1])
        display += final_words[random_word][1][num - 1]
        hint_label.config(text=display)
        hint_2 = True
    else:
        pass

# Choose section 😭
def choose_section_11():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_11
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_12():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_12
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_13():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_13
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_14():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_14
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_15():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_15
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_16():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_16
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_17():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_17
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_18():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_18
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_19():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_19
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_110():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_110
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_111():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_111
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_112():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_112
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_113():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_112
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_21():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_21
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_22():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_22
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_23():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_23
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_24():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_24
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_25():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_25
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_26():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_26
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_27():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_27
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_28():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_28
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_31():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_31
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_32():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_32
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_33():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_33
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_34():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_34
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_35():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_35
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_36():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_36
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_37():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_37
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_38():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_38
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_39():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_39
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_41():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_41
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_42():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_42
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_43():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_43
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_44():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_44
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_45():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_45
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_46():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_46
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_47():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_47
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_48():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_48
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_49():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_49
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_410():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_410
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_411():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_411
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_51():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_51
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_52():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_52
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_53():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_53
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_54():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_54
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_55():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_55
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_56():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_56
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_57():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_57
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_58():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_58
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_59():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_59
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_510():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_510
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_511():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_511
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_512():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_512
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_513():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_513
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_61():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_61
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_62():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_62
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_63():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_63
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_64():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_64
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_65():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_65
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_66():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_66
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_67():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_67
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_68():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_68
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_69():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_69
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_71():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_71
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_72():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_72
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_73():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_73
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_74():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_74
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_75():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_75
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_76():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_76
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_77():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_77
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_78():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_78
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_79():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_79
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_710():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_710
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_81():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_81
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_82():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_82
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_83():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_83
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_84():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_84
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_85():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_85
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_86():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_86
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_87():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_87
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_88():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_88
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


def choose_section_89():
    global initial_words, final_words, answered_words, count
    initial_words = []
    final_words = []
    answered_words = []
    initial_words = vocab.section_89
    final_words = [_ for _ in initial_words]
    count = len(final_words)
    status_bar.config(text=f"{len(answered_words)} / {len(initial_words)} expressions answered.")
    next()


#Create menus and submenus
menubar = Menu(root)
choose_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Choose Module", menu=choose_menu)

root.config(menu=menubar)

menu_sub1 = Menu(choose_menu, tearoff=0)
choose_menu.add_cascade(label="1  ¡Desconéctate!", menu=menu_sub1)
menu_sub1.add_command(label="¿Dónde vives?", command=choose_section_11)
menu_sub1.add_command(label="¿Qué haces en verano?", command=choose_section_12)
menu_sub1.add_command(label="¿Con qué frecuencia?", command=choose_section_13)
menu_sub1.add_command(label="¿Qué tiempo hace?", command=choose_section_14)
menu_sub1.add_command(label="¿Qué te gusta hacer?", command=choose_section_15)
menu_sub1.add_command(label="¿Adónde fuiste de vacaciones?", command=choose_section_16)
menu_sub1.add_command(label="¿Qué hiciste?", command=choose_section_17)
menu_sub1.add_command(label="¿Qué tal lo pasaste?", command=choose_section_18)
menu_sub1.add_command(label="¿Cómo era el hotel?", command=choose_section_19)
menu_sub1.add_command(label="¿Cómo era el pueblo?", command=choose_section_110)
menu_sub1.add_command(label="Quisiera reservar", command=choose_section_111)
menu_sub1.add_command(label="Quiero quejarme", command=choose_section_112)
menu_sub1.add_command(label="Mis vacaciones desastrosas", command=choose_section_113)

menu_sub2 = Menu(choose_menu, tearoff=0)
choose_menu.add_cascade(label="2  Mi vida en el insti", menu=menu_sub2)
menu_sub2.add_command(label="¿Te interesa(n)?", command=choose_section_21)
menu_sub2.add_command(label="¿Qué tal los estudios?", command=choose_section_22)
menu_sub2.add_command(label="¿Cómo es tu insti?", command=choose_section_23)
menu_sub2.add_command(label="Tengo que llevar", command=choose_section_24)
menu_sub2.add_command(label="Las normas del insti", command=choose_section_25)
menu_sub2.add_command(label="¿Cómo es tu día escolar?", command=choose_section_26)
menu_sub2.add_command(label="¿Qué vas a hacer?", command=choose_section_27)
menu_sub2.add_command(label="Las actividades extraescolares", command=choose_section_28)

menu_sub3 = Menu(choose_menu, tearoff=0)
choose_menu.add_cascade(label="3  Mi gente", menu=menu_sub3)
menu_sub3.add_command(label="¿Qué aplicaciones usas?", command=choose_section_31)
menu_sub3.add_command(label="¿Qué estás haciendo?", command=choose_section_32)
menu_sub3.add_command(label="¿Qué te gusta leer?", command=choose_section_33)
menu_sub3.add_command(label="¿Qué es mejor?", command=choose_section_34)
menu_sub3.add_command(label="La familia", command=choose_section_35)
menu_sub3.add_command(label="¿Cómo es?", command=choose_section_36)
menu_sub3.add_command(label="¿Cómo es de carácter?", command=choose_section_37)
menu_sub3.add_command(label="¿Te llevas bien con tu familia?", command=choose_section_38)
menu_sub3.add_command(label="¿Cómo es un buen amigo?", command=choose_section_39)

menu_sub4 = Menu(choose_menu, tearoff=0)
choose_menu.add_cascade(label="4  Intereses e influencias", menu=menu_sub4)
menu_sub4.add_command(label="La paga", command=choose_section_41)
menu_sub4.add_command(label="Mis ratos libres", command=choose_section_42)
menu_sub4.add_command(label="La música", command=choose_section_43)
menu_sub4.add_command(label="El deporte", command=choose_section_44)
menu_sub4.add_command(label="La tele", command=choose_section_45)
menu_sub4.add_command(label="Las películas", command=choose_section_46)
menu_sub4.add_command(label="Nacionalidades", command=choose_section_47)
menu_sub4.add_command(label="Temas del momento", command=choose_section_48)
menu_sub4.add_command(label="Ir al cine", command=choose_section_49)
menu_sub4.add_command(label="¿En el cine o en casa?", command=choose_section_410)
menu_sub4.add_command(label="Los modelos a seguir", command=choose_section_411)

menu_sub5 = Menu(choose_menu, tearoff=0)
choose_menu.add_cascade(label="5  Ciudades", menu=menu_sub5)
menu_sub5.add_command(label="Mi ciudad tiene", command=choose_section_51)
menu_sub5.add_command(label="¿Por dónde se va al cine?", command=choose_section_52)
menu_sub5.add_command(label="¿Cómo es tu zona?", command=choose_section_53)
menu_sub5.add_command(label="En la oficina de turismo", command=choose_section_54)
menu_sub5.add_command(label="¿Qué haremos mañana?", command=choose_section_55)
menu_sub5.add_command(label="¿Qué tiempo hará?", command=choose_section_56)
menu_sub5.add_command(label="Las tiendas", command=choose_section_57)
menu_sub5.add_command(label="Recuerdos y regalos", command=choose_section_58)
menu_sub5.add_command(label="Quejas", command=choose_section_59)
menu_sub5.add_command(label="De compras", command=choose_section_510)
menu_sub5.add_command(label="Los pros y los contras de la ciudad", command=choose_section_511)
menu_sub5.add_command(label="¿Qué harías?", command=choose_section_512)
menu_sub5.add_command(label="Destino Arequipa", command=choose_section_513)

menu_sub6 = Menu(choose_menu, tearoff=0)
choose_menu.add_cascade(label="6  De costumbre", menu=menu_sub6)
menu_sub6.add_command(label="Las comidas", command=choose_section_61)
menu_sub6.add_command(label="Las expresiones de cantidad", command=choose_section_62)
menu_sub6.add_command(label="Los alimentos", command=choose_section_63)
menu_sub6.add_command(label="Mi rutina diaria", command=choose_section_64)
menu_sub6.add_command(label="¿Qué le pasa?", command=choose_section_65)
menu_sub6.add_command(label="Las fiestas", command=choose_section_66)
menu_sub6.add_command(label="Un día especial", command=choose_section_67)
menu_sub6.add_command(label="¿Qué va a tomar?", command=choose_section_68)
menu_sub6.add_command(label="Un festival de música", command=choose_section_69)

menu_sub7 = Menu(choose_menu, tearoff=0)
choose_menu.add_cascade(label="7  ¡A currar!", menu=menu_sub7)
menu_sub7.add_command(label="¿En qué trabajas?", command=choose_section_71)
menu_sub7.add_command(label="¿Qué tipo de persona eres?", command=choose_section_72)
menu_sub7.add_command(label="¿Qué haces para ganar dinero?", command=choose_section_73)
menu_sub7.add_command(label="Mis prácticas laborales", command=choose_section_74)
menu_sub7.add_command(label="¿Por qué aprender idiomas?", command=choose_section_75)
menu_sub7.add_command(label="Solicitando un trabajo", command=choose_section_76)
menu_sub7.add_command(label="Un año sabático", command=choose_section_77)
menu_sub7.add_command(label="¿Cómo viajarías?", command=choose_section_78)
menu_sub7.add_command(label="Viajando en tren", command=choose_section_79)
menu_sub7.add_command(label="El futuro", command=choose_section_710)

menu_sub8 = Menu(choose_menu, tearoff=0)
choose_menu.add_cascade(label="8  Hacia un mundo mejor", menu=menu_sub8)
menu_sub8.add_command(label="¿Cómo es tu casa?", command=choose_section_81)
menu_sub8.add_command(label="Cuidar el medio ambiente en casa", command=choose_section_82)
menu_sub8.add_command(label="¿Cuáles son los problemas más serios?", command=choose_section_83)
menu_sub8.add_command(label="Actúa localmente", command=choose_section_84)
menu_sub8.add_command(label="Use energías renovables", command=choose_section_85)
menu_sub8.add_command(label="Una dieta sana", command=choose_section_86)
menu_sub8.add_command(label="Vivir a tope", command=choose_section_87)
menu_sub8.add_command(label="El deporte nos une", command=choose_section_88)
menu_sub8.add_command(label="Apúntate", command=choose_section_89)


# Create GUI Layout
label_frame = Frame(root)
label_frame.pack(pady=5, padx=30)

spanish_word = Label(label_frame, width= 60, text="", font=("Helvetica", 24, "italic"))
spanish_word.pack(pady=20, padx=5)

hint_label = Label(label_frame, width=110, text="", font=("Courier", 14))
hint_label.pack(pady=10, padx=5)

my_entry = Entry(label_frame, width=30, justify="center", font=("Helvetica", 16))
my_entry.focus()
my_entry.pack(pady=20, padx=5)

answer_label = Label(label_frame, text="", font=("Arial", 16, "bold"))
answer_label.pack(pady=20, padx=5)

# Create buttons
button_frame = Frame(root)
button_frame.pack(pady=5)

answer_image = PhotoImage(file="images/answer4.png")
next_image = PhotoImage(file="images/next.png")
hint_image = PhotoImage(file="images/hint.png")

answer_button = Button(button_frame, image=answer_image, command=answer, highlightthickness=0)
root.bind("<Return>", lambda event:answer())
answer_button.grid(row=0, column=1, padx=10)

next_button = Button(button_frame, image=next_image, command=next, highlightthickness=0)
root.bind("<Shift_R>", lambda event:next())
next_button.grid(row=0, column=2, padx=10)

hint_button = Button(button_frame, image=hint_image, command=hint, highlightthickness=0)
root.bind("<Shift_L>", lambda event:hint())
hint_button.grid(row=0, column=0, padx=10)

# Create hint label


# Status bar
status_bar = Label(root, text=f"{len(answered_words)} / {len(initial_words)} expressions answered.", bd=1, relief=SUNKEN, anchor=E)
status_bar.pack()


next()


root.mainloop()

# TODO crear funcion para q haga archivos pdf
    # requeriría q preguntara tu nombre
    # añade las secciones completadas, palabras acertadas (contando otras secciones), nombre, fecha y hora
# TODO encriptar todo el codigo para q no sea interceptado por antivirus