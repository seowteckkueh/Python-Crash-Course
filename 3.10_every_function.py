#list of countries
countries=['malaysia','singapore','myanmar','thailand','usa','china','australia']

#del function
del countries[-1]
print(countries)

#append function
countries.append('australia')
print(countries)

#pop function
work=countries.pop(2)
print(countries)
print(work)

#insert function
countries.insert(1,work)
print(countries)

#sorted
print(sorted(countries))
print(countries)

#sorted reverse
print(sorted(countries,reverse=True))
print(countries)

#reverse
countries.reverse()
print(countries)
countries.reverse()
print(countries)
#sort
countries.sort()
print(countries)
#sort reverse
countries.sort(reverse=True)
print(countries)


