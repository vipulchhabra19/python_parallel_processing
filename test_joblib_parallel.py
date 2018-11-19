import time
import multiprocessing
from joblib import Parallel, delayed
from math import sqrt

start_time = time.time()

num_cores = multiprocessing.cpu_count()
print("num_cores", num_cores)

square_list = [] 

#def prl_sqr():
#	with Parallel(n_jobs=4) as parallel:	
#		for i in range(1,2000000):
#			print "sssss", time.time() - start_time
#			square_list.append(i*i)
#prl_sqr()

def process_sqr(i):
	sqr = i*i
	print sqr
	return sqr

res = Parallel(n_jobs=2)(delayed(process_sqr)(i) for i in range(200000))
end_time = time.time()
final_time =  end_time - start_time
print(final_time)

	
