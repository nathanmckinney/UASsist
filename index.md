# Welcome to uassist


[![image](https://img.shields.io/pypi/v/uassist.svg)](https://pypi.python.org/pypi/uassist)


**UASsist: Assistant for Unmanned Aircraft System photogrammetry for surveying and mapping applications. **


-   Free software: GNU General Public License v3
-   Documentation: <https://nathanmckinney.github.io/uassist>
    

## Features

-   Reads image metadata and displays information important for UAS surveys
-   Displays photo coordinates on a map embedded in a notebook
-   Input single image or folder containing multiple images
-   Folder inputs will calculate average, min, max altitude for project and range of timestamps
-   Change basemaps and upload geojson or shapefiles to display map
-   Converts image locations and attributes to files:
    -   CSV text
    -   GEOJSON
    -   KML
    -   GEOPACKAGE
    -   ESRI Shapefile
-   TODO:
    -   Create project metadata file
    -   Separate images into sub project folders using breaks in timestamp
    -   Create flight pattern lines
    -   Check EXIF altitude over DEM elevation
-   TODO eventually if possible:
    -   Incorporate extended and non-standard EXIF tags for certain manufacturers

## Attribute File Structure

| ATTRIBUTE     | TYPE      | DESCRIPT         |
| ------------- |:---------:| ----------------:|
| filenname     | string    | image file name  |
| latdd         | float     | Latitude in decimal degrees |
| longdd        | float     | Longitude in decimal degrees |
| altitude      | float     | Elevation from EXIF   |
| datetime      | datetime or string  | date and time from EXIF  |
| makemodel     | string    | make & model values of camera/UAS  |
| height_width  | string    | image size in pixels formatted as 'HEIGHT x WIDTH'  |
| xypair        | list or string |  X and Y values as list in single column |
| filepath      | string    | full path of file including filename |
| geometry      | geometry | Spatial type added for all functions where data is passed through GeoPandas |


![Demo](https://i.imgur.com/I6A2mY8.gif)

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [giswqs/pypackage](https://github.com/giswqs/pypackage) project template.
