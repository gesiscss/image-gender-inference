# image-gender-inference
This repository consists of codes related to the paper " Inferring Gender from Names on the Web: A Comparative Evaluation of Gender Detection Methods" by Karimi et al., WWW Conf. 2016 http://dl.acm.org/citation.cfm?doid=2872518.2889385

Codes are written by
Fariba Karimi, Florian Lemmerich and Stefan Vujovic

In order to perform gender inference according to the aproach described in the paper mentioned above the following files can be used:
1. [genderize_query.py](https://github.com/frbkrm/image-gender-inference/blob/master/genderize_query.py)
2. [getGoogleImagesv0.31.jar](https://github.com/frbkrm/image-gender-inference/blob/master/getGoogleImagesv0.31.jar)
3. [get_google_images.py](https://github.com/frbkrm/image-gender-inference/blob/master/get_google_images.py)
4. [faceplus_query.py](https://github.com/frbkrm/image-gender-inference/blob/master/faceplus_query.py)
5. [tasks.py](https://github.com/frbkrm/image-gender-inference/blob/master/tasks.py)

## genderize_query

This is the first step in our "pipeline", where the [genderize API](http://genderize.io/) is used to infer gender, based on the first name of a person. 

### Dependencies

* [Pandas](https://pypi.python.org/pypi/pandas/)
* [Genderize Client](https://pypi.python.org/pypi/Genderize/0.1.5)
* Python 3.x
* Genderize API key

Before running the script a file (csv or json) with first names is needed. An output file with gender, confidence for assigning gender, and frequency of the names in the database will be generated.

In order to run the scipt two command line arguments need to be specified, path to the input file with names, and path where the output file should be saved. 

### Input file

name |
--- | 
Peter |
Fariba |
Jovan |

### Output file

name |count |gender |confidence|
--- | --- |--- |--- |
Peter |3658 |male |.99 |
Fariba |465 |female |.96 |
Jovan |60 |male |.98 |
 
```{r, engine='bash', count_lines}
python genderize_query.py [inputfile.csv] [outputfile.csv]
```

For the next step we need to retrieve images for specified names from Google Image results by using getGoogleImages and then use [Face++ API](https://www.faceplusplus.com/) to infere gender out of these images.

# Getting images from Google

Initialy this was done with runing the getGoogleImages jar file, but later on the Python script below was developed as the jar doesn't handle utf-8 values well. So now, for the step of collecting image URL's there is a choice between the two programs below.

## getGoogleImages Java

Before runing this file, a file containing first and last names should be prepared. The format of one name is:
FIRST_NAME+LAST_NAME, for example: fariba+karimi. As a result of runing the script, a file will be generated and it will contain 5 URLs of images retrieved for specified name, for example: fariba+karimi,[url1,url2,url3,url4,url5] 

### Dependencies

* Java

### Input file

Peter+Smith |
--- | 
Fariba+Karimi |
Jovan+Jovanovic |

### Output file

Peter+Smith | http://.. |http://.. |http://.. |http://.. |http://.. |
--- |--- |--- |--- |--- |--- | 
Fariba+Karimi |http://.. |http://.. |http://.. |http://.. |http://.. |
Jovan+Jovanovic |http://.. |http://.. |http://.. |http://.. |http://.. |

The script can be ran this way: 
```{r, engine='bash', count_lines}
java -jar getGoogleImagesv0.31.jar [inputfile.txt]  [output.csv]
```
## get_google_images.py

Before runing this file, a file containing first and last names should be prepared. The format of one name is:
FIRST_NAME+LAST_NAME, for example: fariba+karimi. As a result of runing the script, a file will be generated and it will contain 5 URLs of images retrieved for specified name, for example: fariba+karimi,[url1,url2,url3,url4,url5] 

### Dependencies

* [Pandas](https://pypi.python.org/pypi/pandas/)
* Python 3.x
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](http://docs.python-requests.org/en/master/)

### Input file

Peter+Smith |
--- | 
Fariba+Karimi |
Jovan+Jovanovic |

### Output file

Peter+Smith | http://.. |http://.. |http://.. |http://.. |http://.. |
--- |--- |--- |--- |--- |--- | 
Fariba+Karimi |http://.. |http://.. |http://.. |http://.. |http://.. |
Jovan+Jovanovic |http://.. |http://.. |http://.. |http://.. |http://.. |

The script can be ran this way: 
```{r, engine='bash', count_lines}
python get_google_images.py [inputfile.csv]  [output.csv]
```

## faceplus_query

Using the file generated by getGoogleImages as input, we can retrieve gender for specified images using Face++. 

### Dependencies

* Python 2
* urllib2
* Face++ API key

In order to run the scipt two command line arguments need to be specified, path to the input file with names and urls, and path where the output file (json) should be saved. 

### Input file

Peter+Smith | http://.. |http://.. |http://.. |http://.. |http://.. |
--- |--- |--- |--- |--- |--- | 
Fariba+Karimi |http://.. |http://.. |http://.. |http://.. |http://.. |
Jovan+Jovanovic |http://.. |http://.. |http://.. |http://.. |http://.. |


### Output file

This file contains results for each image passed to the API. The results contain information about url, image size, face attributes like: gender , age, pose, race, smiling, mouth_left, mouth_righ, nose, eye_right.

```{r, engine='bash', count_lines}
python faceplus_query.py [inputfile.csv] [outputfile.json]
```

## faceplus_processing

After generating the json file with face++, it needs to be processed, and this can be done using the face_plus_processing.py whichh also follows the approach specified in the refferenced paper.

### Input file

Json file specified above.

### Output file

name | gender |
--- |--- | 
Fariba+Karimi | female |
Jovan+Jovanovic | male | 

```{r, engine='bash', count_lines}
python faceplus_processing.py [inputfile.json] [outputfile.csv]
```

## tasks.py
 
This script is developed to be used as a module as it contains tasks which are recurring when preparing data for the pipeline.  
