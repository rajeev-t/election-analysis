voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for data_pt in voting_data:
    print(f"{data_pt['county']} county has {data_pt['registered_voters']:,} registered voters.")