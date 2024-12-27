# CIT-254

**hacking-labs** - A script used to change the TCP/IP addresses in the CIT-254 lab enviornment for my _CIT-254 Ethical Hacking_ classes.<br />
Copyright &copy; (2022-2024) Dr. Matthew Kisow. All rights reserved.</br>
Dr. Matthew Kisow <mkisow@ccac.edu>

## Tasks
- [ ] NONE

## Installation
1. Following the instructions for your distribution, install git.
2. Using the _mkdir_ command, create a directory called */Lab Files* at the root of the drive.
```shell
          cd /
          mkdir "/Lab Files"
```
3. Using the _curl_ command, download the **hacking-labs** script executable.
```shell
         curl -s -L "https://github.com/DoctorKisow/CIT-254/raw/main/hacking-labs" >> hacking-labs
```
4. Using the _chmod_ command, change the permissions of the **hacking-labs** script to _750_.
```shell
          chmod 750 hacking-labs

```
5. Using the _hacking-labs_ command, change the depolyed enviornment ip addresses **hacking-labs** command using the _-i_ switch.
```shell
          bash hacking-labs -i <a.b.c.d>
```
6. Using the _chown_ command, change the ownership of the **hacking-labs** script to _root:labuser_.
```shell
          chown root:labuser hacking-labs
```


## Script Notes
By typing _hacking-labs_ with no options, or _hacking-labs -h_ you can get help.

## Warning
This is a learning and teaching tool _ONLY_ and should _NOT_ be used in a _PRODUCTION_ enviornment!

## License
This work is licensed under the Creative Commons Attribution-NoDerivatives 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nd/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
