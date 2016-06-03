# serial-pi
I was tired of buying expensive serial console hardware, just to be able
to get remote access to the terminals of firewalls and switches.

It uses python, screen and curses.

For the Hardware i typically use a Raspberry Pi und a USB -> 4x RS232
adaptor (like Digitus-DA-70159-RS232).

## Installation
serialpiconfig.py needs to be modified to your needs. Just change the 
values of name and device-files.

`$ git clone https://github.com/mvelten/serial-pi.git`
`$ cd serial-pi`

### create configuration
`$ cp serialpiconfig.py.example serialpiconfig.py`
`$ vi serialpiconfig.py`

## auto install
`$ sudo ./setup.sh`


### optional: place ssh public key
Copy your public ssh key (identity.pub) to the device
`$ mkdir .ssh`
`$ chmod 700 .ssh`
`$ cd .ssh`
`$ touch authorized_keys`
`$ chmod 600 authorized_keys`
`$ cat ../identity.pub >> authorized_keys`


