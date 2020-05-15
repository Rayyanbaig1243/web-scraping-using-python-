# web-scraping-using-python-
In this reposirory i have shown how to scrwl the Yelp Business dtaa using python.

Yelp_details_scarwling.py script will scrap the data of name cattgory address and nomber of reviews from the Yelp and stores in csv file.

This script uses Google chrome as default browser.

	from selenium import webdriver
	from bs4 import BeautifulSoup
	import pandas as pd
	from webdriver_manager.chrome import ChromeDriverManager
	import numpy as np
	driver = webdriver.Chrome(ChromeDriverManager().install())

	Name=[];review=[];address=[];cattagory = []
	no_of_pages_toscrowl = int(input('Enter the no of pages need to be scrowled :  '))

	for i in range(10,(no_of_pages_toscrowl+1)*10,10):
		try:
			driver.get("https://www.yelp.com/search?find_desc=Small%20Businesses&find_loc=Newark%2C%20CA%2094560&start="+ str(i))
			content = driver.page_source
			soup = BeautifulSoup(content,features="lxml")

			for a in soup.findAll('li', attrs={'class':'lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU'}):
				name=a.find('a',href=True,attrs={'class':"lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE"})

				pno=a.find(attrs={'class':'lemon--span__373c0__3997G text__373c0__2Kxyz reviewCount__373c0__2r4xT text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-'})

				add=a.find(attrs={'class':'lemon--span__373c0__3997G raw__373c0__3rcx7'})
	from selenium import webdriver
	from bs4 import BeautifulSoup
	import pandas as pd
	from webdriver_manager.chrome import ChromeDriverManager
	import numpy as np
	driver = webdriver.Chrome(ChromeDriverManager().install())

	Name=[];review=[];address=[];cattagory = []
	no_of_pages_toscrowl = int(input('Enter the no of pages need to be scrowled :  '))

	for i in range(10,(no_of_pages_toscrowl+1)*10,10):
		try:
			driver.get("https://www.yelp.com/search?find_desc=Small%20Businesses&find_loc=Newark%2C%20CA%2094560&start="+ str(i))
			content = driver.page_source
			soup = BeautifulSoup(content,features="lxml")

			for a in soup.findAll('li', attrs={'class':'le
				catt=a.find(attrs={'class':'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--default__373c0__7tls6'})


				if name !=None:
					#print('hotel name is : ',name.text)
					Name.append(name.text)
				else:Name.append(np.nan)

				if name !=None:
					review.append(pno.text)
				else:review.append(np.nan)
				if add !=None:
					address.append(add.text)
				else:address.append(np.nan)
				if catt !=None:	
					cattagory.append(catt.text)
				else:cattagory.append(np.nan)

		except :
			print('some error occured.!')
			print('1) try to chenge the number of pages to scrowl "preffered number is 4"')
			print('2) check your internet connection')
			print('3) run the script agin')
			print('4) close all current chrome tabs')
			pass
	index=[];for i in range(1,len(Name)+1):index.append(i)
	df = pd.DataFrame({'index':index, 'Hotel Name':Name ,'Catogory':cattagory, 'number of reviews' :review,'address':address}) 
	df.to_csv('new_hotels.csv', index=False, encoding='utf-8')

METHODOLOGY:
this script first open that websites in chrome using the url pattern specified in for loop.
then getts the equired data and stores in the list.
at the end all data is stored in a CSV formate using Pandas Library.

It was bit confusing while understanding the path. but it was simple.
frist, i gone throw all next websites using next page link and got the pattern of path and looped over all path till the specified number.

I have used exception block to tell the common errors. that, we will get while running the script and to get some suggestion to aviod errors.

HOW TO RUN:
step1) install all the reqiured libraries selenium, bs4, Pandas and Numpy.
step2) run the  python web_scrawling_on_Yelp.py on your terminal.
strp 3) in terminal an messge was printed "Enter the no of pages need to be scrowled :". hear type the number pages to be scrwled maximum 250 approx.

After running the script secsusfully it will store a Csv file in your folders.

Note:
Sometines this will make an arry length mis math problem beacuse of dynamic new pages. we need to re run the script till it wont give any error.
aslo it prints some suggestion when problem occures with loading the page.
