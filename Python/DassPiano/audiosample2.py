import pyaudio
import numpy as np
import pylab
import time
from matplotlib import pyplot as plt 


CHUNK = 4096 # number of data points to read at a time
RATE = 44100  # time resolution of the recording device (Hz)

# def soundplot(stream):
#     t1=time.time()
#     data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
#     pylab.plot(data)
#     pylab.title(i)
#     pylab.grid()
#     pylab.axis([0,len(data),-2**16/2,2**16/2])
#     pylab.savefig("03.png",dpi=50)
#     pylab.close('all')
#     print("took %.02f ms"%((time.time()-t1)*1000))

# if __name__=="__main__":
#     p=pyaudio.PyAudio()
#     stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
#                   frames_per_buffer=CHUNK)
#     for i in range(int(20*RATE/CHUNK)): #do this for 10 seconds
#         soundplot(stream)
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

# create a numpy array holding a single read of audio data
i2 = 0
temparr = np.empty(0)

for i in range(200): #to it a few times just to see
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    if np.count_nonzero(data) > 0:
        if i2 + 1 == i:
            print(temparr, type(data))
            temparr = np.concatenate((temparr, data), axis=None)
            print('masssssss')
        elif(i2 != 0):

            print('epppppppp', temparr)
            plt.title("Matplotlib demo") 
            plt.xlabel("x axis caption") 
            plt.ylabel("y axis caption")
            y = 2 * temparr + 5 
            plt.plot(temparr,y, "ob") 
            plt.show()

            temparr = np.empty(0)
            temparr = np.concatenate((temparr, data), axis=None)

        else:
            print('errrrrr')
         
            temparr = np.empty(0)
            temparr = np.concatenate((temparr, data), axis=None)

        print(data.shape, i)
        i2 = i

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()
