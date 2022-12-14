# -*- coding: utf-8 -*-
"""exporting_resutls.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HQmNmu2rWREpypIPS1Il9xmCf7SVU30W
"""

#first we have to get the token which has sent to our email

#loading data from GEE
dataset = ee.Image("LANDSAT/LC08/C01/T1_TOA/LC08_170052_20170108")\
  .select('B3', 'B4')


#filtering AOI boundary as Sri Lanka
country = ee.Geometry.Rectangle(5.55, 9.51, 79.41, 81.53)

#exporting data to the drive
exprt = ee.batch.Export.image.toDrive(**{
    'image' = dataset,
    'description' = 'imagetoDriveExample'
    'folder' = 'exported_images'
    'scale' = 30
    'region' = aoi.getInfo()['coordinates']
})
exprt.start()
