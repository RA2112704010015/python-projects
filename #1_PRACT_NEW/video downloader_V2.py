import pytube
video_list = []
name_list = []
itag_list = []
while True:
    url = input("enter URL'S (TERMINATE BY STOP):--")
    if url == "STOP" or url == "stop" or url == "Stop":
        break
    nam = input("enter name of above url:--")
    vide = pytube.YouTube(url)
    for ste in vide.streams:
        if "video" in str(ste) and "mp4" in str(ste):
            print(ste)
    it = int(input("enter itag:--"))
    video_list.append(url)
    name_list.append(nam)
    itag_list.append(it)
for x, video in enumerate(video_list):
    vid = pytube.YouTube(video)
    name = name_list[x]
    ita = itag_list[x]
    stream = vid.streams.get_by_itag(ita)
    print(f"Downloading video {x+1} {name} ....")
    stream.download(filename=name)
    print("Done")
