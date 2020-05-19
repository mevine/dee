#data modelling//#
playlist = {
    "title":"kizomba" , 
    "author":"mevjones",
    "song": 
    [
        {"title":"song1","artist":["koffi"],"duration":2.5},
        {"title":"song2","artist":["kereni","dj daluki"],"duration":5.25},
        {"title":"vee","artist":["sepere"],"duration":2.9}

        ]
}
total_length = 0  
for song in playlist ["song"] :
   # print(song["title"]) //prints title of song//
   total_length += song["duration"]
   print(total_length)


#//dictionary comprehension//
numbers = dict(first = 1,second = 2,third = 3)
squared_numbers={key:value **2 for key,values in numbers.items()}
print (squared_numbers)