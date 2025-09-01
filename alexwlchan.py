# Use the alexwlchan/ao3 library
import ao3
# work = ao3.Work(52884502)

# work = api.work(id='52884502')

# url = "https://archiveofourown.org/works/52884502"
# testing
url = "https://archiveofourown.org/works/66427039"
# workid = AO3.utils.workid_from_url(url)
workid = "66427039"
print(f"Work ID: {workid}")
work = ao3.Work(workid)
# print(f"Chapters: {work.nchapters}")
# print(f"Work Chapters?: {work.chapters.work}")
title = work.title
print(f"Title: {title}")
author = work.author
print(f"Author: {author}")
summary = work.summary
# print(f"Summary: {summary}")
words = work.words
print(f"Words: {words:,}")
# print(f"chapter 1 title: {work.nchapters}")
chapters = work.chapters
print(f"Type of chapters: {type(chapters)}")
print(f"Chapters: {chapters}")
posted = chapters.strip().split('/')
print(f"chapters split list: {posted}")
print(f"{posted[0]}")
posted_num = int(posted[0])
print(f"Type of posted: {type(posted_num)}")
# print(f"Chapters posted: {chapters['posted']}")
data = work.json()
# print(f"Work: {data}")