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

# Kullanım örneği
file_path = 'English.rc'  # Dosya yolunu buraya girin
quoted_texts_vector = extract_quoted_texts(file_path)
print(quoted_texts_vector)
