import aubio
import numpy as np
import pyaudio
import wave
import os.path

from tkinter import *
from tkinter import font

root = Tk()
root.geometry("1350x680")


helv36 = font.Font(family="Musiqwik",size=50,weight="bold")
v = StringVar()

Lh = Label(root, text = "Piano Teacher -- Developed by Dass S.")
Lh.grid(row=0, column=0)




L1 = Label(root, text = '', font=helv36)
L1.grid(row=3, column=0)

L2 = Label(root, text = '')
L2.grid(row=4, column=0)

img = PhotoImage(file="piano.png") 

L4 = Label(root, image= img)
L4.grid(row=5, column=0)

# Creating a photoimage object to use image 



arrvalue = "a"
arrchar = "a"

marryhad = np.array(["", "E4", "D4", "C4", "D4", "E4", "E4", "E4",
    "D4", "D4", "D4", "E4", "G4", "G4", "E4", "D4", "C4", "D4", "E4", 
    "E4", "E4", "E4", "D4", "D4", "E4", "D4", "C4" "" ])

arrTest = marryhad
#array value0
keynotes = np.array([32.703, 34.648, 36.708, 38.891, 41.208, 43.654, 46.249, 48.999, 51.913, 55.000, 58.270, 61.735,
    130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94,
    261.63, 277.18, 293.67, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88])

#keyvalue = np.array(["C", "C#", "D", "D#", "E","F", "F#", "G", "G#", "A", "A#","B"])
keyvalue = np.array(["C1", "C1#", "D1", "D1#", "E1","F1", "F1#", "G1", "G1#", "A1", "A1#","B1",
    "C3", "C3#", "D3", "D3#", "E3","F3", "F3#", "G3", "G3#", "A3", "A3#","B3", 
    "C4", "C4#", "D4", "D4#", "E4","F4", "F4#", "G4", "G4#", "A4", "A4#","B4"])

keychar = np.array(["C1", "C1#", "D1", "D1#", "E1","F1", "F1#", "G1", "G1#", "A1", "A1#","B1",
    "C3", "C3#", "D3", "D3#", "E3","F3", "F3#", "G3", "G3#", "A3", "A3#","B3", 
    "R", "E1", "S", "D2", "T","U", "F4#", "V", "G4#", "W", "A4#","X"])

#arrTest = np.array(["dump","C4","D4","C4","D4","dump","dump"])
arrTestText = ""
for index, value in np.ndenumerate(arrTest):
    arrTestText = arrTestText + ' '.join(map(str, keychar[np.where(keyvalue == value)[0]]))

L3 = Label(root, text = arrTestText,  font=helv36)
L3.grid(row=1, column=0)

L5 = Label(root, text = ' '.join(map(str, arrTest)))
L5.grid(row=2, column=0)


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx

def autdiofun():
    if (len(L1['text']) + 2) > len(arrTest):
        print("fucntion exit")
        return

    # PyAudio object.
    p = pyaudio.PyAudio()

    # Open stream.
    stream = p.open(format=pyaudio.paFloat32,
        channels=1, rate=44100, input=True,
        frames_per_buffer=1024)

    # Aubio's pitch detection.
    pDetection = aubio.pitch("default", 2048,
        2048//2, 44100)
    # Set unit.
    pDetection.set_unit("Hz")
    pDetection.set_silence(-40)

    lcount = 0
    countarr = np.array(["Dass","","","", "", ""])

    #while True:
    for x in range(30):

        data = stream.read(1024)
        
        samples = np.fromstring(data,
            dtype=aubio.float_type)
        pitch = pDetection(samples)[0]
        # Compute the energy (volume) of the
        # current frame.
        #volume = np.sum(samples**2)/len(samples)
        # Format the volume output so that at most
        # it has six decimal numbers.
        #volume = "{:.6f}".format(volume)
        if pitch != 0.0:

            if arrTest[len(L1['text']) + 1] + ".png" != L4['image']:

                if os.path.exists(arrTest[len(L1['text']) + 1] + ".png"):
                    img = PhotoImage(file=arrTest[len(L1['text']) + 1] + ".png")
                    L4.configure(image = img)
                    L4.image = img
                else:
                    img = PhotoImage(file="piano.png")
                    L4.configure(image = img)
                    L4.image = img

            pitch2, note = find_nearest(keynotes, pitch)
            lcount = lcount + 1
            countarr[lcount] = keyvalue[note]
            #print('ssss', keyvalue[note], lcount, countarr[lcount])
            
            if lcount >= 5:
                lcount = 0
                countarr[1] = ""
                countarr[2] = ""
                countarr[3] = ""
                countarr[4] = ""


            if countarr[1] == countarr[2] and countarr[2] == countarr[3] and countarr[3] == countarr[4] and note != len(keyvalue) and lcount ==4 and countarr[2] != '':
                print(len(L1['text']), arrTest, arrvalue, pitch, pitch2, note, keyvalue[note], countarr, lcount)    
                #arrvalue = arrvalue + keyvalue[note]
                #arrchar = arrchar + keychar[note]

                    #L4.pack()

                if len(arrTest) > (len(L1['text'])):
                    if arrTest[len(L1['text']) + 1] == keyvalue[note]:
                        print("matcheeddddd")
                        L1['text'] = L1['text'] + keychar[note]
                        L2['text'] = L2['text'] + keyvalue[note]
                    else:
                        print("noooooooot")
                    #v.set(keychar[note])


    #print("termianlteds sdfsdlfsd")
    stream.stop_stream()
    stream.close()
    p.terminate()
    root.after(10, autdiofun)

        #print(volume)

#autdiofun()

root.after(100, autdiofun)

root.mainloop()
