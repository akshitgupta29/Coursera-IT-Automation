# Linux Notes

- 0 = Stdin
- 1 = stdout
- 2 = stderr

- `tr` = truncate command eg. `tr ' ' '\n'`
- `ctrl + c` = send `sigint` signal that cleanly closes the program.
- `ctrl + z` = `sigstop` -  exits the program immediately.
    - can be brought back using the `fg` command.
    - can be sent back again using `bg` command.
- `kill` = send the sigterm signal.

- `jobs` = to check the list of the running jobs.
- `ps ax` = all the processes

- `basename` is a command that takes name and then the extenstions and just returns the name of the file without the extension.

- use `;` to run the multiple bash script in one single line

### Globs
- `*` any character matching, no matter how many times.
- `?` only single time matching.

### if-else

- checks the exit status as the conditions. If exit status == 0, then true.

- General Syntax:
```bash
if ls /etc/hosts; then
    echo "Hi"
else:
    echo "bye"
fi
```

## Test command.

- used to check the conditions present under the bash script.

- -n = to check if the string is empty or not.
```bash 
if test -n "$PATH"; then
    echo "Hi"
else:
    echo "bye"
fi
```

- The other way to do the same is using the brackets, that is more commonly used:

```bash
if [ -n "$PATH" ]; then
    echo "Hi"
```
NOTE: Space is very much important here. 

### While Loops

- Access the command line argument using `$1, $2` etc.

### For loops

TIP: Adding a echo in front of any script that modifies the file system, we can save lot of pain and see what is actually happeneing.

### Cut Command:

Syntax: 

`cut -d" " -f5-`

- -d for the delimitr
- -f5- : tells that we need the 5th columns.

`cut -d' ' -f5- /var/log/syslog/ | sort | uniq -c | sort -nr | head`

- cut the revelant info.
- sort it alphabetically.
- find the unique elements and give them a number.
- sort on the basis of the number using -nr.
- get the top 10 values.

`grep " jane " ../data/list.txt | cut -d ' ' -f 1,3`

Returns a set of columns.










