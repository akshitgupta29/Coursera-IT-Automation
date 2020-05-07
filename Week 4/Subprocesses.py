#needs to be executed in the linux terminal.

import subprocess
import os

subprocess.run(['dir'])

#the parent function is blocked unitl the child process completes. Hence, it has to wait till the execution of the child function get's over and then only can continue the exectuion.
subprocess.run(['sleep', '10'])

result = subprocess.run(['ls', 'hello.txt'])
print (result.returncode)

# Getting the output of the script in the python code itself.

'''To store the output, we use capture_output = True'''
#Need python 3.7, hence done directly on the web.

result = subprocess.run(['ls'], capture_output=True)
print(result.returncode)
print (result.stderr)
print (result.stdout)

#if a new variable is needed, the best practice is to copy all the evnironment variables, add the required line, and then run the subprocess command using the `env` parameter.
my_env = os.environ.copy()
my_env['PATH'] = os.pathsep.join(["/opt/myapp", my_env['PATH']])
result = subprocess.run(['/test'],env=my_env)
'''
Other arguments:
cwd
timeout
shell
'''



