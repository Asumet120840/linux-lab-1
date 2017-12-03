import click
import requests

from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup

@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def main(src, dst):
	"""Get photo Youtube"""
	try:	
		src_search=""	
		for fn in src:
        		src_search+='%s' % (fn)+" "
		src_search+='%s'%(dst)
		if(src_search[:24]=='https://www.youtube.com/' or src_search[:23]=='http://www.youtube.com/'):
			if(src_search[:5]=='http:'):src_search=src_search[:4]+'s'+src_search[4:]
			Yid=src_search.replace('https://www.youtube.com/watch?v=','')
		else:
			url="https://www.youtube.com/results?search_query="+src_search.replace(' ','+')
			html=requests.get(url)
			b=BeautifulSoup(html.content,'html.parser')
			Yid=str(b.find_all('div',{'class':'yt-lockup-dismissable'})[0].div.a['href']).replace('/watch?v=','')
		url='http://img.youtube.com/vi/{}/maxresdefault.jpg'.format(Yid)
		req=requests.get(url)
		img=Image.open(StringIO(req.content))
		img.show()
	except:
		print("--->Not found!! Vedio<---")
