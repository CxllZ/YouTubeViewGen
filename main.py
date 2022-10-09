from ast import With
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from tqdm import tqdm
from threading import Thread
from atexit import register
import fade

user_agents = []
banner = """
▓██   ██▓ ▒█████   █    ██ ▄▄▄█████▓ █    ██  ▄▄▄▄   ▓█████     ██▒   █▓ ██▓▓█████  █     █░     ▄████ ▓█████  ███▄    █ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒▓  ██▒ ▓▒ ██  ▓██▒▓█████▄ ▓█   ▀    ▓██░   █▒▓██▒▓█   ▀ ▓█░ █ ░█░    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░▒ ▓██░ ▒░▓██  ▒██░▒██▒ ▄██▒███       ▓██  █▒░▒██▒▒███   ▒█░ █ ░█    ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
  ░ ▐██▓░▒██   ██░▓▓█  ░██░░ ▓██▓ ░ ▓▓█  ░██░▒██░█▀  ▒▓█  ▄      ▒██ █░░░██░▒▓█  ▄ ░█░ █ ░█    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
  ░ ██▒▓░░ ████▓▒░▒▒█████▓   ▒██▒ ░ ▒▒█████▓ ░▓█  ▀█▓░▒████▒      ▒▀█░  ░██░░▒████▒░░██▒██▓    ░▒▓███▀▒░▒████▒▒██░   ▓██░
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░▒▓███▀▒░░ ▒░ ░      ░ ▐░  ░▓  ░░ ▒░ ░░ ▓░▒ ▒      ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░    ░░▒░ ░ ░ ▒░▒   ░  ░ ░  ░      ░ ░░   ▒ ░ ░ ░  ░  ▒ ░ ░       ░   ░  ░ ░  ░░ ░░   ░ ▒░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░   ░       ░░░ ░ ░  ░    ░    ░           ░░   ▒ ░   ░     ░   ░     ░ ░   ░    ░      ░   ░ ░ 
 ░ ░         ░ ░     ░                 ░      ░         ░  ░         ░   ░     ░  ░    ░             ░    ░  ░         ░ 
 ░ ░                                               ░                ░                                                    
"""

bannerfin = """

  █████▒██▓ ███▄    █  ██▓  ██████  ██░ ██ ▓█████ ▓█████▄  ▐██▌ 
▓██   ▒▓██▒ ██ ▀█   █ ▓██▒▒██    ▒ ▓██░ ██▒▓█   ▀ ▒██▀ ██▌ ▐██▌ 
▒████ ░▒██▒▓██  ▀█ ██▒▒██▒░ ▓██▄   ▒██▀▀██░▒███   ░██   █▌ ▐██▌ 
░▓█▒  ░░██░▓██▒  ▐▌██▒░██░  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ░▓█▄   ▌ ▓██▒ 
░▒█░   ░██░▒██░   ▓██░░██░▒██████▒▒░▓█▒░██▓░▒████▒░▒████▓  ▒▄▄  
 ▒ ░   ░▓  ░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░ ▒▒▓  ▒  ░▀▀▒ 
 ░      ▒ ░░ ░░   ░ ▒░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░ ░ ▒  ▒  ░  ░ 
 ░ ░    ▒ ░   ░   ░ ░  ▒ ░░  ░  ░   ░  ░░ ░   ░    ░ ░  ░     ░ 
        ░           ░  ░        ░   ░  ░  ░   ░  ░   ░     ░    
                                                   ░            
"""

def progbar30():
    for i in tqdm(range(30)):
        sleep(1)

def progbar10():
    for i in tqdm(range(10)):
        sleep(0.25)

def main():
    counter = 0
    print(fade.greenblue(banner))
    print("Results May Be Inaccurate")

    # link = "https://www.youtube.com/watch?v=ZDbZ0zF3lTg"
    print("e.g. https://www.youtube.com/watch?v=ZDbZ0zF3lTg")
    link = input("Enter YouTube Video URL: ")

    with open("uas.txt", 'r') as f:
        f.seek(0)
        lines = f.readlines()

        for line in lines:
            opts = Options()
            # opts.add_argument(f"--mute-audio --log-level=OFF --user-agent={line}")
            opts.add_argument(f"--headless --mute-audio --log-level=OFF --user-agent={line}")

            driver = webdriver.Chrome(chrome_options=opts)

            driver.get(link);
            driver.implicitly_wait(10)

            print(fade.purplepink("Waiting To Click 'Accept Cookies'"))
            proggy10 = Thread(target=progbar10())
            proggy10.start()

            element = driver.find_element("css selector", '#content > div.body.style-scope.ytd-consent-bump-v2-lightbox > div.eom-buttons.style-scope.ytd-consent-bump-v2-lightbox > div:nth-child(1) > ytd-button-renderer:nth-child(2)')
            element.click()

            try:
                driver.implicitly_wait(10)
                element = driver.find_element("css selector", '#skip-button\:6 > span > button')
                element.click()
            except:
                pass

            print(fade.purplepink("Watching Video For 30 Seconds"))
            proggy30 = Thread(target=progbar30())
            proggy30.start()

            driver.quit()

            proggy10.join()
            proggy30.join()

            counter+=1
            print(f"Gave {counter} views to {link} With User Agent: {line}")

            with open('uas.txt', 'w') as fw:
                for g in lines:
                    # strip() is used to remove '\n'
                    # present at the end of each line
                    if g.strip('\n') != line:
                        fw.write(g)

    f.close()

    print(fade.greenblue(bannerfin))

if __name__ == '__main__':
    register(main)