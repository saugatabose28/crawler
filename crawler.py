import urllib
import urlparse
from BeautifulSoup  import BeautifulSoup
from cgi import escape
import string

def crawler(url):
    count=0
    urls=[url]
    visited=[url]
    repeat=[]
    f1=open("text.txt","w")
    while len(urls)>0 and len(urls)<10000:
        
	try:
		htmltext=urllib.urlopen(url).read()
	except:
		print urls[0]
		#print "qwe"
	#RETRIEVING HTML 	
	soup=BeautifulSoup(htmltext)
	urls.pop(0)
	#print urls,"@@@"
	for tag in soup.findAll('a',href=True):			      		
		
		#FIND ABSOLUTE LINK						      
		count+=1
		tag['href']=urlparse.urljoin(url,tag['href'])
		
#		ABSOLUTE LINK-PRINT      		      
		if  tag['href'] not in visited:	
		 	urls.append(tag['href'])			      
		 	visited.append(tag['href'])
			print 'added',count
		else: 
			repeat.append(count)
        
        #DATA
	for tag in soup.findAll('p'):				
		#print(tag.getText())
		f1.write(tag.getText().encode("ascii","ignore"))			
		
    f1.close()
    f=open("links.txt","w")
    s1="Input URL for crawler: "+"\n"
    s2=s1+"			"+url+"\n"
    f.write(s2)
    f.close()
    f=open("links.txt","a")
    k=1
    for i in visited:
        
	j=str(k)+": "+str(i)+"\n"
	f.write(j)
	k=k+1
    f.close()
    ret_urls=string.join(urls,'*')
    return ret_urls
    


def main(): 
    crawler('www.python.org')


if __name__ == '__main__' :
   main()
