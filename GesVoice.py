import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import openai
import webbrowser
from translate import Translator
from io import BytesIO
import requests
import runpy
import pygame
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
import pyautogui
import webview
import threading
import pygetwindow as gw
import wikipedia
import pywhatkit as kit
import geocoder



class FirstEntry:
    def __init__(self, master):
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(fill='both', expand=True)
        self.master = master
        
        self.bg_image = ctk.CTkImage(Image.open("background.png"),size=(750, 500))
        self.bg_image_label = ctk.CTkLabel(self.frame, text="",image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)
        
        self.entry_frame = ctk.CTkFrame(self.frame,width=350,height=400)
        self.entry_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.title_label = ctk.CTkLabel(self.entry_frame, text="Baslarken",bg_color="transparent",fg_color="transparent",font=ctk.CTkFont(family="Helvatica",size=30))
        self.title_label.place(relx=0.5, y=10, anchor='n')
        
        self.name_label = ctk.CTkLabel(self.entry_frame, text="İsim")
        self.name_label.place(x=110,y=70)
        self.name_entry = ctk.CTkEntry(self.entry_frame)
        self.name_entry.place(relx=0.5, y=110, anchor='center')

        self.surname_label = ctk.CTkLabel(self.entry_frame, text="Soyisim")
        self.surname_label.place(x=110,y=130)
        self.surname_entry = ctk.CTkEntry(self.entry_frame)
        self.surname_entry.place(relx=0.5, y=170, anchor='center')

        self.asistan_name_label = ctk.CTkLabel(self.entry_frame, text="Asistan ismi")
        self.asistan_name_label.place(x=110,y=190)
        self.asistan_name_entry = ctk.CTkEntry(self.entry_frame)
        self.asistan_name_entry.place(relx=0.5, y=230, anchor='center')

        

        self.submit_button = ctk.CTkButton(self.entry_frame, text="Giriş",fg_color="#6c529e",
                                           hover_color="#55407e", command=self.check_info)
        self.submit_button.place(relx=0.5, y=280, anchor='center')

        self.logo_image = ctk.CTkImage(Image.open("logo.png"),size=(160, 60))
        self.logo_image_label = ctk.CTkLabel(self.entry_frame, text="",image=self.logo_image)
        self.logo_image_label.place(relx=0.5, y=340, anchor='center')

    def check_info(self):
        name = self.name_entry.get()
        name=name.capitalize()
        surname = self.surname_entry.get()
        surname=surname.capitalize()
        asistan_name = self.asistan_name_entry.get()
        asistan_name= asistan_name.capitalize()

        if not name or not surname or not asistan_name:
            error_label = ctk.CTkLabel(self.entry_frame, text="Lütfen tüm alanları doldurunuz!")
            error_label.place(relx=0.5, y=385, anchor='center')
            self.entry_frame.after(2000, error_label.destroy)
        elif not name.isalpha() or not surname.isalpha() or not asistan_name.isalpha():
            error_label = ctk.CTkLabel(self.entry_frame, text="Lütfen yalnızca harf giriniz!")
            error_label.place(relx=0.5, y=385, anchor='center')
            self.entry_frame.after(2000, error_label.destroy)
        else:            
            with open('config.txt', 'w') as f:
                f.write(f'İsim: {name}\n')
                f.write(f'Soyisim: {surname}\n')
                f.write(f'Asistan: {asistan_name}\n')
                self.start_welcome()
            
    def start_welcome(self):
        self.frame.destroy()
        Welcome(self.master)


class Welcome:
    def __init__(self, master):
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(fill='both', expand=True)
        self.master = master 
        self.name=" "
        

        with open('config.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'İsim:' in line:
                    self.name = line.split(':')[1]
                    

        self.bg_image = ctk.CTkImage(Image.open("background.png"),size=(750, 500))
        self.bg_image_label = ctk.CTkLabel(self.frame, text="",image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        
        self.welcome_frame = ctk.CTkFrame(self.frame,width=550,height=350)
        self.welcome_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        
        self.title_label = ctk.CTkLabel(self.welcome_frame, text=f"Hosgeldin{self.name}",bg_color="transparent",fg_color="transparent",font=ctk.CTkFont(family="Helvatica",size=40))
        self.title_label.place(relx=0.5, y=15, anchor='n')
        
        self.logo_image = ctk.CTkImage(Image.open("logo.png"),size=(180, 70))
        self.logo_image_label = ctk.CTkLabel(self.welcome_frame, text="",image=self.logo_image,bg_color = "transparent")
        self.logo_image_label.place(relx=0.5, y=270, anchor='n')
        
        button_font = ctk.CTkFont(family="Helvetica", size=20)
        self.button = ctk.CTkButton(self.welcome_frame, width=180,height=70, text="Başlat",font=button_font,
                                    fg_color="transparent",border_width=1.5,border_color="purple",hover_color="purple",
                                    command=self.start_main)
        self.button.place(relx=0.5, y=140, anchor='n')
        
    def start_main(self):
        self.frame.destroy()
        Main(self.master)

class Main:
    def __init__(self, master):
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(fill='both', expand=True)

        self.widgets_to_destroy = []

        with open('config.txt', 'r') as f:
            name_line = f.readlines()
            for line in name_line:
                if 'İsim:' in line:
                    self.name = line.split(':')[1]

        
        with open('config.txt','r') as f:
            asistan_line=f.readlines()
            for line2 in asistan_line:
                if 'Asistan:' in line2:
                    self.asistan_name=line2.split(':')[1].strip()


        self.logo_image = ctk.CTkImage(Image.open("logo.png"),size=(180, 70))
        self.logo_image_label = ctk.CTkLabel(self.frame, text="",image=self.logo_image)
        self.logo_image_label.place(x=20, y=25)

        button_font = ctk.CTkFont(family="Helvetica", size=15)
        self.button = ctk.CTkButton(self.frame, width=150,height=50, text="Sanal Fare'yi Başlat",font=button_font,fg_color="transparent",
                                    border_width=1.5,border_color="purple",hover_color="purple",
                                    corner_radius=50, command=self.virtual_mouse)
        self.button.pack()
        self.button.place(x=550,y=35)

        self.help_box_visible = False
        self.help_button = ctk.CTkButton(self.frame, width=10,height=10,text="yardım",fg_color="transparent",
                                        hover_color="gray",command=self.toggle_help_box)
        self.help_button.place(x=670, y=90)

        self.help_box = ctk.CTkTextbox(self.frame,width=150,height=400)
        self.help_box.insert("1.0","Çıkmak için 'esc' basın")
        self.help_box.configure(state="disabled")

        self.help_image = ctk.CTkImage(Image.open("move.png"),size=(120, 70))
        self.help_image_label = ctk.CTkLabel(self.help_box, text="",image=self.help_image)
        self.help_image_label.place(relx=0.5, y=30,anchor="n")

        self.help_image = ctk.CTkImage(Image.open("left.png"),size=(120, 70))
        self.help_image_label = ctk.CTkLabel(self.help_box, text="",image=self.help_image)
        self.help_image_label.place(relx=0.5, y=105,anchor="n")

        self.help_image = ctk.CTkImage(Image.open("right.png"),size=(120, 70))
        self.help_image_label = ctk.CTkLabel(self.help_box, text="",image=self.help_image)
        self.help_image_label.place(relx=0.5, y=175,anchor="n")

        self.help_image = ctk.CTkImage(Image.open("up.png"),size=(120, 70))
        self.help_image_label = ctk.CTkLabel(self.help_box, text="",image=self.help_image)
        self.help_image_label.place(relx=0.5, y=240,anchor="n")

        self.help_image = ctk.CTkImage(Image.open("down.png"),size=(120, 60))
        self.help_image_label = ctk.CTkLabel(self.help_box, text="",image=self.help_image)
        self.help_image_label.place(relx=0.5, y=310,anchor="n")

        self.radiobutton_frame = ctk.CTkFrame(self.frame,width=200,height=500)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(130, 0), sticky="n")
        self.radio_var = tk.IntVar(value=0)
        self.label_radio_group = ctk.CTkLabel(self.radiobutton_frame, text="Asistan Modları:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="n")
        self.radio_button_1 = ctk.CTkRadioButton(self.radiobutton_frame, text="Sesli Asistan", variable=self.radio_var, value=1, command=self.page1)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = ctk.CTkRadioButton(self.radiobutton_frame, text="ChatGpt", variable=self.radio_var, value=2, command=self.page2)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = ctk.CTkRadioButton(self.radiobutton_frame, text="Dall-E", variable=self.radio_var, value=3, command=self.page3)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20)
        self.radio_button_4 = ctk.CTkRadioButton(self.radiobutton_frame, text="Diğer", variable=self.radio_var, value=4, command=self.page4)
        self.radio_button_4.grid(row=4, column=2, pady=10, padx=20, sticky="n")


    def virtual_mouse(self):
        def start_virtual_mouse():
            runpy.run_path("sanalfare.py")
            
        def start_osk():
            os.system('osk')
        
        thread = threading.Thread(target=start_virtual_mouse)
        thread.start()

        thread2 = threading.Thread(target=start_osk)
        thread2.start()

    def toggle_help_box(self):
        if self.help_box_visible:
            self.help_box.place_forget()
        else:
            self.help_box.place(x=600, y=120)
            self.help_box.lift() 
        self.help_box_visible = not self.help_box_visible



    def page1(self):
        
        for widget in self.widgets_to_destroy:
            widget.destroy()
        self.widgets_to_destroy = []
        
        self.asistan_frame = ctk.CTkFrame(self.frame,width=400,height=350)
        self.asistan_frame.place(x=185,y=130)
        self.widgets_to_destroy.append(self.asistan_frame)

        self.asistan_status = False
        self.asistan_button = ctk.CTkButton(self.asistan_frame,width=120,height=40,text="Asistanı Başlat",fg_color="transparent",
                                    border_width=1.5,border_color="#6c529e",hover_color="#6c529e",
                                    corner_radius=50, command=self.asistan)
        self.asistan_button.place(x=10, y=20)
        self.widgets_to_destroy.append(self.asistan_button)
        

        self.text_box_visible = False
        self.info_image = ctk.CTkImage(Image.open("info.png"),size=(20, 20))
        self.info_button = ctk.CTkButton(self.frame, width=10,height=10,image=self.info_image, text="",fg_color="transparent",
                                        hover_color="gray",command=self.toggle_text_box)
        self.info_button.place(x=552, y=130)
        self.widgets_to_destroy.append(self.info_button)

        self.text_box1 = ctk.CTkTextbox(self.asistan_frame,width=400,height=300)
        self.text_box1.place(x=0,y=80)
        self.widgets_to_destroy.append(self.text_box1)

        self.text_box = ctk.CTkTextbox(self.frame,width=150,height=370)
        self.text_box.insert("1.0", f"""KOMUTLAR:
                             
{self.asistan_name}: Bu komut 
asistanın başlamasını 
sağlar

-Hangi gündeyiz: 
Günü söyler

-Saat kaç: 
Saati söyler

-Google'da ara: 
Google'da arama yapar

-Uygulama aç: 
Uygulama açar

-Not et:
Söylediklerinizi kaydeder

-Not aç:
İstediğiniz notu açar

-Not oku:
İstediğiniz notu okur

-Numara ara:
Telefon Bağlantıları uygulamasını açarak numarayı arar

-Ses kaydı al:
Ses kaydını başlatır

-Araştır:
İstenilen konuyu internette araştırır

-Numara ekle:
Numara ekler

-Mesaj at:
Eklenilen numaraya mesaj atar

-Müzik aç:
Müzik açar

-Video aç:
Video açar

-Hava durumu:
Hava durumunu söyler

-Hatırlatıcı oluştur:
Hatırlatıcı oluşturur

-Hatırlatıcı Kaldır:
Oluşturulan hatırlatıcıyı kaldırır

-Ses aç:
Sistem sesini açar

-Ses kapat:
Sistem sesini kapatır

-Masaüstü:
Masaüstüne geçer

-Kapat:
Açık olan pencereyi kapatır

-Alt tab:
Sekme değiştirir

-Bilgisayarı kapat:
Bilgisayarı belirtilen sürede kapatır.

-Bilgisyarı yeniden başlat:
Bilgisayarı yeniden başlatır
""") 
        self.text_box.configure(state="disabled")  
        self.widgets_to_destroy.append(self.text_box)

        self.reminder_box_visible = False
        self.reminder_button = ctk.CTkButton(self.frame, width=30,height=30,text="Hatırlatıcı",fg_color="#6c529e",
                                    hover_color="#55407e",command=self.toggle_reminder_box)
        self.reminder_button.place(x=510, y=170)

        self.reminder_box = ctk.CTkTextbox(self.frame,width=150,height=370)
        self.reminder_box.insert("1.0"," ")
        self.reminder_box.configure(state="disabled")
        self.widgets_to_destroy.append(self.reminder_box)
        
    def shutdown_time(wt):
        time.sleep(wt)
        os.system('shutdown -s')

    def toggle_text_box(self):
        if self.text_box_visible:
            self.text_box.place_forget()
        else:
            self.text_box.place(x=600, y=120)
        self.text_box_visible = not self.text_box_visible

    def toggle_reminder_box(self):
        if self.reminder_box_visible:
            self.reminder_box.place_forget()
        else:
            self.reminder_box.place(x=600, y=120)
        self.reminder_box_visible = not self.reminder_box_visible

    def asistan(self):
        if not self.asistan_status:
            self.asistan_status = True
            self.r = sr.Recognizer()
            pygame.mixer.init()
            thread = threading.Thread(target=self.start)
            thread.start()
        else:
            self.asistan_status = False
        
    def start(self):
        while self.asistan_status:
            wake = self.record()
            if wake != '':
                wake = wake.lower()
                wake = wake.capitalize()  
                self.test(wake)
               
    def test(self,wake):
        global voice
        if self.asistan_name in wake:
            self.speak(f"Seni dinliyorum{self.name}")
            while True:
                voice=self.record()
                if voice!= '':
                    voice=voice.lower()
                    voice = voice.capitalize() 
                    self.responce(voice)        
                        
    def record(self):
        while True: 
            with sr.Microphone() as source:
                self.text_box1.configure(state="normal")
                self.text_box1.insert("end", "Dinleniyor...\n")
                self.text_box1.configure(state="disabled")
                self.r.adjust_for_ambient_noise(source, duration=0.9)
                audio = self.r.listen(source)
            voice = ''
            try:
                voice = self.r.recognize_google(audio, language='tr-TR')
                self.text_box1.configure(state="normal")
                self.text_box1.insert("end", "Söylediğiniz: {}\n".format(voice))
                self.text_box1.configure(state="disabled")
            except:
                self.text_box1.configure(state="normal")
                self.text_box1.insert("end", "Üzgünüm, ne dediğinizi anlayamadım? {}\n".format(voice))
                self.text_box1.configure(state="disabled")
            return voice
    
    def speak(self,string):
        tts = gTTS(text=string, lang='tr')
        filename = "answer.mp3"
        tts.save(filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        os.remove(filename)
        
    def responce(self,voice):
        if "Görüşürüz" in voice:
            self.speak("Görüşürüz")
            exit()
        if "Hangi gündeyiz" in voice:
            today = time.strftime("%A")
            today = today.capitalize() 
            if today == "Monday":
                today = "Pazartesi" 
            elif today == "Tuesday":
                today = "Salı"
            elif today == "Wednesday":
                today = "Çarşamba"
            elif today == "Thursday":
                today = "Perşembe"
            elif today == "Friday":
                today = "Cuma"
            elif today == "Saturday":
                today = "Cumartesi"
            elif today == "Sunday":
                today = "Pazar"
            self.speak(today)
        if "Saat kaç" in voice:
            selection = ["Saat şuan:", "Hemen bakıyorum:"]  
            clock = datetime.now().strftime("%H:%M")  
            chosen_phrase = random.choice(selection)  
            self.speak(chosen_phrase + clock)
        if "Google'da ara" in voice:
            self.speak("Ne aramamı istersin")
            search = self.record()
            url="https://www.google.com/search?q={}".format(search)
            webbrowser.get().open(url)
            self.speak("{}içi Google'da bulabildiklerimi listeliyorum.".format(search))
        if "Uygulama aç" in voice:
            self.speak("Hangi uygulamayı açmamı istiyorsun?")
            app_name = self.record().lower()
            self.speak("{} uygulamasını açıyorum".format(app_name))
            time.sleep(0.5)
            pyautogui.press('win')
            time.sleep(0.5)
            pyautogui.write(app_name)
            time.sleep(0.5)
            pyautogui.press('enter') 
        if 'Not al' in voice:
            self.speak("Notun adı ne olsun?")
            filename = self.record()
            self.speak("Neyi kaydetmek istersiniz?")
            note = self.record()
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'OneDrive','Masaüstü') 
            file_path = os.path.join(desktop, filename + ".txt")
            with open(file_path, "w") as f:
                f.write(note)
            self.speak("Notunuz kaydedildi")
        if 'Not aç' in voice:
            self.speak("Hangi notu açmamı istersiniz")
            note_name = self.record()
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'OneDrive','Masaüstü') 
            file_path = os.path.join(desktop, note_name + ".txt")
            if os.path.isfile(file_path):
                os.system(file_path)
            else:
                self.speak("Üzgünüm, notunuz masaüstünde kayıtlı değil.")
        if 'Not oku' in voice:
            self.speak("Hangi notu okumamı istersin?")
            file = self.record()
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'OneDrive','Masaüstü') 
            file_path = os.path.join(desktop, file + ".txt")
            if os.path.isfile(file_path):
                self.speak("Hemen okuyorum")
                file_open = open(file_path)
                icerik = file_open.read()
                self.speak(icerik)
                file_open.close()
            else:
                self.speak("Üzgünüm, notunuz masaüstünde kayıtlı değil.")
        if "Numara ara" in voice:
            pyautogui.press('win')
            time.sleep(0.5)
            pyautogui.write("Telefon")
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(3)
            phone_window = None
            for window in gw.getAllWindows():
                if window.title=="Telefon Bağlantısı":
                    phone_window = window
                    window.maximize()
            time.sleep(1)
            pyautogui.press('alt')
            time.sleep(0.5)
            pyautogui.press('3')
            self.speak("Kimi aramamı istersin?")
            name=self.record()
            self.speak("Hemen arıyorum")
            pyautogui.leftClick(1600,200)
            pyautogui.write(name, interval=0.1)
            pyautogui.press('enter')
            pyautogui.press('tab')
            time.sleep(0.5)
            for i in range(4):
                pyautogui.press('down')
            pyautogui.press('enter')
        if "Ses kaydı al" in voice:
            pyautogui.press('win')
            time.sleep(0.5)
            pyautogui.write("Ses Kaydedici")
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(3)
            self.speak("Ses kaydını başlatıyorum.")
            pyautogui.press('alt')
            pyautogui.press('r')
        if "Araştır" in voice:
            self.speak("Hangi konuyu araştırmamı istersiniz?")
            topic = self.record()
            wikipedia.set_lang("tr")
            summary = wikipedia.summary(topic, sentences=2)
            self.speak("İşte bulduğum sonuç")
            self.text_box1.configure(state="normal")
            self.text_box1.insert("end", summary,"\n")
            self.text_box1.configure(state="disabled")
        if "Numara ekle" in voice:
            self.speak("Numaranın ismi ne olsun?")
            numbers_name=self.record()
            self.speak("Numarayı söyleyiniz ")
            number=self.record()
            with open('numbers.txt', 'a') as f:
                f.write(f'{numbers_name}: {number}\n')
            self.speak("Yeni numara eklendi")
        if "Mesaj at" in voice:
            self.speak("Kime mesaj göndermek istiyorsunuz?")
            person=self.record()
            with open('numbers.txt', 'r') as f:
                for line in f:
                    name, number = line.strip().split(': ')
                    if name == person:
                        person_number ='+90'+number
                        break
            self.speak("Mesajınız söyleyiniz")
            msg=self.record()
            kit.sendwhatmsg_instantly(person_number, msg, wait_time=5)
            time.sleep(5)
            pyautogui.press('enter')
            self.speak("Mesaj gönderildi")
        if "Müzik aç" in voice:
            self.speak("Müzik veya sanatçı ismi söyleyiniz")
            songOrArtisit= self.record()
            kit.playonyt(songOrArtisit)
        if "Video aç" in voice:
            self.speak("Video ismini söyleyiniz")
            video= self.record()
            kit.playonyt(video)
        if "Hava durumu" in voice:
            g = geocoder.ip('me')
            url = f"https://wttr.in/{g.city}?format=%C+%t&lang=tr"
            response = requests.get(url)
            self.speak(f"{g.city} için bugün hava {response.text}")
        if "Hatırlatıcı oluştur" in voice:
            self.speak("Hatırlatma mesajını söyleyiniz")
            reminder_msg = self.record()
            self.speak("Hatırlatma tarihini söyleyiniz")
            reminder_date = self.record()
            self.speak("Hatırlatma saatini söyleyiniz")
            reminder_hour = self.record()
            self.reminder_box.configure(state="normal") 
            self.reminder_box.insert("end", "\nHatırlatma Tarihi: " + reminder_date)
            self.reminder_box.insert("end", "\nHatırlatma Saati: " + reminder_hour)
            self.reminder_box.insert("end", "\nHatırlatma Mesajı: " + reminder_msg)
            self.reminder_box.configure(state="disabled")  
        if "Hatırlatıcı Kaldır" in voice:
            self.reminder_box.configure(state="normal") 
            self.reminder_box.delete("1.0", "end") 
            self.reminder_box.configure(state="disabled")
        if "Ses aç" in voice:
            os.system("amixer -D pulse sset Master 80%")
        if "Ses kapat" in voice:
            os.system("amixer -D pulse sset Master 0%")
        if "Masaüstü" in voice:
            pyautogui.hotkey('win', 'd')
        if "Kapat" in voice:
            pyautogui.hotkey('alt', 'f4') 
        if "Alt tab" in voice:
            pyautogui.hotkey('alt', 'tab')
        if "Bilgisayarı kapat" in voice:
            self.speak("Bilgisayar ne zaman kapansın istiyorsunuz?")
            shutdown=self.record()
            if shutdown=='Şimdi':
                os.system('shutdown -s')
            else:
                self.speak("Kaç saat sonra kapansın")
                hour = self.record()
                self.speak("Kaç dakika sonra kapansın")
                minute = self.record()
                now = datetime.datetime.now()
                shutdown_time = now + datetime.timedelta(hours=hour, minutes=minute)
                wait_time = (shutdown - now).total_seconds()
                self.shutdown_time(wait_time)
        if "Bilgisyarı yeniden başlat" in voice:
            self.speak("Emin misiniz?")
            yes=self.record()
            if yes=='Evet':
                os.system("shutdown /r /t 1")
        


    def page2(self):
        openai.api_key = " " #chatgpt kullanmak için openai sitesinden kendinize bir key oluşturabilirsiniz
        for widget in self.widgets_to_destroy:
            widget.destroy()
        self.widgets_to_destroy = []
        
        pygame.mixer.init()
        
        self.chat_frame = ctk.CTkFrame(self.frame,width=400,height=350)
        self.chat_frame.place(x=185,y=130)
        self.widgets_to_destroy.append(self.chat_frame)

        self.chat_log = ctk.CTkTextbox(self.chat_frame,width=400,height=350)
        self.chat_log.grid()
        self.chat_log.configure(state="disabled")

        mic_image = Image.open("mic.png")
        self.photoImg = ctk.CTkImage(mic_image)

        self.img_button = ctk.CTkButton(self.chat_frame,text="", fg_color="transparent",image=self.photoImg, width=20, 
                                        height=20,hover_color="gray",command=self.on_button_click2)
        self.img_button.place(x=0, y=321)

        self.msg_entry = ctk.CTkEntry(self.chat_frame,width=300,height=30)
        self.msg_entry.bind("<Return>", self.on_button_click)
        self.msg_entry.grid()
        self.msg_entry.place(x=40, y=321)
        
        self.button_clicked = False
        self.send_button = ctk.CTkButton(self.chat_frame, width=30,height=28,text="Gönder", fg_color="transparent",
                                         hover_color="gray",border_width=1.5,border_color="gray" ,command=self.on_button_click)
        self.send_button.place(x=345,y=321)  
    
    def on_button_click(self,event=None):
        self.button_clicked = True
        thread = threading.Thread(target=self.send_message_chatgpt)
        thread.start()
        
    def send_message_chatgpt(self, event=None, msg=None):
        if msg is None:
            msg = self.msg_entry.get()
        if msg != "":
            self.chat_log.configure(state="normal")
            self.chat_log.insert("end", "You: " + msg + "\n")
            self.chat_log.configure(state="disabled")
            self.msg_entry.delete(0, "end")
            self.button_clicked = True
            if self.button_clicked == True:
                self.receive_message_chatgpt(msg)
                self.button_clicked = False

    def receive_message_chatgpt(self, msg):
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": msg},
            ]
        )
        response_text = response['choices'][0]['message']['content']
        self.chat_log.configure(state="normal")
        self.chat_log.insert("end", "ChatGpt: " + response_text + "\n")
        self.chat_log.configure(state="disabled")
        return response_text

    def on_button_click2(self):
        thread = threading.Thread(target=self.activate_voice_mode)
        thread.start()

    def activate_voice_mode(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.chat_log.configure(state="normal")
            self.chat_log.insert("end", "You: " + "Sizi Dinliyorum..." + "\n")
            self.chat_log.configure(state="disabled")
            audio = r.listen(source)
            text = r.recognize_google(audio, language='tr-TR')
            
            self.send_message_chatgpt(text)
            tts = gTTS(text=self.receive_message_chatgpt(text), lang='tr')
            tts.save("response.mp3")
            pygame.mixer.music.load("response.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.music.unload()
            os.remove("response.mp3")
            


    def page3(self):
        for widget in self.widgets_to_destroy:
            widget.destroy()
        self.widgets_to_destroy = []

        self.dalle_frame = ctk.CTkFrame(self.frame,width=400,height=350)
        self.dalle_frame.place(x=185,y=130)
        self.widgets_to_destroy.append(self.dalle_frame)

        self.prompt_entry = ctk.CTkEntry(self.dalle_frame,width=300,height=30)
        self.prompt_entry.bind("<Return>", self.create_image_dalle)
        self.prompt_entry.grid()
        self.prompt_entry.place(x=41.5, y=321)

        self.create_button = ctk.CTkButton(self.dalle_frame, width=31,height=28,text="Oluştur", fg_color="transparent",
                                           hover_color="gray",border_width=1.5,border_color="gray",command=self.on_button_click3)
        self.create_button.place(x=344,y=321)
        
        self.download_button = ctk.CTkButton(self.dalle_frame, width=30,height=28,text="İndir", fg_color="transparent",
                                           hover_color="gray",border_width=1.5,border_color="gray",command=self.download_image)
        self.download_button.place(x=0,y=321)

    def on_button_click3(self):
        thread = threading.Thread(target=self.create_image_dalle)
        thread.start()

    def create_image_dalle(self, event=None):
        global image_url
        openai.api_key = " " #dall-e kullanmak için openai sitesinden kendinize bir key oluşturabilirsiniz
        prompt = self.prompt_entry.get()
        if prompt != "":
            self.prompt_entry.delete(0, "end")
            translator = Translator(from_lang='tr', to_lang='en')
            translated_prompt = translator.translate(prompt)
            response = openai.Image.create(
                model = "dall-e-2",
                prompt = translated_prompt,
                n=1,
                size="256x256"
            )
            image_url = response.data[0].url
            response = requests.get(image_url)
            img_data = response.content
            self.image = ctk.CTkImage(Image.open(BytesIO(img_data)), size=(256,256))
            self.image_label = ctk.CTkLabel(self.dalle_frame, text="",image=self.image)
            self.image_label.place(relx=0.5, rely=0.5, anchor='center')
    
    def download_image(self): 
        try:
            webbrowser.open(image_url)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1)
            pyautogui.hotkey('enter')
            error_label = ctk.CTkLabel(self.dalle_frame, text="Resim indirildi!")
            error_label.place(x=5, y=290)
            self.dalle_frame.after(2000, error_label.destroy)
        except:
            error_label = ctk.CTkLabel(self.dalle_frame, text="Resim bulunamadı!")
            error_label.place(x=5, y=290)
            self.dalle_frame.after(2000, error_label.destroy)
    


    def page4(self):
        self.others_frame = ctk.CTkFrame(self.frame,width=400,height=350)
        self.others_frame.place(x=185,y=130)
        self.widgets_to_destroy.append(self.others_frame)
        
        self.free_label = ctk.CTkLabel(self.others_frame, text="Diğer Yapay Zekalar",bg_color="transparent",fg_color="transparent",font=ctk.CTkFont(family="Helvatica",size=15))
        self.free_label.place(x=10, y=8)

        self.button1 = ctk.CTkButton(self.others_frame, width=150,height=45, text="Blackbox", text_color="white", fg_color="#6c529e",
                                    hover_color="#55407e", command=self.blackbox)
        self.button1.place(x=30,y=50)
        self.button2 = ctk.CTkButton(self.others_frame, width=150,height=45, text="Auto Write", text_color="white", fg_color="#6c529e",
                                    hover_color="#55407e", command=self.autowrite)
        self.button2.place(x=220,y=50)
        self.button3 = ctk.CTkButton(self.others_frame, width=150,height=45, text="Copilot", text_color="white", fg_color="#6c529e",
                                    hover_color="#55407e", command=self.copilot)
        self.button3.place(x=30,y=120)
        self.button4 = ctk.CTkButton(self.others_frame, width=150,height=45, text="Logo ai", text_color="white", fg_color="#6c529e",
                                    hover_color="#55407e", command=self.logoai)
        self.button4.place(x=220,y=120)
        self.button5 = ctk.CTkButton(self.others_frame, width=150,height=45, text="Deep ai", text_color="white", fg_color="#6c529e",
                                    hover_color="#55407e", command=self.deepai)
        self.button5.place(x=30,y=190)
        self.button6 = ctk.CTkButton(self.others_frame, width=150,height=45, text="DeepL", text_color="white", fg_color="#6c529e",
                                    hover_color="#55407e", command=self.deepl)
        self.button6.place(x=220,y=190)
        self.button7 = ctk.CTkButton(self.others_frame, width=150,height=45, text="Kome", text_color="white", fg_color="#6c529e",
                                    hover_color="#55407e", command=self.kome)
        self.button7.place(x=30,y=260)
        self.button7 = ctk.CTkButton(self.others_frame, width=150,height=45, text="Quillbot", text_color="white", fg_color="#6c529e",
                                    hover_color="#55407e", command=self.quillbot)
        self.button7.place(x=220,y=260)

        self.text_box2_visible = False
        self.info_image = ctk.CTkImage(Image.open("info.png"),size=(20, 20))
        self.info2_button = ctk.CTkButton(self.frame, width=10,height=10,image=self.info_image, text="",fg_color="transparent",
                                        hover_color="gray",command=self.toggle_text_box2)
        self.info2_button.place(x=552, y=130)
        self.widgets_to_destroy.append(self.info2_button)

        self.text_box2 = ctk.CTkTextbox(self.frame,width=150,height=370)
        self.text_box2.insert("1.0", f"""
BlackBox: Kod yazar
                              
Autowrite: Yaratıcı 
metinler oluşturur

Copilot: Sohbet 
botudur

Logo ai: Logo 
oluşturur

Deep ai: Yaratıcı 
çizimler yapar

DeepL: Çeviri yapar
                              
Kome: Youtube 
videolarının
metnini çıkartır
                              
Quillbot: Profesyonel 
yazı yazmayı sağlar
                              
""") 
        self.text_box2.configure(state="disabled") 
        self.widgets_to_destroy.append(self.text_box2)

    def toggle_text_box2(self):
        if self.text_box2_visible:
            self.text_box2.place_forget()
        else:
            self.text_box2.place(x=600, y=120)
        self.text_box2_visible = not self.text_box2_visible

    def blackbox(self):
        webview.create_window('Blackbox', 'https://www.blackbox.ai/')
        webview.start()
        
    def autowrite(self):
        webview.create_window('Auto Write', 'https://autowrite.app/')
        webview.start()
        
    def copilot(self):
        webview.create_window('Copilot', 'https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=undexpand')
        webview.start()
    
    def logoai(self):
        webview.create_window('Logo ai', 'https://www.logoai.com/logo-maker')
        webview.start()
    
    def deepai(self):
        webview.create_window('Deep ai', 'https://deepai.org/')
        webview.start()
        
    def deepl(self):
        webview.create_window('DeepL', 'https://www.deepl.com/en/translator')
        webview.start()
    
    def kome(self):
        webview.create_window('Kome', 'https://kome.ai/tools/youtube-transcript-generator')
        webview.start()
    
    def quillbot(self):
        webview.create_window('Quillbot', 'https://quillbot.com/')
        webview.start()

         
  
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("750x500")
    root.title("GesVoice")
    root.resizable(width="FALSE",height="FALSE")
    
    if not os.path.exists('config.txt'):
        Main_app = FirstEntry(root)
    else:
        Main_app = Welcome(root)
        
    root.mainloop()

    