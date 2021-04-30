# uassist


[![image](https://img.shields.io/pypi/v/uassist.svg)](https://pypi.python.org/pypi/uassist) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/uassist/badges/version.svg)](https://anaconda.org/conda-forge/uassist)


**UASsist: Assistant for Unmanned Aircraft System photogrammetry for surveying and mapping applications. **


-   Free software: GNU General Public License v3
-   Documentation: https://nathanmckinney.github.io/UASsist/
    

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

![Demo](https://i.imgur.com/5GLSavr.jpg)
## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [giswqs/pypackage](https://github.com/giswqs/pypackage) project template.
