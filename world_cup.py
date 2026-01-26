# Write a python code block to create a dictionary of cricket World Cup winners.
# Let the key be the year; the value is the country that won the world cup that year.
# Print the name of the best performing country.
# Display the unique list of countries that have won the world cup.
world_cup_winners={
    1975: "West Indies",
    1980: "West Indies",
    1999: "Australia",
    2003: "Australia",
    2011: "India",
    2015: "Australia",
}
countries=list(world_cup_winners.values())
best_country=max(set(countries),key=countries.count)
print("Best Performing Country:",best_country)
for country in set(countries):
    print(country,"won",countries.count(country),"times")
