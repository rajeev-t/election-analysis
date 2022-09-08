print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]

if counties[1] == 'Denver':
    print(counties[1])

temp = int(input("What is the temperature outside?"))

if temp > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

x = 0

while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422849, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

counties_dict = {"Arapahoe": 422849, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")