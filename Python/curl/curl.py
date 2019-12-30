import pycurl
c = pycurl.Curl()
c.setopt(c.URL, 'https://www.raspberrypi.org/homepage-9df4b/static/2efe82d07c653f3f638c0cbf54346b5d/bc3a8/67d8fcc5b2796665a45f61a2e8a5bb7f10cdd3f5_raspberry-pi-3-1-1619x1080.jpg')
fp = open('o2.jpg', 'wb')
c.setopt(c.WRITEFUNCTION, fp)
c.perform()
