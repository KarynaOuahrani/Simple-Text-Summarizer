

import nltk
import heapq
import string
import tkinter as tk
from tkinter import messagebox
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def text_summarizer(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize the text into words and convert to lower case
    words = word_tokenize(text.lower())

    # Remove stopwords and punctuation from the word list
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and word not in string.punctuation]

    # Calculate word frequencies
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_freq[word]
                else:
                    sentence_scores[sent] += word_freq[word]

    # Select the top sentences based on their scores
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Join the top sentences to form the summary
    summary = ' '.join(summary_sentences)
    return summary

def start_program():
    main_frame.pack_forget()
    text_input_frame.pack()

def exit_program():
    root.quit()

def summarize_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        summary = text_summarizer(text)
        result_text.set(summary)
    else:
        messagebox.showwarning("Input Error", "Please enter some text to summarize.")

def restart_program():
    result_text.set("")
    text_entry.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Text Summarizer")
root.geometry("800x600")

# Style settings
button_style = {'font': ('Arial', 14), 'bg': 'lightblue', 'fg': 'black', 'activebackground': 'blue', 'activeforeground': 'white'}
label_style = {'font': ('Arial', 12), 'bg': 'lightgray', 'fg': 'black'}
text_style = {'font': ('Arial', 12), 'bg': 'white', 'fg': 'black'}

# Main frame with introduction, Start and Exit buttons
main_frame = tk.Frame(root, bg='lightgray')
intro_label = tk.Label(main_frame, text="Welcome to the Text Summarizer Application!\n\nThis application allows you to input a block of text and generates a concise summary of it.\n\nClick 'Start' to begin.", **label_style)
intro_label.pack(pady=20)
start_button = tk.Button(main_frame, text="Start", command=start_program, **button_style)
exit_button = tk.Button(main_frame, text="Exit", command=exit_program, **button_style)
start_button.pack(pady=10)
exit_button.pack(pady=10)
main_frame.pack(fill='both', expand=True)

# Frame for text input and summarization
text_input_frame = tk.Frame(root, bg='lightgray')
intro_label2 = tk.Label(text_input_frame, text="Enter the text you want to summarize below:", **label_style)
intro_label2.pack(pady=10)
text_entry = tk.Text(text_input_frame, height=15, width=80, **text_style)
text_entry.pack(pady=10)
summarize_button = tk.Button(text_input_frame, text="Summarize", command=summarize_text, **button_style)
summarize_button.pack(pady=10)
result_text = tk.StringVar()
result_label = tk.Label(text_input_frame, textvariable=result_text, wraplength=600, justify="left", **label_style)
result_label.pack(pady=10)
restart_button = tk.Button(text_input_frame, text="Restart", command=restart_program, **button_style)
restart_button.pack(pady=10)

# Start the main event loop
root.mainloop()





