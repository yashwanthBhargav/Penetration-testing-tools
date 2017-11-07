import mechanize
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

#For [SSL: CERTIFICATE_VERIFY_FAILED] errors
import ssl

class XSScanner2:
	def __init__(self):
		self.reset()
	def ask():
		x = raw_input("Do u want to inject another payload??[y/n]: ") 
		if x=="Y" or x=="y":
		   driver.close()
		   return True       
		elif x=="N"or x=="n":
			 driver.close()
			 raise SystemExit
		else:
			print "Invalid option"
			ask()
	
	def result(self,site):
		d="nope"
		response=br.open(site)
		soup=BeautifulSoup(response,'html.parser')
		nlfs=[]
		nlff=[]
		for a in soup.find_all("form"):
			if (a.get("name")!=None):
				nlff.append(str(a.get("name")))
		for b in soup.find_all("input"):
			#print b
			if (b.get("name")!=None) and (b.get("type")=="text" or b.get("type")==None)and b.get("name")not in nlff:
				nlfs.append(str(b.get("name")))
		for c in soup.find_all("textarea"):
			if (c.get("name")!=None) and (c.get("type")!="hidden")and c.get("name")not in nlff and c.get("name")not in nlfs:
				nlfs.append(str(c.get("name")))

		#print nlff 
		#print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		#print nlfs    

		for na in nlfs:
			print na
			f=open("list1.txt")
			while True:
				r=f.readline()
				print "Injecting the below payload: "
				print r
				driver = webdriver.Firefox()
				driver.get(site)
				time.sleep(10)
				try: 
				 element = driver.find_element_by_name(na)
				 element.send_keys(r)
				 element.submit()
				 
				except():
					d= "Parameter not tracable"
				driver.implicitly_wait(20)
				x = raw_input("Do u want to inject another payload??[y/n]: ") 
				if ask():
					continue
		return d

           


          
             
         

