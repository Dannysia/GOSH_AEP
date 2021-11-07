import xml.etree.ElementTree as ET

def getTransformers(path):
    file = open(path)
    tree = ET.parse(file)
    root = tree.getroot()
    output = []
    for child in root[0][3]:
        try:
            data = {
                "PlacemarkID" : child.attrib['id'],
                "Type" : "T",
                "Latitude" : child[4][2].text.split(',')[0],
                "Longitude" : child[4][2].text.split(',')[1],
                "Altitude" : child[4][2].text.split(',')[2],
                "AltitudeMode" : child[4][1].text,
                "Extrude" : child[4][0].text
            }
            output.append(data)
        except Exception as ex:
            print(ex)
    return output

def getPoles(path):
    file = open(path)
    tree = ET.parse(file)
    root = tree.getroot()
    output = []
    for child in root[0][3]:
        try:
            data = {
                "PlacemarkID" : child.attrib['id'],
                "Type" : "P",
                "Latitude" : child[4][2].text.split(',')[0],
                "Longitude" : child[4][2].text.split(',')[1],
                "Altitude" : child[4][2].text.split(',')[2],
                "AltitudeMode" : child[4][1].text,
                "Extrude" : child[4][0].text
            }
            output.append(data)
        except Exception as ex:
            print(ex)
    return output

#transformers = getTransformers("D:\\Users\\Danny\\Downloads\\HOhio\\Transformers\\doc.kml")
#poles = getPoles("D:\\Users\\Danny\\Downloads\\HOhio\\Poles\\doc.kml")

def getExif(path):
    from exif import Image
    image = Image(open(path, 'rb'))
    latitude = image['gps_latitude'][0] + image['gps_latitude'][1]/60 + image['gps_latitude'][2]/3600
    if image['gps_latitude_ref'] == 'S':
        latitude = latitude * -1
    longitude = image['gps_longitude'][0] + image['gps_longitude'][1]/60 + image['gps_longitude'][2]/3600
    if image['gps_longitude_ref'] == 'W':
        longitude = longitude * -1
    altitude = image['gps_altitude']
    try:
        date = image['datetime']
        date = date[0:4] + '-' + date[5:7] + '-' + date[8:]
        if date[-2:] == '  ':
            date = date[:-2] + '00'
    except:
        date = '1970-01-01 00:00:00'
    data = {
        "Latitude" : latitude,
        "Longitude" : longitude,
        "Altitude" : altitude,
        "OriginalName" : path.split('\\')[-1],
        "DateTaken" : date
    }
    return data

def getExifs(folder):
    import glob
    output = []
    for picture in glob.glob(folder+'*.JPG'):
        try:
            output.append(getExif(picture))
        except:
            continue
    return output

exifs = getExifs("D:\\Users\\Danny\\Downloads\\HOhio\\")
print(len(exifs))

for data in exifs:
    print(data)