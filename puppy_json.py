from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

my_url = 'https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals.aspx?species=Dog&gender=A&agegroup=UnderYear&location=&site=&onhold=A&orderby=name&colnum=3&css=http://ws.petango.com/WebServices/adoptablesearch/css/styles.css&authkey=io53xfw8b0k2ocet3yb83666507n2168taf513lkxrqe681kf8&recAmount=&detailsInPopup=No&featuredPet=Include&stageID=&wmode=opaque'
url2 = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+cards'

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
    gender_container = container.find("div", {"class":"list-animal-sexSN"})
    breed_container = container.find("div", {"class":"list-animal-breed"})
    age_container = container.find("div", {"class":"list-animal-age"})
    location_container = container.find("div", {"class":"hidden"})

data = {}

new_string = json.dumps(data, indent=2)

print(new_string)

writeToJSONFile('./','puppy',data)
