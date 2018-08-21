'''
Brief:
    Quick script to install and then play with pyrw

Author(s):
    Charles Machalow
'''

import os
import sys

THIS_FILE = os.path.abspath(__file__)
THIS_FOLDER = os.path.abspath(os.path.dirname(THIS_FILE))

if __name__ == '__main__':
#    if 'TEST_AND_GO' in os.environ:
        from pyrw.rwe import ReadWriteEverything
        rwe = ReadWriteEverything()
        print ('| --------------------------------------------- |')
        print ('| rwe object has been created for your usage... |')
        print ('| %-45s |' % rwe.getRWEVersion())
        print ('| --------------------------------------------- |')
        data = rwe.readPCI(0,31,0)
        print (data[0], data[1])        
        gpiobase = data[0x48] + data[0x49] * 256 + data[0x4a]*256*256 + data[0x4b] *245*256*256 - 1
#gpiobase = data[0] + data[1] * 256+ data[2] * 256 * 256 + data[3] *256*256*256
        print ('%#x' % gpiobase)
        gpio=91
        gpioport = gpiobase + 0x100 + gpio * 8
        print ('Set owner')
        print ('%#x' % gpioport)
        data = rwe.readIO32(gpioport)
        rwe.writeIO32(gpioport, 0x80000001)
        # rwe.getRWEVersion()
#        print ('%#x' % data)
        # we should be interactive..
#    else:
#        os.chdir(THIS_FOLDER)
#        os.system('%s -m pip install . --force-reinstall > nul 2>&1' % sys.executable)
#        os.environ['TEST_AND_GO'] = '1'
#        os.system('%s -i %s' % (sys.executable, THIS_FILE))
