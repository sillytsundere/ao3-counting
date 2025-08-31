# Use the wendytg/ao3_api library
from ao3_api import AO3

# session = ao3_api.Session()
# work = ao3_api.Work(work_id="52884502", session=session)

url = "https://archiveofourown.org/works/45990127"
workid = AO3.utils.workid_from_url(url)
print(f"Work ID: {workid}")
work = AO3.Work(workid)
print(f"Chapters: {work.nchapters}")