import requests
import time
from bs4 import BeautifulSoup
from colorama import Fore , init , Style
links_file=open("links.txt","w")
link_count=0
init()
def extracting_all_links(url_req):
        global link_count
        try:
            response = requests.get(url_req).content
            html_soup = BeautifulSoup(response, 'html.parser')
            all_html_a = html_soup.find_all('a')
            for links in all_html_a:
                if ('href') in links.attrs:
                    linkss = links['href']
                    if ("https://") in linkss or ("www.") in linkss or ("http") in linkss:
                        link_count+=1
                        links_file.write(linkss+"\n")
                        print(linkss)
            links_file.close()
            init()
            print(f"{Fore.GREEN}[+] Finished Links : {link_count}{Style.RESET_ALL}")
            input("[!] Thanks For Using ..")
            exit(0)
        except Exception:
            input("Error To URL !")
print(f'''{Fore.YELLOW} |----------------------------------------|
 |     [ Extractor Links In Website ]        |
 |    ----Github : TNALotaibi----         |
 |----------------------------------------|                                 
''')
print(f'''{Fore.YELLOW}[?] get -s target   <---- if website encryption ( https:// ) \n[?] get -n target   <---- if website not encryption ( http:// ){Style.RESET_ALL}\n''')
print(f"{Fore.YELLOW}[+] Enter ")
command = input("--> ")
if not command.find("get -s"):
    spp = command.split(" -s ")[1]
    url_requests = f'https://{spp}'
    for _ in ["|", "/", "-", "\\", "|", "/", "-", "\\"]:
        time.sleep(0.2)
        print(f"{Style.RESET_ALL}{Fore.LIGHTRED_EX}[{_}] Please wait .. {url_requests}{Style.RESET_ALL}",end="\r")
    extracting_all_links(url_requests)
elif not command.find("get -n"):
    url_requests = f'http://{command.split(" -n ")[1]}'
    for _ in ["|", "/", "-", "\\", "|", "/", "-", "\\"]:
        time.sleep(0.2)
        print(f"{Style.RESET_ALL}{Fore.LIGHTRED_EX}[{_}] Please wait .. {url_requests}{Style.RESET_ALL}",end="\r")
    extracting_all_links(url_requests)
else:
    input("Enter valid command !")
    exit(0)
