# Dictionary is a special structure that lets us store info in key-valued pairs
#   if I want to access a piece of info, I can refer to it by its key
# Example: Jan -> January / Feb -> February / etc...

# Dictionaries are kept in curly brackets
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConversions["Nov"])                              # November
print(monthConversions.get("Dec"))                          # December
print(monthConversions.get("Luv", "Not valid"))             # Not Valid (default value for if first parameter doesn't exist)
