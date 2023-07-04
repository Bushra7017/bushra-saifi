# First install the Library in your PC by following command:-!pip install googletrans==4.0.0-rc1
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def main():
    text = input("Enter the English text to translate: ")
    translated_text = translate_text(text, 'hi')  # 'hi' represents Hindi
    print("Translated text in Hindi:", translated_text)

if __name__ == '__main__':
    main()