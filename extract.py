import os, fnmatch, sys
path = os.path.dirname(sys.argv[0])
urlpath = os.path.join(path,"url")
urls = os.path.join(urlpath,"urls.txt"); open(urls,"w+")
scriptfile = os.path.join(urlpath,"dl.ps1"); open(scriptfile,"w+")

filelist = os.listdir(urlpath)

matchstring = "video-url*.txt"
for file in filelist:
	urlfile = os.path.join(urlpath,file)
	if fnmatch.fnmatch(file, matchstring):
		for link in open(urlfile, "r").readlines():
			open(urls, "a+").write(link)
storeurl = open(urls, "r").read().splitlines()

i=0
for x in storeurl:
	i = i+1
	if i < 10:
		open(scriptfile, "a+").write("ffmpeg -i " + x + " -c copy -bsf:a aac_adtstoasc 'S03E0" + str(i) + ".mp4'\n")
	else:
		open(scriptfile, "a+").write("ffmpeg -i " + x + " -c copy -bsf:a aac_adtstoasc 'S03E" + str(i) + ".mp4'\n")