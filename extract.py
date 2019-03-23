import os, fnmatch, sys
path = os.path.dirname(sys.argv[0])
urlpath = os.path.join(path,"urls")
urls = os.path.join(path,"urls.txt"); open(urls,"w+")
scriptfile = os.path.join(path,"dl.ps1"); open(scriptfile,"w+")

filelist = os.listdir(urlpath)

matchstring = "video-url*.txt"
for file in filelist:
	urlfile = os.path.join(urlpath,file)
	if fnmatch.fnmatch(file, matchstring):
		for link in open(urlfile, "r").readlines():
			open(urls, "a+").write(link)
storeurl = open(urls, "r").read().splitlines()

season = "S03"
episode = 72

cmdlist = []
dquo = '"'
for url in storeurl:
	if episode < 10:
		episodename = season + "E00" + str(episode) + ".mp4"
	elif episode < 100:
		episodename = season + "E0" + str(episode) + ".mp4"
	elif episode < 1000:
		episodename = season + "E" + str(episode) + ".mp4"
	cmd = "youtube-dl " + dquo + url + dquo + " -f best" + " -o " + dquo + episodename + dquo
	cmdlist.append(cmd)
	open(scriptfile, "a+").write(cmd + "\n")
	episode+=1
for cmd in cmdlist:
	os.system(cmd)