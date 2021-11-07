def getConnection():
    import mysql.connector
    return mysql.connector.connect(user='danny', password='nnqSUt^oBoVSvC6', host='localhost', database='vision', auth_plugin='mysql_native_password')

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


connection = getConnection()
cursor = connection.cursor()

#query = "INSERT INTO KMLCoords(PlacemarkID, Type,  Latitude, Longitude, Altitude, AltitudeMode, Extrude) VALUES (%(PlacemarkID)s, %(Type)s, %(Latitude)s, %(Longitude)s, %(Altitude)s, %(AltitudeMode)s, %(Extrude)s)"
#for data in getPoles("poles.kml"):
#    try:
#        cursor.execute(query, data)
#    except Exception as ex:
#        print(ex)

#for data in getTransformers("transformers.kml"):
#    try:
#        cursor.execute(query, data)
#    except Exception as ex:
#        print(ex)

#query = "INSERT INTO PoleImages(OriginalName, DateTaken, Latitude, Longitude, Altitude) VALUES (%(OriginalName)s, %(DateTaken)s, %(Latitude)s, %(Longitude)s, %(Altitude)s);"
#exifs = getExifs("/home/danny/HOhio/")
#print(len(exifs))
#for data in exifs:
#    try:
#        cursor.execute(query,data)
#    except Exception as ex:
#        print(ex)

#connection.commit()

def getConnection2():
    import mysql.connector
    return mysql.connector.connect(user='danny', password='nnqSUt^oBoVSvC6', host='localhost', database='vision', auth_plugin='mysql_native_password')

def getConnection2():
    import mysql.connector
    return mysql.connector.connect(user='danny', password='nnqSUt^oBoVSvC6', host='localhost', database='vision', auth_plugin='mysql_native_password')

def getImagePairs():
    connection = getConnection2()
    cursor = connection.cursor()
    query = "SELECT ImageID, OriginalName FROM PoleImages;"
    cursor.execute(query)
    res = cursor.fetchall()
    output = []
    for pair in res:
        data = {
            "original" : pair[1],
            "new" : str(pair[0]) + ".JPG"
        }
        output.append(data)
    return output

def copyAndRenameImages(path):
    import shutil
    import os
    pairs = getImagePairs()
    for pair in pairs:
        originalPath = pair["original"]
        newPath = path + "new/" + pair["new"]
        shutil.copyfile(originalPath, newPath)

#copyAndRenameImages("HOhio/")

def findNearestPole(imageID):
    connection = getConnection()
    cursor = connection.cursor()
    query = "SELECT Longitude, Latitude FROM PoleImages WHERE ImageID = %(imageID)s;"
    cursor.execute(query, { "imageID" : imageID })
    res = cursor.fetchall()[0]
    targetLat = res[1]
    targetLong = res[0]
    query = "SELECT PlacemarkID, (SQRT(POWER(Latitude-%(targetLat)s,2))+POWER(Longitude-%(targetLong)s,2)) AS Distance FROM KMLCoords WHERE Type = 'P' ORDER BY Distance ASC LIMIT 1"
    cursor.execute(query, {"targetLat" : targetLat, "targetLong" : targetLong})
    return cursor.fetchall()[0][0]

def findNearestPole():
    iquery = "INSERT INTO KMLCoordsPolesToImage(PlacemarkID, ImageID) VALUES (%(PlacemarkID)s, %(ImageID)s);"
    connection = getConnection()
    cursor = connection.cursor()
    query = "SELECT ImageID FROM PoleImages;"
    cursor.execute(query)
    images = cursor.fetchall()
    for image in images:
        PlacemarkID = findNearestPole(image)
        try:
            cursor.execute(iquery, {"PlacemarkID" : PlacemarkID, "ImageID" : image[0]})
        except Exception as ex:
            print(ex)
    connection.commit()

findNearestPole()