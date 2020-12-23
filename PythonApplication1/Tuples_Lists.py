
#MySequence = (1, 3, 6, 4, 1, 2)

#print (MySequence[-2])
#for countseq=0 to len(MySequence)

#next countseq

#B=["a","b","c"]
#print (B[1:])


#tuple1 = ("disco",10,1.2 )
#print (type(tuple1))


album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print (album_set3)
print (album_set1.issubset(album_set2))

D={'a':0,'b':1,'c':2}
print (D["a"])
print(D.keys())