#Goal: Experiment with Lists and Differennt Functions

months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']

print(months)
#traverse/iterate

# for month in months:
#     print(f"{month}, 2025")

months.reverse()
print(months)

#difference between a list and a string
full_name = "Jahra Adan Fabon"

new_list = list(full_name) #converts string to list
new_list.reverse()
print(new_list)

new_list.sort()
print(new_list)
