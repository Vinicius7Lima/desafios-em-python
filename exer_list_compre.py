seq_num = '123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789'
nove = '.'.join([seq_num[x: x + 9] for x in range(0, len(seq_num), 9)])
print(nove)






