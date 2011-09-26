from os import*
o=[]
for c in read(0,9**9):
 o.append({'>':'p+=1','<':'p-=1','+':'s[p]+=1','-':'s[p]-=1','.':
 'write(1,chr(s[p]))',',':'s[p]=ord(read(0,1))','[':
 'while s[p]!=0:',']':0}.get(c,''))
r='s=[0]*8**5'
p=0
for e in o:
 if e==0:p-=1
 else:
  r+='\n'+' '*p+e
  if'!'in e:p+=1
exec(r)
