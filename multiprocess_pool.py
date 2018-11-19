from multiprocessing import Pool
import time 
starttime = time.time()
def f(x):
    return x*x

if __name__ == '__main__':
    	p = Pool(10)
        print(p.map(f, range(1,10000000)))

endtime = time.time()  - starttime

print(endtime)


#new_start_time = time.time()

#print(map(f, range(1,10000000)))

#new_end_time = time.time() - new_start_time

#print(new_end_time)
