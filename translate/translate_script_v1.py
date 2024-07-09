import pandas as pd
from translate import Translator

# Çevirici oluşturun (örneğin, İngilizce'den Türkçe'ye çevirme)
translator = Translator(to_lang="tr")

# Kelimelerinizi içeren CSV dosyasını yükleyin
df = pd.read_csv('voc.csv')

# Yeni bir sütun ekleyerek çevirileri saklayın
df['Translated'] = df['Word'].apply(translator.translate)

# Çevirilmiş kelimeleri yeni bir CSV dosyasına kaydedin
df.to_csv('translated_v1.csv', index=False)
