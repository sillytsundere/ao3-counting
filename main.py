import eel
# from datetime import datetime as dt
# import AO3
# api = AO3()

# Use the wendytg/ao3_api library
# import ao3_api
# session = ao3_api.Session()
# work = ao3_api.Work(work_id="52884502", session=session)

# Use the alexwlchan/ao3 library
import AO3
# work = ao3.Work(52884502)

# work = api.work(id='52884502')


@eel.expose
def hello():
    print("Hello World!")

url = "https://archiveofourown.org/works/52884502"
# workid = AO3.utils.workid_from_url(url)
workid = "52884502"
print(f"Work ID: {workid}")
work = AO3.Work(workid)
# print(f"Chapters: {work.nchapters}")
# print(f"Work Chapters?: {work.chapters.work}")
title = work.title
print(f"Title: {title}")
author = work.author
print(f"Author: {author}")
summary = work.summary
print(f"Summary: {summary}")
words = work.words
print(f"Words: {words}")
# print(f"chapter 1 title: {work.nchapters}")
data = work.json()
# print(f"Work: {data}")


eel.init("www")
eel.start("index.html")

# while True:
#     timestamp = dt.now()
#     eel.addText("The time is now {}".format(timestamp.strftime("%I:%M:%S %p")))

#     eel.sleep(1.0)

