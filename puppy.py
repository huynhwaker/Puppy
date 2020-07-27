from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

my_url = 'https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals.aspx?species=Dog&gender=A&agegroup=UnderYear&location=&site=&onhold=A&orderby=name&colnum=3&css=http://ws.petango.com/WebServices/adoptablesearch/css/styles.css&authkey=io53xfw8b0k2ocet3yb83666507n2168taf513lkxrqe681kf8&recAmount=&detailsInPopup=No&featuredPet=Include&stageID=&wmode=opaque'

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

#grabs each puppy record
containers = page_soup.findAll("td",{"class":"list-item"})

container = containers[0]
#name_container = container.findAll("div", {"class":"list-animal-name"})

for container in containers:
    if container.div is None:
        pass
    else:
        picture = container.div.a.img["src"]
    name_container = container.find("div", {"class":"list-animal-name"})
    id_container = container.find("div", {"class":"list-animal-id"})
    gender_container = container.find("div", {"class":"list-animal-sexSN"})
    breed_container = container.find("div", {"class":"list-animal-breed"})
    age_container = container.find("div", {"class":"list-animal-age"})
    location_container = container.find("div", {"class":"hidden"})
    if name_container is None:
        pass
    else:
        print("Name: " + name_container.string)
    if id_container is None:
        pass
    else:
        print("ID: " + id_container.string)
    if gender_container is None:
        pass
    else:
        print("Sex: " + gender_container.string)
    if breed_container is None:
        pass
    else:
        print("Breed: " + breed_container.string)
    if age_container is None:
        pass
    elif age_container.string is None:
        pass
    else:
        print("Age: " + age_container.string)
    print("Image: " + picture)
    print("\n")

print("Puppy Count: " + str(len(containers)))
