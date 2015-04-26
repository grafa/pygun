#!/usr/bin/env python

from pygun.pygun import PyGun


m = PyGun("key-e9df5d8209160c7d6a0fbf68a735d03d", "sandboxbcf4ef3bde1d4b9e88c0a2d4e8afb579.mailgun.org")
m.sender("postmaster@sandboxbcf4ef3bde1d4b9e88c0a2d4e8afb579.mailgun.org", "Mailgun Sandbox")
m.to("hrdina.pavel@gmail.com", "Pavel")
m.subject("Test z notebooku")
m.text("testovaci text")
print m.send()
