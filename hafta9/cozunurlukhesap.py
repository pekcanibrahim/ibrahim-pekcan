import pyautogui

# Ekran çzöünürlüğü
screenWidth, screenHeight = pyautogui.size()
print("Ekran Çzözünürlüğü :", screenWidth, screenHeight)

# Fare durumu
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
