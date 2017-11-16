""" Networking study guide.
    I am writing a dictionary of items to study for my networking course.
    The goal of this project is to be an all-encompassing dictionary of terms and items.
    To retrieve an answer you search via raw input.
    written in Python 2.7
    
    Copyright Alex Clark November 2017
"""
def ipv4():
  print """
    IPv4
    Internet Protocol version 4
    example 192.168.0.5
    v4 is 32 bits
    """

def ipv6():
    print """
    IPv6
    Internet Protocol version 6
    example 2001L0DB8:AC10:FE01:0000:0000:0000:0000
    v6 is 128 bits
    """
def client():
    print """
    client is a pc. an example of a client is what you are holding.
    a host is a web server
    """

def bastion():
    print """
    a bastion host is the device open to the internet. it's the
    gateway between the networld and the world wide web. it's outside the dmz
    and is generally protected pretty well. built with a single prupose
    such as a proxy server
    """

def proxy():
    print """
    a proxy server is a server that acts as a middle man
    for communications. when a client requests a connection the
    request goes to the proxy server. then the request is forwarded
    from the proxy to the location of the information requested
    """

search_word = raw_input("what are you searching for? ")
if search_word == "ipv4":
    ipv4()
elif search_word == "ipv6"
    ipv6()
elif search_word == "client":
    client()
elif search_word == "host":
    client()
elif search_word == "bastion":
    bastion()
elif search_word == "proxy":
    proxy()
else:
    print "enter something valid"
