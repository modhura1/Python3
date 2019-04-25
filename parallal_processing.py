import multiprocessing as mp

def jobA(num, q):
    q.put(num * 2)

def jobB(num, q):
    q.put(num ^ 3)

import multiprocessing as mp
q = mp.Queue()
jobs = (jobA, jobB)
args = ((50, q), (6, q))
for job, arg in zip(jobs, args):
    mp.Process(target=job, args=arg).start()

for i in range(len(jobs)):
    print('Result of job {} is: {}'.format(i, q.get()))
