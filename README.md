# web-Scrape-using-python-
In this reposirory i have shown how to Scrape the Yelp Business data using python.
Yelp_details_scarwling.py script will scrap the data of name, cattgory, address and number of reviews from the Yelp website and stores in csv file.
This script uses Google chrome as default browser.

# METHODOLOGY:
This script first open that websites in chrome using the url pattern specified in the for loop.
then gets the required data and stores in the list.
at the end all the data of lists is stored in a CSV formate using Pandas Library.
It was bit confusing while understanding the path. but it was simple.
frist, i gone through all next websites using next page link and got the pattern of path and looped over all path till the specified number.

I have used exception block to tell the common errors. that, we will get while running the script and to get some suggestion to aviod errors.

### programming language: Python 3

## HOW TO RUN:
step 1): install all the required libraries. (they are, selenium, bs4, Pandas and Numpy.)

step 2): run the  `web_scrape.py` script on your terminal.

step 3): in terminal an messge was printed "Enter the no of pages need to be scrowled :". hear type the number pages to be Scraped.(maximum 250 approx, selected based on the websites last page number).

	After running the script successfuly it will store new_busines.csv file in your curent working directory. I have added the copy of new_business.csv file Scraped on the 4 webpages. 

## Note:
Sometines this will make an array length mis match problem beacuse of dynamic new pages. we need to re-run the script till we won,t get any error.
Aslo, it prints some suggestion when other problem occures with loading the webpage.

### Thank you for reading.
