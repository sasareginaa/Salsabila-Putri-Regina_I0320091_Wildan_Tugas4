#Soal 6

a = 4
b = 11

#a bitwise OR (|)
c = a | b
print('\n**********OR**********')
print('nilai :',a,' , binary :', format(a,'08b'))
print('nilai :',b,' , binary :', format(b,'08b'))
print('------------------------------------------ (|)')
print('nilai :',c,' , binary :', format(c,'08b'))

#b bitwise shif right (>>)
c = a >> b
print('\n**********>>**********')
print('nilai :',a,' , binary :', format(a,'08b'))
print('nilai :',b,' , binary :', format(b,'08b'))
print('---------------------------------------- (>>)')
print('nilai :',c,' , binary :', format(c,'08b'))

#c bitwise XOR (^)
c = a ^ b
print('\n**********XOR**********')
print('nilai :',a,' , binary :', format(a,'08b'))
print('nilai :',b,' , binary :', format(b,'08b'))
print('----------------------------------------- (^)')
print('nilai :',c,' , binary :', format(c,'08b'))

#d bitwise NOT (~)
c = ~a
print('\n**********NOT**********')
print('nilai :',a,' , binary :', format(a,'08b'))
print('----------------------------------------- (~)')
print('nilai :',c,' , binary :', format(c,'08b'))

#e bitwise AND (&)
c = b & a
print('\n**********AND**********')
print('nilai :',b,' , binary :', format(b,'08b'))
print('nilai :',a,' , binary :', format(a,'08b'))
print('---------------------------------------- (&)')
print('nilai :',c,' , binary :', format(c,'08b'))