import os

import requests
import urllib.request

from bs4 import BeautifulSoup

import time
import timeit

from selenium import webdriver

import re

class HotelScrapy(object):
    """This problem automates images downloading, saving and
    labeling with correct ratings.

    Attributes:
        divHtml: The name of the txt file that contains
                 <div class="photoGridBox"></div> html contents.
        photoUrl: The url address of hotel photos page.
        imageDict: A dictionary of key is the imageId and the value is imageURL.
        cehckedList: A list of IDs of downloaded images to avoid duplication.
    """

    def __init__(self, divHtml, photoUrl):
        """Inititate HotelScrapy with divhtml and photourl."""
        self.divHtml = divHtml
        self.photoUrl = photoUrl
        self.imageDict = {}
        self.checkedList = []

    def generateDict(self):
        """Open the html contents, scrap the imageID and imageURL,
           populate the imageDict dictionary by assigning key of imageID and
           value of imageURL. The imageID is the name of the image,
           the imageURL is the url address of that image.
        """
        with open(self.divHtml,'r') as iFile:
            line=iFile.read()
            lines=line.split()
            for item in lines:
                if item.startswith('data-mediaid='):
                    imageID=re.sub("[^0-9]", "", item)
                elif item.startswith('src="https:'):
                    imageUrl=item[5:item.find('.jpg')+4]
                    self.imageDict[imageID]=imageUrl

    def render_page(self,imageUrl):
        """Return the html contents from the image url"""
        driver = webdriver.Chrome()
        driver.get(imageUrl)
        time.sleep(1)
        contents = driver.page_source
        return contents

    def getRating(self,imageID):
        """Return the rating for the image without handlabeling"""
        imageUrl=self.photoUrl+imageID
        contents=self.render_page(imageUrl)
        soup = BeautifulSoup(contents, "html.parser")
        ratings=['1','2','3','4','5']
        for r in ratings:
            rating="ui_bubble_rating member bubble_"+r
            if soup.find('div', class_=rating):
                return r

    def saveImage(self):
        """Download the image and save it to appropriate rating folder """
        for imageID,image in self.imageDict.items():
            if int(imageID) in self.checkedList:
                continue
            rating=self.getRating(imageID)
            self.checkedList.append(imageID)
            if not rating:
                continue
            fullfilename = os.path.join('rating'+rating, imageID)
            urllib.request.urlretrieve(image, fullfilename+'.jpg')

    def run(self):
        """Automate the image downloading, saving and labeling process"""
        start = timeit.timeit()
        self.generateDict()
        self.saveImage()
        end = timeit.timeit()
        print("We have successfully saved {} images and labeled it with ratings in {:.2f} minuets".format(len(self.checkedList),(end - start)/60))
