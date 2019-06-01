import requests
import random
from timeit import default_timer as timer

exam_result = {
    1: 'AA',
    2: 'BA',
    3: 'BB',
    4: 'CB',
    5: 'CC',
    6: 'DD',
    7: 'FD',
    8: 'FF'
}

for i in range(3000):
    rand = random.randint(1,8)
    requests.get('http://127.0.0.1:12345/create?sentence=utku{}:{}'.format(str(i), exam_result[rand]))

start = timer()
data = requests.get('http://127.0.0.1:12345/get/utku3000')
end = timer()
print(end-start)


