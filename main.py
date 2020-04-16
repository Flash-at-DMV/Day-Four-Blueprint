import requests
import os
from urllib.parse import urlparse, urljoin

def validate_url(url = ""):
  parsed_url = url.lower()
  if not (url.startswith('//') or url.startswith('http://') or url.startswith('https://')):
    parsed_url = '//' + url.lower()

  parsed_url = urlparse(urljoin(parsed_url, "/"))._replace(scheme='http')
  
  if (all([parsed_url.scheme, parsed_url.netloc, parsed_url.path]) and len(parsed_url.netloc.split(".")) > 1):
    return parsed_url.geturl()
  
  return False

def check_url(url = ""):
  url = url.strip()
  parsed_url = validate_url(url)

  if parsed_url is False:
    print(f"{url} is not a valid URL.")
    return

  try:
    result_status = requests.get(parsed_url, timeout=3).status_code

    if result_status == requests.codes.ok:
      print(f"{url} is up!")
    else:
      print(f"{url} is down!")

  except Exception:
    print(f"{url} is down!")

def ask_to_try_again():
  answer = input("Do you want to start over?(y/n)")

  if answer == "y" or answer == "n":
    return answer

  print("That's not a valid answer")
  ask_to_try_again()
  
def main():
  os.system("clear")
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (seperated by comma)")

  urls = input().split(',')
  for url in urls:
    check_url(url)

  if ask_to_try_again() == "y":
    main()
  else:
    print("k. bye!")

main()