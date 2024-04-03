import pyautogui
import time

def sirayla_tikla(konumlar, tekrar_sayisi):
    for i in range(tekrar_sayisi):
        for konum in konumlar:
            pyautogui.click(konum)
            time.sleep(0.5)  # Her tıklamadan sonra kısa bir bekleme süresi

# Tıklama yapılacak konumlar (x, y) koordinatları şeklinde listelenir
tiklanacak_konumlar = [(100, 100), (200, 200), (300, 300)]  # Örnek konumlar

tekrar_sayisi = 3  # Her konum için kaç kez tıklama yapılacağı

while True:
    # Fonksiyonu çağırarak tıklamaları gerçekleştirin
    sirayla_tikla(tiklanacak_konumlar, tekrar_sayisi)
    
    # Her döngünün sonunda 15 dakika bekleyin (900 saniye)
    time.sleep(10)
