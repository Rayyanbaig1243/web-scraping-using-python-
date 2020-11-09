  #importing required Libraries
	
	from selenium import webdriver
	from bs4 import BeautifulSoup
	import pandas as pd
	from webdriver_manager.chrome import ChromeDriverManager
	import numpy as np
	driver = webdriver.Chrome(ChromeDriverManager().install())
	
	#creating 3 empty List to store data
	Name=[];review=[];address=[];cattagory = []
	
	#Gettng The input from the user
	no_of_pages_toscrowl = int(input('Enter the no of pages need to be scrowled :  '))

	#looping over the number of pages entered by the user to scrape the data
	for i in range(10,(no_of_pages_toscrowl+1)*10,10):
	
		try:
			#getting the required page data
			driver.get("https://www.yelp.com/search?find_desc=Small%20Businesses&find_loc=Newark%2C%20CA%2094560&start="+ str(i))
			content = driver.page_source
			
			#creating an obeject of BeautifulSoup
			soup = BeautifulSoup(content,features="lxml")

			#looping over the document fields to get the Specific data bassed on type and Class
			for a in soup.findAll('li', attrs={'class':'le
				catt=a.find(attrs={'class':'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--default__373c0__7tls6'})
				
				#checking if any null value is present in the specific field then append Nan value else append scrapped value
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
			#if some error occures then it will give some basic Recomendation to avoid That error
			print('some error occured.!')
			print('1) try to chenge the number of pages to scrowl "preffered number is 4"')
			print('2) check your internet connection')
			print('3) run the script agin')
			print('4) close all current chrome tabs')
			pass
							   
	creating an index list contaions the numbers from 1 to len of the data
	index=[];for i in range(1,len(Name)+1):index.append(i)
	
	#at last creating the DataFrame from the list
	df = pd.DataFrame({'index':index, 'Hotel Name':Name ,'Catogory':cattagory, 'number of reviews' :review,'address':address}) 
	df.to_csv('new_business.csv', index=False, encoding='utf-8')
