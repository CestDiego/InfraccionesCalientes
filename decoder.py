import urllib, urllib2, json
import json

def decode_address_to_coordinates(address):
        params = {
            'address' : address,
            'key': 'AIzaSyBYV18V24_F6GRAFcWoQ0Y95f9tsB8v7_M',
            'sensor' : 'true',
        }
        url = 'https://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        result = json.load(response)
        try:
                return result['results'][0]['geometry']['location']
        except:
                return None

with open('INFRA-3.json', 'r') as input_file:
    le_json = json.load(input_file)

for item in le_json:
    if item.has_key("lat"):
            continue
    adress = item["LUGAR1"] + " " + item["NRO"] + " Miraflores, Lima"
    coord = decode_address_to_coordinates(u''.join(adress).encode('utf-8'.strip()))
    try:
        coord["lat"]
    except TypeError:
            print "Se acabaron tus creditos"
            break
    with open('INFRA-5t.json', 'w') as output_file:
        item["lat"] = coord["lat"]
        item["lng"] = coord["lng"]
        json.dump(le_json, output_file, indent=2)
        print coord, adress

