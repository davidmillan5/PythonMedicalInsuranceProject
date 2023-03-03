# Python Strings: Medical Insurance Project

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""


print(medical_data)

updated_medical_data = medical_data.replace("#", "$")

print(updated_medical_data)

num_records = 0

for data in updated_medical_data:
    if(data == "$"):
        num_records +=1

print("There are "+ str(num_records)+ " medical records in the data.")

medical_data_split = updated_medical_data.split(";")

#print(medical_data_split)

medical_records = []

for record in medical_data_split:
  medical_records.append(record.split(','))
print(medical_records)

medical_records_clean = []

medical_records_clean = []

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

print(medical_records_clean)


for record in medical_records_clean:
    record[0] = record[0].upper()
    print(record[0])

names = []
ages = []
bmis = []
insurance_costs = []


for data in medical_records_clean:
    names.append(data[0])
    ages.append(data[1])
    bmis.append(data[2])
    insurance_costs.append(data[3])

print("Names: " + str(names))
print("Ages: " + str(ages))
print("bmis: " + str(bmis))
print("Insurance Costs: " + str(insurance_costs))

total_bmi = 0

for bmi in bmis:
    total_bmi += float(bmi)
    average_bmi = total_bmi / len(bmis)
    print("Average BMI: {}".format(average_bmi))

total_cost = 0

updated_costs = [cost.replace('$', '') for cost in insurance_costs]
# print(("The list after removal of character : " + str(updated_costs)))

for cost in updated_costs:
    total_cost += float(cost)

average_cost = total_cost / len(insurance_costs)
print("Average insurance cost: {}".format(average_cost))

for i in medical_records_clean:
    print(str(i[0].title().split()[0]) + " is " +str(i[1]) + " years old with a BMI of " + str(i[2] + " and an insurance cost of " + str(i[3]) + ".\n"))