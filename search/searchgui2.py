import tkinter as tk
from tkinter import filedialog, messagebox
import re
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def extract_quoted_texts(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
    
    quoted_texts = re.findall(r'"(.*?)"', content)
    return quoted_texts

def write_to_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")

def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if input_file_path:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, input_file_path)

def select_output_file():
    global output_file_path
    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if output_file_path:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, output_file_path)

def add_to_ignore_list():
    ignore_item = ignore_entry.get().strip().replace('\n', '')
    if ignore_item:
        ignore_listbox.insert(tk.END, ignore_item)
        ignore_entry.delete(0, tk.END)

def remove_from_ignore_list():
    selected_index = ignore_listbox.curselection()
    if selected_index:
        ignore_listbox.delete(selected_index)

def process_files():
    global input_file_path, output_file_path
    if not input_file_path or not output_file_path:
        messagebox.showerror("Error", "Please select input and output files first.")
        return
    
    ignore_items = ignore_listbox.get(0, tk.END)
    quoted_texts_vector = extract_quoted_texts(input_file_path)
    
    filtered_texts = []
    for text in quoted_texts_vector:
        ignore_text = False
        for ignore_item in ignore_items:
            if ignore_item in text:
                ignore_text = True
                break
        if not ignore_text:
            filtered_texts.append(text)
    
    write_to_file(filtered_texts, output_file_path)
    messagebox.showinfo("Success", f"Extracted texts have been written to {output_file_path}")

# Ana pencere oluşturma
root = tk.Tk()
root.title("Text Extraction Tool")

# Giriş dosyası seçme
input_file_label = tk.Label(root, text="Select Input File:")
input_file_label.grid(row=0, column=0, padx=10, pady=10)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=10, pady=10)
input_file_button = tk.Button(root, text="Browse...", command=select_input_file)
input_file_button.grid(row=0, column=2, padx=10, pady=10)

# Çıkış dosyası seçme
output_file_label = tk.Label(root, text="Save as:")
output_file_label.grid(row=1, column=0, padx=10, pady=10)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=10, pady=10)
output_file_button = tk.Button(root, text="Browse...", command=select_output_file)
output_file_button.grid(row=1, column=2, padx=10, pady=10)

# Ignore listesi
ignore_label = tk.Label(root, text="Ignore List:")
ignore_label.grid(row=2, column=0, padx=10, pady=10)
ignore_entry = tk.Entry(root, width=30)
ignore_entry.grid(row=2, column=1, padx=10, pady=10)
add_ignore_button = tk.Button(root, text="Add", command=add_to_ignore_list)
add_ignore_button.grid(row=2, column=2, padx=10, pady=10)
remove_ignore_button = tk.Button(root, text="Remove", command=remove_from_ignore_list)
remove_ignore_button.grid(row=2, column=3, padx=10, pady=10)
ignore_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
ignore_listbox.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

# İşlem butonu
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

# Pencereyi çalıştırma
root.mainloop()
