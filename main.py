







import random, string, requests, time

print("┏━━━┳━━━┳┓┏━┳━━━┳┓╋┏┓┏━━━┳━━━┳━┓╋┏┓\n┗┓┏┓┃┏━┓┃┃┃┏┫┏━┓┃┃╋┃┃┃┏━┓┃┏━━┫┃┗┓┃┃\n╋┃┃┃┃┃╋┃┃┗┛┛┃┗━━┫┗━┛┃┃┃╋┗┫┗━━┫┏┓┗┛┃\n╋┃┃┃┃┗━┛┃┏┓┃┗━━┓┃┏━┓┃┃┃┏━┫┏━━┫┃┗┓┃┃\n┏┛┗┛┃┏━┓┃┃┃┗┫┗━┛┃┃╋┃┃┃┗┻━┃┗━━┫┃╋┃┃┃\n┗━━━┻┛╋┗┻┛┗━┻━━━┻┛╋┗┛┗━━━┻━━━┻┛╋┗━┛\n")

getkeys = requests.get("https://heartfeltlastcomments.dakshkain.repl.co").text

free = getkeys.split("|")[0]

prem = getkeys.split("|")[1]

keys = (free, prem)

print("Join https://discord.gg/RakePQ559v & Get Your Free Trial KEY For Generator!")

print("Message @- Daksh. 🖤#0001 Discord/@Daksh1028 Telegram To Purchase Premium")

def main():

  while True:

     bin1 = random.choice(["3", "4", "5", "6"])

     n = random.randint(5, 11)

     bin2 = ''.join(random.choices(string.digits, k=n))

     bin = f"{bin1}{bin2}"

     url = f"https://lookup.binlist.net/{bin}"

     response = requests.get(url)

    

     try:

       if response.status_code == 200:

         data = response.json()

         if data['bank']:

           print(f"\n✅ Fetched Valid BIN\n• BIN: {bin}\n• Bin Information:\n  ↳ Card: {data['scheme']}\n  ↳ Type: {data['type']}\n  ↳ Level: {data['brand']}\n  ↳ Bank:\n    ↳ {data['bank']['name']}\n  ↳ Country:\n    ↳ {data['country']['name']}\n• Prepaid: {data['prepaid']}")

           break

    

     except KeyError:

       pass

    

access = input("Enter KEY: ")

    

if access in keys:

  if access == free:

    print(f"\nEntered Valid KEY! {access}\nVersion: free")

    time.sleep(2.5)

    print("\nGenerating 1x BIN For You...")

    main()

  

  elif access == prem:

    print(f"\nEntered Valid KEY! {access}\nVersion: prem")

    time.sleep(1)

    num = int(input("\nNumber of Bins: "))

    for i in range(num):

      main()

      

else:

  print("Wrong KEY Entered!")



/



22 
