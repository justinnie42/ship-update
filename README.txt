SHIPPING UPDATER:

HOW TO SETUP:
1. INSTALL LATEST VERSION OF PYTHON
2. TYPE py -m pip install selenium
3. MAKE SURE YOU HAVE FIREFOX INSTALLED
4. COPY THE deftshipUpdate FOLDER FROM THE FLASHDRIVE INTO THE DESKTOP
5. DOWNLOAD geckodriver.zip FROM GITHUB
6. EXTRACT geckodriver.zip TO THE deftshipUpdate FOLDER
7. DELETE geckodriver.txt (or whichever geckodriver is not geckodriver.exe)
8. CLICK ON deftshipUpdate.py TO START

USING THE DEFTSHIPUPDATE (UPDATES DEFTSHIP AND SHIPPO)
1. CLICK ON THE deftshipUpdate FILE
2. WAIT FOR EBAY AND SHIPPO TO LOAD
3. DO THE CAPTCHAS FOR EBAY AND SHIPPO - 30 SECOND WINDOW
4. THE PROGRAM WILL AUTOMATICALLY LOAD DEFTSHIP AND SHIPPO
5. EVERY PACKAGE AWAITING TO BE SHIPPED WILL BE LOADED ONTO DEFTSHIP,
INCLUDING THE QUANTITY OF EACH ITEM
IF THE PACKAGE IS NOT IN THE DATABASE, THE DETAILS FOR THE PACKAGE WILL
BE LEFT BLANK REGARDLESS OF QUANTITY

ADDING A NEW ITEM:
1. CLICK ON addProduct.txt
2. ENTER A NEW LINE
3. TYPE OUT THE DETAILS OF THE PRODUCT FOLLOWING THE EXAMPLE 
(NAME, SKU, LENGTH, WIDTH, HEIGHT, WEIGHT)
4. SEPARATE EACH SECTION OF THE PRODUCT WITH A , 
5. SAVE THE TEXT FILE

ADDING A MULTIPLE PART PACKAGE:
1. CLICK ON addABPackage.txt
2.ENTER A NEW LINE
3. TYPE OUT THE DETAILS OF THE PRODUCT FOLLOWING THE EXAMPLE
(NAME,SKU,LENGTHA,WIDTHA,HEIGHTA,WEIGHTA)
(NAME,SKU,LENGTHB,WIDTHB,HEIGHTB,WEIGHTB)
4. MAKE SURE THE TWO PACKAGES HAVE THE SAME NAME AND ARE NEXT TO EACH OTHER
5. SAVE THE TEXT FILE