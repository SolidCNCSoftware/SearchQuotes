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
            quoted_texts = re.findall(r'"(.*?)"', line)
            for i, quoted_text in enumerate(quoted_texts, start=1):
                quoted_texts_with_positions.append((quoted_text, idx, i))

    return quoted_texts_with_positions


def check_patterns(text):
    if re.search(r'#include|[a-zA-Z_]+\.h', text): #keywords
        return True

    elif re.search(r'&[a-zA-Z0-9]+\s*(?:\.\.\.|\\t[a-zA-Z0-9]+)?', text): #menu items
        return True

    elif re.search(r'res\\\\(?:[a-zA-Z0-9_]+\\)*[a-zA-Z0-9_]+\.[a-zA-Z0-9]+', text): #file paths
        return True

    elif re.search(r'\b\w+\.bmp\b', text): #bmp
        return True

    elif re.search(r'\\n\w+', text): #/n
        return True

    elif re.search(r'\\n\w+\s+\w+', text): #/n
        return True

    elif re.search(r'^\d+$', text): #numbers
        return True

    elif re.search(r'^[^a-zA-Z]*$', text): #no letters
        return True

    elif re.search(r'^[^a-zA-Z]*[a-zA-Z][^a-zA-Z]*$', text): #just one letter
        return True
    return False




def write_to_file(data, input_file, output_file):
    encoding = detect_encoding(input_file)
    with open(input_file, 'r', encoding=encoding) as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for item in data:
            text, line_number, word_position = item
            file.write(f"{text}, Line: {line_number}, Word: {word_position}")

            if check_patterns(text):
                file.write(", Translate: 0")
            else:
                file.write(", Translate: 1")

            file.write("\n")


# Kullanım örneği
input_file_path = 'English.rc'  # Giriş dosya yolunu buraya girin
output_file_path = 'deneme.txt'  # Çıkış dosya yolunu buraya girin

quoted_texts_vector = extract_quoted_texts(input_file_path)
write_to_file(quoted_texts_vector, input_file_path, output_file_path)

print(f"Extracted texts with line and word positions have been written to {output_file_path}")


