from urllib import urlopen
webpage = urlopen("http://www.baidu.com")
text = webpage.read()
