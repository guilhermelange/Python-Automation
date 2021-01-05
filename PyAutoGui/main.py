import pyautogui as bot
import time
from PIL import Image

def locate():
    size = bot.size()
    #cordsChrome = pyautogui.locateCenterOnScreen("imagens/notepad.png")

    cordsChrome = bot.locateOnScreen('imagensOut/notepad.png', grayscale=True)
    cordsChrome = bot.center(cordsChrome)
    bot.moveTo(cordsChrome.x, cordsChrome.y, 0.5)
    bot.click(cordsChrome)
    time.sleep(1)
    bot.click(size.width/2, size.height/2)
    bot.write("   ")

    screen = bot.screenshot("imagensOut/screenTela.png")
    imageAux = Image.open("imagensOut/screenTela.png")
    imageAux = imageAux.convert(mode="L")
    imageAux.save("imagensOut/screenTela.png")
    locate = bot.locate('imagensOut/link1.png', "imagensOut/screenTela.png")
    print(locate)

    cordsLink1 = bot.locateOnScreen('imagensOut/link1.png', grayscale=True)
    cordsLink1 = bot.center(cordsLink1)
    bot.moveTo(cordsLink1.x, cordsLink1.y, 0.5)
    bot.click(cordsLink1)

if __name__ == '__main__':
    locate()