from ao3api.works import Work

# work = ao3.Work(52884502)

# work = api.work(id='52884502')

# url = "https://archiveofourown.org/works/52884502"
# testing
url = "https://archiveofourown.org/works/66427039"
# workid = AO3.utils.workid_from_url(url)
workid = "56370340"
print(f"Work ID: {workid}")
work = Work(workid)

title = work.title
print(f"Title: {title}")
author = work.author
print(f"Author: {author}")
# summary = work.summary
# # print(f"Summary: {summary}")
words = work.words
print(f"Words: {words:,}")

chapters = work.chapters
print(f"Type of chapters: {type(chapters)}")
print(f"Chapters: {chapters}")
# posted = chapters.strip().split('/')
# print(f"chapters split list: {posted}")
# print(f"{posted[0]}")
# posted_num = int(posted[0])
# print(f"Type of posted: {type(posted_num)}")
# print(f"Chapters posted: {chapters['posted']}")
data = work.json()
# print(f"Work: {data}")