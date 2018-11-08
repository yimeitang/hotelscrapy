## hotelscrapy
This program automates images downloading, saving and labeling with correct ratings.

***
## [Usage Overview](#usage-overview)
First, you need a .txt file that has the photo page html contents.

Then, you need the url address of the hotel page.

Ok, now you could run hotelscrapy that automates image downloading, saving and rating labeling process!
```python
>>>photoUrl = 'https://www.tripadvisor.com/Hotel_Review-g35805-d87595-Reviews-The_Congress_Plaza_Hotel_and_Convention_Center->>>Chicago_Illinois.html#photos;aggregationId=101&albumid=101&filter=7&ff='
>>>hs = HotelScrapy('divhtml.txt', photoUrl)
>>>hs.run()
We have successfully saved 1735 images and labeled it with ratings in 150.34 minutes
```
