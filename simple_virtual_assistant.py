import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import webbrowser
import pyjokes
import playsound

def text_to_speech():
    language_dict = {
        "portugues": "pt", "ingles": "en", "espanhol": "es",
        "frances": "fr", "italiano": "it", "alemao": "de",
        "russo": "ru", "chines": "zh-CN", "coreano": "ko",
        "arabe": "ar", "turco": "tr", "polones": "pl", "sueco": "sv",
    }
    
    while True:
        language = input("Em qual idioma deseja ouvir? ").lower()
        if language in language_dict:
            language = language_dict[language]
            break
        else:
            print("Idioma não encontrado, tente novamente.")
    
    text = input("Digite o texto que deseja ouvir: ")
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("text.mp3")
    playsound.playsound("text.mp3")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Fale algo...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="pt-BR")
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio")
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento de voz")
    return ""

def speak(text):
    audio = gTTS(text=text, lang="pt", slow=False)
    audio.save("voice.mp3")
    playsound.playsound("voice.mp3")

def execute_command(text):
    print("Texto reconhecido: " + text)
    text = text.lower()
    if "horas" in text:
        now = datetime.now()
        speak(f"Agora são {now.hour} horas e {now.minute} minutos")
    elif "aprendizado de máquina" in text:
        webbrowser.open("https://web.dio.me/home")
    elif "google" in text:
        webbrowser.open("https://www.google.com")
    elif "youtube" in text:
        webbrowser.open("https://www.youtube.com")
    elif "piada" in text:
        speak(pyjokes.get_joke())
    elif "python" in text:
        webbrowser.open("https://www.w3schools.com/python/python_reference.asp")
    elif "github" in text:
        webbrowser.open("https://github.com")
    elif "notícias ia" in text:
        webbrowser.open("https://bigbrain.beehiiv.com/")
    else:
        speak("Desculpe, não entendi o que você disse")

def main():
    while True:
        choice = input("Escolha uma opção:\n1 - Texto para áudio\n2 - Comandos por voz\n3 - Sair\n")
        if choice == "1":
            text_to_speech()
        elif choice == "2":
            print("I am listening...")
            command = recognize_speech()
            if command:
                execute_command(command)
        elif choice == "3":
            print("Encerrando assistente...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
