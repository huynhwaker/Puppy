from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals.aspx?species=Dog&gender=A&agegroup=UnderYear&location=&site=&onhold=A&orderby=name&colnum=3&css=http://ws.petango.com/WebServices/adoptablesearch/css/styles.css&authkey=io53xfw8b0k2ocet3yb83666507n2168taf513lkxrqe681kf8&recAmount=&detailsInPopup=No&featuredPet=Include&stageID=&wmode=opaque'

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

#grabs each puppy record
containers = page_soup.findAll("td",{"class":"list-item"})

container = containers[0]
#name_container = container.findAll("div", {"class":"list-animal-name"})

filename = "puppy.csv"
f = open(filename, "w")

headers = "id,name,gender,breed,age,location,image\n"

f.write(headers)

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
        name = "N/A"
    else:
        name = name_container.string
    if id_container is None:
        pid = "N/A"
    else:
        pid = id_container.string
    if location_container is None:
        location = "N/A"
    else:
        location = location_container.string
    if gender_container is None:
        sex = "N/A"
    else:
        sex = gender_container.string
    if breed_container is None:
        breed = "N/A"
    else:
        breed = str(breed_container.string)
    if age_container is None:
        age = "N/A"
    elif age_container.string is None:
        age = "N/A"
    else:
        age = age_container.string

    f.write(pid + "," + name + "," + sex + "," + breed.replace(","," | ") + "," + age + "," + location + "," + picture + "\n")

f.close()
