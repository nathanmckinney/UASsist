"""Conversions Module
    """

def img_to_csv(imgdict):
    import csv
    import pandas

    df = dict_to_df(imgdict)

    df.to_csv('images.csv', index=False)

    """
        with open('photos.csv', 'w', newline='') as file:
            fieldnames = ['filename', 'latdd', 'longdd']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
    """

def img_to_geojson(imgdict):
    pass

def img_to_shp(imgdict):
    pass

def imgdir_conv(folderpath):

    import os, exifread, datetime, uassist
    from exifread.utils import get_gps_coords

    masterdict = {}

    for filename in os.listdir(folderpath):
        if filename.endswith(".jpg") or filename.endswith(".JPG"): 
            filepath = folderpath + "/" + filename
            f = open(filepath, 'rb')
            tags = exifread.process_file(f, details=False)

            # GPS Altitude Values
            gpsaltval = [c.decimal() for c in tags["GPS GPSAltitude"].values]
            gpsalt = round(gpsaltval[0], 2)

            # GPS Coords
            gps = get_gps_coords(tags)
            latdd = round(gps[0], 7)
            longdd = round(gps[1], 7)

            xy = [latdd, longdd]
            #xyz = [latdd, longdd, gpsalt]

            # timestamps
            datetimestr = str(tags.get("Image DateTime"))
            datetimeobj = datetime.datetime.strptime(datetimestr, '%Y:%m:%d %H:%M:%S')
            
            # model
            make = str(tags["Image Make"])
            model = str(tags["Image Model"])
            makemodel = (make + " " + model)
            
            #image width and height
            imgh = str(tags.get("EXIF ExifImageLength"))
            imgw = str(tags.get("EXIF ExifImageWidth"))
            imghw = (imgw + " x " + imgh)

            masterdict[filename] = [filename, latdd, longdd, gpsalt, datetimeobj, makemodel, imghw, xy, filepath]
            
            continue
        else:
            continue

    return masterdict

def dict_to_df(imgdict):
    import pandas

    cols = ['filename','latdd','longdd','altitude','datetime','makemodel','height_width','xy_pair','filepath']

    df = pandas.DataFrame.from_dict(imgdict, orient='index', columns=cols)

    return df

