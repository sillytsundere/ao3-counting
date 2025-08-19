# Use the wendytg/ao3_api library
import ao3_api
print(ao3_api.__file__)
session = ao3_api.Session()
work = ao3_api.Work(work_id="52884502", session=session)