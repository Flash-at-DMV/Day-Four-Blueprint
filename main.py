import requests
import os
from urllib.parse import urlparse, urljoin

def check_url(url = ""):
  url = url.strip().lower()
  try:
    parsed_url = url
    if not (url.startswith('//') or url.startswith('http://') or url.startswith('https://')):
      parsed_url = '//' + url

    parsed_url = urlparse(urljoin(parsed_url, "/"))._replace(scheme='http')
    
    if (all([parsed_url.scheme, parsed_url.netloc, parsed_url.path]) and len(parsed_url.netloc.split(".")) > 1):
      parsed_url = parsed_url.geturl()
    else:
      print(f"{url} is not a valid URL.")
      return
    
    result_status = requests.get(parsed_url, timeout=3).status_code

    if result_status == requests.codes.ok:
      print(f"{url} is up!")
    else:
      print(f"{url} is down!")
  except Exception:
    print(f"{url} is down!")
  

def main():
  os.system("clear")
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (seperated by comma)")

  urls = input().split(',')
  for url in urls:
    check_url(url)

  while True:
    try_again = input("Do you want to start over?(y/n)")

    if try_again == "y":
      main()
      break
    elif try_again == "n":
      print("k. bye!")
      break
    else:
      print("That's not a valid answer")

main()