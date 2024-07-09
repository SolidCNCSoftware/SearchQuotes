import pandas as pd
from googletrans import Translator

# Çevirici oluşturun
translator = Translator()

# Kelimelerinizi içeren CSV dosyasını yükleyin
df = pd.read_csv('voc.csv')

# Çeviri fonksiyonunu tanımlayın
def translate_word(word):
    translation = translator.translate(word, dest='tr')
    return translation.text

# Yeni bir sütun ekleyerek çevirileri saklayın
df['Translated'] = df['Word'].apply(translate_word)

# Çevirilmiş kelimeleri yeni bir CSV dosyasına kaydedin
df.to_csv('translated_v2.csv', index=False)
