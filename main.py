import eel
# from datetime import datetime as dt
import AO3

@eel.expose
def hello():
    print("Hello World!")

url = "https://archiveofourown.org/works/52884502/chapters/139528555"
workid = AO3.utils.workid_from_url(url)
print(f"Work ID: {workid}")
work = AO3.Work(workid)
print(f"Chapters: {work.nchapters}")
print(f"Work Chapters?: {work.chapters.work}")
# title = work[7:-1]
# print(f"Title: {title}")
# print(f"chapter 1 title: {work.chapters[0].text}")
print(len(work.chapters[0].text.split(" ")))


eel.init("www")
eel.start("index.html")

# while True:
#     timestamp = dt.now()
#     eel.addText("The time is now {}".format(timestamp.strftime("%I:%M:%S %p")))

#     eel.sleep(1.0)

