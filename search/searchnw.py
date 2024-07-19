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
        lines = file.readlines()
        quoted_texts_with_positions = []
        for idx, line in enumerate(lines, start=1):
            words = line.split()
            quoted_texts = re.findall(r'"(.*?)"', line)
            word_index = 0
            for quoted_text in quoted_texts:
                word_index = line.index(quoted_text, word_index)
                word_position = len(line[:word_index].split()) + 1
                quoted_texts_with_positions.append((quoted_text, idx, word_position))
                word_index += len(quoted_text)
    
    return quoted_texts_with_positions

def write_to_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item[0]}, Line: {item[1]}, Word: {item[2]}\n")

# Kullanım örneği
input_file_path = 'English.rc'   # Giriş dosya yolunu buraya girin
output_file_path = 'translate_number_word.txt'  # Çıkış dosya yolunu buraya girin

quoted_texts_vector = extract_quoted_texts(input_file_path)
write_to_file(quoted_texts_vector, output_file_path)

print(f"Extracted texts with line and word positions have been written to {output_file_path}")
