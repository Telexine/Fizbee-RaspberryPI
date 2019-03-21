![img](https://github.com/Telexine/Fizbee-WEB-People-In-Area/blob/master/Fizbee-poster.jpg?raw=true)


Fizbee - Raspberry PI
================
RPI Unit of https://github.com/Telexine/Fizbee-WEB-People-In-Area

Requirements
------------
- Raspberry PI 3 (Bluetooth Supported)
- python

Installation
------------

```sh
$ pip i requirements.txt
```
<Create Firebase Project, enable readwrite Realtime Database>

### Edit Firebase URL

```sh
(line 4)firebaseURL = 'https://<url-path>.firebaseio.com' 
```
 

Run
------------

```sh
$ sudo python ./daemon.py
```
 
