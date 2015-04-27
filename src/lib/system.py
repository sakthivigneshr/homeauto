import os
import subprocess
import shlex

def sys_call(cmd):
	cmd = shlex.split(cmd)
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	return out, err

def simple_sys_call(cmd):
	os.system(cmd)
