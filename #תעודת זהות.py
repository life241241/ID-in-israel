#תעודת זהות
id = input("please enter your id: (except for the last number = 8 digits): ")
id1 = int(id[0]) * 1
id2 = int(id[1]) * 2
if id2 > 9 :
    id2 = str(id2)
    id2 = int(id2[0]) + int(id2[1])
id3 = int(id[2]) * 1
id4 = int(id[3]) * 2
if id4 > 9 :
    id4 = str(id4)
    id4 = int(id4[0]) + int(id4[1])
id5 = int(id[4]) * 1
id6 = int(id[5]) * 2
if id6 > 9 :
    id6 = str(id6)
    id6 = int(id6[0]) + int(id6[1])
id7 = int(id[6]) * 1
id8 = int(id[7]) * 2
if id8 > 9 :
    id8 = str(id8)
    id8 = int(id8[0]) + int(id8[1])
sum_id = id1 + id2 + id3 + id4 + id5 + id6 + id7 + id8
end = 100 - sum_id
end = end % 10



print(f"your all id number is: {id}{end}")