import datetime
import time
import matplotlib.pyplot as plt

timesince = []
day = []
timetime = []
count = 0
fp = open('logfile','r')
for line in fp:
	if(line.find('Time since last spotted:') != -1):
		tmp = line.split()
		timesince.append(int(tmp[len(tmp)-2])/3600)
		time_struct = time.strptime(tmp[0] + ' ' + tmp[1] + ' ' + tmp[2] + ' ' + tmp[3] + ' ' + tmp[4])
		day.append(time_struct.tm_yday)
#		timetime.append(time_struct.tm_hour*60*60 + time_struct.tm_min*60 + time_struct.tm_sec)
		timetime.append(time_struct.tm_hour + time_struct.tm_min/60 + time_struct.tm_sec/3600)
		count = count + 1

today = day[0]
to_plot_time = []
to_plot_timesince = []
for i in range(0,count):
	if (day[i] == today):
		to_plot_time.append(timetime[i])
		to_plot_timesince.append(timesince[i])
	else:
		plt.plot(to_plot_time, to_plot_timesince)
		plt.show()
		to_plot_time = []
		to_plot_timesince = []
		today = day[i]
		to_plot_time.append(timetime[i])
		to_plot_timesince.append(timesince[i])
