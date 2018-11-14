# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:38:07 2018

@author: 94
"""

import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
print(sr.Microphone.list_microphone_names())
print("say something")
with mic as source:
    audio = r.listen(source)

print("stop saying")
recorded_string=r.recognize_google(audio)
print("recorded string: "+recorded_string)
#i=0
#while i < len(recorded_string):
#    print(recorded_string[i])
#    if (recorded_string[i]=='x'):
#        print("this is it")
#    i+=1

# removing spaces
new=recorded_string.replace("time","x").replace("times","x").replace("bar","x").replace("part","x").replace("baar","x").replace(" ","")

print("processed string: "+new)



#processing the x/times
#condition (1) the string must contain only numbers and x
#condition (2) x should not be in the beginning or end
i=0
x=0
newlist1=list(new)
newlist2=[]
while i < (len(newlist1)):
    x=0
    if ((newlist1[i]=='x')|(newlist1[i]=='X')):
        frequency=int(newlist1[i-1])
        newlist2[len(newlist2)-1]=newlist1[i+1]
        while x < (frequency-2):
            newlist2.append(newlist1[i+1])
            x+=1
    else:
        newlist2.append(newlist1[i])
    i+=1
print("Final number :{}".format("".join(newlist2)))

print("done till here")