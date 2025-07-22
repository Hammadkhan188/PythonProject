courses=["msoffice","html","flutter","php","c#","mern","react","css","uiux","bootstrap"]

print(courses[6])
print(courses[-3])
print(courses[-1])
print(courses[2:6])



courses.append("php")
print(f"after append {courses}")

courses.append("headoop")
print(f"after append {courses}")

courses.insert(2,"python")
print(f"after insert {courses}")

print(f"Size of length:{len(courses)}")

more_courses=("mongobd","nodejs","vuels","sql")
courses.extend(more_courses)
print(courses)

print(f"Size of length:{len(courses)}")

courses.remove("html")
print(f"after removing {courses}")

courses.pop()
print(f"after pop {courses}")

print(f"Size of length:{len(courses)}")

courses.sort()
print(f"assending order {courses}")

courses.sort(reverse=True)
print(f"dessending order {courses}")

more_courses=("urdu","iot","networking")
courses.extend(more_courses)
print(courses)

print(f"Size of length:{len(courses)}")

courses.clear()
print(f"after clearing list :{courses}")

print(f"Size of length:{len(courses)}")