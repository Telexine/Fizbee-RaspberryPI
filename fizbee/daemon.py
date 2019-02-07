import pexpect

res = open("mac.txt", 'w')
 
child = pexpect.spawn("bluetoothctl")
child.send("scan on\n")
mac_addrs = []

try:
    while True:
        child.expect("Device (([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2}))")
        mac_addr = child.match.group(1)
        if mac_addr not in mac_addrs:
            mac_addrs.append(mac_addr)
            res.write(mac_addr+"\n")
except KeyboardInterrupt:
    child.close()
    res.close()