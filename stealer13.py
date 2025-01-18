import selenium
import selenium.webdriver
import colorama
from colorama import Fore
colorama.init()










print(Fore.RED + "MADE BY M0EXIS" + "\n"*5)

print("╔═══╗╔════╗╔═══╗╔═══╗╔╗───╔═══╗╔═══╗─╔╗─╔═══╗\n║╔═╗║║╔╗╔╗║║╔══╝║╔═╗║║║───║╔══╝║╔═╗║╔╝║─║╔═╗║\n║╚══╗╚╝║║╚╝║╚══╗║║─║║║║───║╚══╗║╚═╝║╚╗║─╚╝╔╝║\n╚══╗║──║║──║╔══╝║╚═╝║║║─╔╗║╔══╝║╔╗╔╝─║║─╔╗╚╗║\n║╚═╝║──║║──║╚══╗║╔═╗║║╚═╝║║╚══╗║║║╚╗╔╝╚╗║╚═╝║\n╚═══╝──╚╝──╚═══╝╚╝─╚╝╚═══╝╚═══╝╚╝╚═╝╚══╝╚═══╝" + '\n'*4)






driver = selenium.webdriver.Chrome()
driver.get(input("Enter url:"))
print(Fore.RED + "getting cookies...")
cookies  = driver.get_cookies()

print(cookies)

text_c = ''
for el in cookies:
    for key in el:
        text_c = text_c + f"{key}:{el[key]}; "


with open("cookies.txt", "a", encoding="utf-8") as f:
    f.write(text_c)




print(Fore.RED + "work finished")