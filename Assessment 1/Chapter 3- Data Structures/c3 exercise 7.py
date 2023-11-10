#Use reverse() and sorted() fucntions to re-arrange the list you have made
places_to_visit = ["Hongkong", "Seoul", "Paris", "New York"]

print("original order:", places_to_visit)

print("alphabetical order:", sorted(places_to_visit))

print("original order after sorting:", places_to_visit)

print("reverse alphabetical order:", sorted(places_to_visit, reverse=True))

print("original order after reverse sorting:", places_to_visit)

places_to_visit.reverse()
print("reversed order:", places_to_visit)

places_to_visit.reverse()
print("reverted to original order:", places_to_visit)

places_to_visit.sort()
print("sorted in alphabetical order:", places_to_visit)

places_to_visit.sort(reverse=True)
print("sorted in reverse alphabetical order:", places_to_visit)