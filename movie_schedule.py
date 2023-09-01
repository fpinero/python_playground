
# Let's create a dictionary
current_movvies = {'The Grind': '11:00am',
                   'Rudolph': '1:00pm',
                   'Frosty the Snowman': '5:00pm',
                   'Christmas Vacation': '5:00pm'}

print("We're showing the following movies:")
for key in current_movvies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movvies.get(movie)

if showtime == None:
    print("The requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)

