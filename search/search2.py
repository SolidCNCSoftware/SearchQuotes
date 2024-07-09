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

# Kullanım örneği
input_file_path = 'English.rc'   #r"C:\Users\CAN\Desktop\English.rc"  # Giriş dosya yolunu buraya girin
output_file_path = 'translate.txt'  # Çıkış dosya yolunu buraya girin

quoted_texts_vector = extract_quoted_texts(input_file_path)
write_to_file(quoted_texts_vector, output_file_path)

print(f"Extracted texts have been written to {output_file_path}")
