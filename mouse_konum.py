import pyautogui

print("Program fare koordinatlarını gösteriyor. Çıkmak için CTRL+C'ye basın.")

try:
    while True:
        x, y = pyautogui.position()
        print("Mouse koordinatları: x =", x, ", y =", y)
        pyautogui.sleep(1)  # Her saniye kontrol etmek için bir saniye bekleyin

except KeyboardInterrupt:
    print("\nProgram kapatıldı.")