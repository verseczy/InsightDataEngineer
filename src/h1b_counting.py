#import xlrd
import csv
import codecs
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from io import StringIO
import sys
from case_class import Case

dict_job = {}
dict_state = {}
id_case = -1
id_job = -1
id_state = -1

def savetodict(lll):
	global dict_job
	global dict_state
	fc=StringIO(lll)
	rr=csv.reader(fc, delimiter=';')
	for row in rr:
		_case_number = row[id_case]
		_job_titile = row[id_job]
		_work_state = row[id_state]
	_case = Case(_case_number, _job_titile, _work_state)
	#if dict_job.__contains__(_case.Job_Title) == False:
	#	dict_job[_case.Job_Title] = 0
	dict_job[_case.Job_Title] += 1 
	#if dict_state.__contains__(_case.Worksite_State) == False:
	#	dict_state[_case.Worksite_State] = 0
	dict_state[_case.Worksite_State] += 1
	return _work_state

def createdicttable(lll):
	global dict_job
	global dict_state
	fc=StringIO(lll)
	rr=csv.reader(fc, delimiter=';')
	for row in rr:
		_case_number = row[id_case]
		_job_titile = row[id_job]
		_work_state = row[id_state]
		dict_job[_job_titile] = 0
		dict_state[_work_state] = 0

if __name__ == "__main__":
	#start_time = time.time()
	filename = "../input/h1b_input.csv"
	#filename = sys.argv[0]
	ll = codecs.open(filename, encoding = 'utf-8').read().split("\n")
	tlabel = ll[0].split(';')
	for i in range(0,len(tlabel)):
		if tlabel[i] == "CASE_NUMBER":
			id_case = i
		elif tlabel[i] == "SOC_NAME":
			id_job = i
		elif tlabel[i] == "WORKSITE_STATE":
			id_state = i

	try:
		ll.remove('')
	except Exception as e:
		pass
	
	ll.remove(ll[0])
	list(map(createdicttable, ll))
	fl=list(map(savetodict, ll))

	#start_time = time.time()
	job_list = sorted(dict_job.items(), key = lambda item : (-item[1], item[0]))
	state_list = sorted(dict_state.items(), key = lambda item : (-item[1], item[0]))
	#end_time = time.time()
	#print(end_time - start_time)

	sum_job = 0
	sum_state = 0
	start_time1 = time.time()
	for i in range(0, min(10, len(job_list))):
		sum_job += job_list[i][1]
	end_time = time.time()
	#print(end_time - start_time)
	
	f_job = open("../output/top_10_occupations.txt", 'w+')
	#f_job = open(sys.argv[1], 'w+')
	print("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE", file = f_job)
	for i in range(0, min(10, len(job_list))):
		percent = round((job_list[i][1] / sum_job * 100), 1)
		percent = str(percent) + "%"
		print(str(job_list[i][0])+";"+str(job_list[i][1])+";"+percent, file = f_job)

	for i in range(0, min(10, len(state_list))):
		sum_state += state_list[i][1]
	f_state = open("../output/top_10_states.txt", 'w+')
	#f_state = open(sys.argv[2], 'w+')
	print("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE", file = f_state)
	for i in range(0, min(10, len(state_list))):
		percent = round((state_list[i][1] / sum_state * 100), 1)
		percent = str(percent) + "%"
		print(str(state_list[i][0])+";"+str(state_list[i][1])+";"+percent, file = f_state)

	#end_time = time.time()
	#print(end_time - start_time)

	print("finished.")