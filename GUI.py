from tkinter import *
from tkinter.messagebox import *
import whois
import mechanize
import webbrowser
from bs4 import BeautifulSoup 
import urllib2
import urllib
import string
from selenium import webdriver
from urllib2 import urlopen
from urllib import urlencode
from urlparse import uses_query
import requests
import httplib
import urlparse
import os
import sys
import ssl
import time
from selenium import webdriver
import requests
import XSScanner2

ssl._create_default_https_context = ssl._create_unverified_context
br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#br.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',)]
'''br.addheaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}'''
br.set_handle_refresh(False)

def set_input(value):
    Te.delete(1.0, END)
    Te.insert(END, value)

def rClicker(e):
    ''' right click context menu for all Tk Entry and Text widgets
    '''

    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        def rClick_Cut(e):
            e.widget.event_generate('<Control-x>')

        def rClick_Paste(e):
            e.widget.event_generate('<Control-v>')

        e.widget.focus()

        nclst=[
               (' Cut', lambda e=e: rClick_Cut(e)),
               (' Copy', lambda e=e: rClick_Copy(e)),
               (' Paste', lambda e=e: rClick_Paste(e)),
               ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

    except TclError:
        print ' - rClick menu, something wrong'
        pass

    return "break"


def rClickbinder(r):

    try:
        for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except TclError:
        print ' - rClickbinder, something wrong'
        pass

def cms_f():
	#blank.delete(0,'end')
	set_input("Checking....")
	 
	#v.set("")
	m = True
	site =str(url.get())
	p = urllib2.urlopen(site)
	p= p.read()
	s = BeautifulSoup(p,'html.parser')
	#print s
	for l in s.find_all("meta"):
		if l.get("name")=="generator":
			d= l.get("content")
			m =False
			#blank.insert(0, d)
			#v.set(str(d))
			set_input(str(d))
	if m:
		d= "Cannot find the CMS :("
		#blank.insert(0, d)
		#v.set(str(d))
		set_input(str(d))
def domain():
	#blank.delete(0,'end')
	set_input("Checking....")
	 
	#v.set("Checking....")
	site = str(url.get())
	d = whois.whois(site)
	#blank.insert(0, d)
	#v.set(str(d))
	set_input(str(d))
def XSScanner1():
	#v.set("")
	#blank.delete(0,'end')
	#def paramfind(ur2):
	#	br.open(ur2)
	#	for l in br.links():
	#	    print l.url
	set_input("Checking....")
	 
	site = str(url.get())
	parsed_url = urlparse.urlparse(site)
	#print parsed_url
	parsed_url_list = list(parsed_url)
	#print parsed_url_list
	parameters = dict(urlparse.parse_qs(parsed_url_list[4]))
	d=[]
	if parameters =={}:
		d.append( "No parameters in the url........." )
		#paramfind(ur1) 
		k="Url has no parameters,use XSScanner2"	
		#v.set(str(d))
		set_input(str(d))
	else:
		list2 = parsed_url_list[4];
		#print parameters
		f=open("list1.txt")
		count=0
		for i in parameters:
			r="qqqqqqqqq"
			print "Checking the "+ i +" parameter:"
			while len(r)>5:
				r=f.readline()
				#print '+'
				parameters[i] = r        #changing a single parameter
				parsed_url_list[4] = urlencode(parameters)
				#d.append(urlparse.urlunparse(parsed_url_list))
				some_url=urlparse.urlunparse(parsed_url_list)
				#print some_url
				page=urllib.urlopen(some_url)
				if str(r) in page.read() and len(r)>4:
					count+=1
					d.append(str(r))
        			print str(r)+":"+str(count)
			if count>0:
				k="URL is Vulnerable to XSS \n Payloads Succesfull:"
				#print d
				for i in d:
					k+="\n"+str(i)				          
				#v.set(k)	
				set_input(k)
			else:
				

def Scanner2():
	d="nope"
	#set_input("Checking....")
	#v.set("Checking....")
	site = str(url.get())
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
	
	if nlfs==[] and nlff==[]:
		
		set_input("No text fields to inject XSS Payloads")
		#v.set("No text fields to inject XSS Payloads")
	else:
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
				#x = tkinter.tkSimpleDialog.askstring
				if x=="n" or x=="N":
					break
				set_input("")
		for na in nlff:
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
				#x = tkinter.tkSimpleDialog.askstring
				if x=="n" or x=="N":
					set_input("")
					break
				set_input("")
	#set_input("comming soon.....").

def spider():
	site = str(url.get())
	X=str(url.get())
	ur1="http://google.co.in/search?q=inurl:"+X+".com"
	response=br.open(ur1)
	Te.delete(1.0, END)
	for link in br.links():
		if X in link.url:
			Te.insert(END,"\n"+str(link.base_url))
	


main = Tk()
main.title("Tools")


Label(main, text = "Enter Url:",font=('MS', 8,'bold')).grid(row=1, column=1,sticky='E')
Label(main, text = "Result: ",font=('MS', 8,'bold')).grid(row=2, column=1,sticky='En')

Te = Text(main, height=10, width=30)
Te.insert(END, "")
scroll = Scrollbar(main, command=Te.yview)
Te.configure(yscrollcommand=scroll.set)

#v = StringVar()
#Label(main, textvariable=v,wraplength=350, justify=LEFT).grid(row=2, column=2,columnspan=10,sticky='W')


url = Entry(main,width=80)
Te.grid(row=2, column=2,columnspan=10,sticky='Ensw')
scroll.grid(row=2,column=12,sticky='ens')
#blank = Entry(main,width=100)


url.grid(row=1, column=2,columnspan=8,sticky='W')
#blank.grid(row=2, column=2,columnspan=10,sticky='nesW')

main.rowconfigure(1, minsize=50)
main.rowconfigure(2, minsize=100)
main.rowconfigure(4, minsize=50)
main.rowconfigure(6, minsize=50)

Button(main, text='Quit', bg="light blue",font=('Times', 16,'bold'), command=main.destroy).grid(row=6,column=3,columnspan=3)
Button(main, text='domain details', bg="light blue",font=('MS', 8,'bold'), command=domain).grid(row=4, column=2,sticky='W')
Button(main, text='CMS for the URL', bg="light blue",font=('MS', 8,'bold'),  command=cms_f).grid(row=4, column=3,sticky='W')
Button(main, text='XSS Scanner 1', bg="light blue",font=('MS', 8,'bold'),  command=XSScanner1).grid(row=4, column=4,sticky='W')
Button(main, text='XSS Scanner 2', bg="light blue", font=('MS', 8,'bold'), command=Scanner2).grid(row=4, column=5,sticky='W')
quote="Spider URL\n(enter required domain)"
Button(main, text=quote, bg="light blue", font=('MS', 6,'bold'), command=spider).grid(row=4, column=6,sticky='W')

rClickbinder(main)
mainloop()
