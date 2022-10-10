import requests

lista = []

sites = open('sites.txt', 'r')
for site in sites:
    lista.append(site.rstrip())
sites.close()

#print(lista)


for site in lista:
    try:
        x = requests.get('https://'+site)
        if x.status_code == 200:
            print(f'{site.capitalize()} : {x.status_code} OK')
        else:
            print(f'{site} : {x.status_code}')
    except:
        print(f"{site} unable to connect : {x.status_code}")