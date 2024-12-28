file = open("data/simulation_data.txt")
data = file.readlines()

file2 = open("data/u_ex.txt")
data2 = file2.readlines()

print("\n\tSimulation\tExact")
print("Length ",len(data),"\t\t",len(data2))

numbers2 = [float(x) for x in data2[len(data2)-1].split()]
numbers = [float(x) for x in data[len(data)-1].split()]
print("Max    ",max(numbers),"\t",max(numbers2))
print("Idx    ",numbers.index(max(numbers)),"\t\t",numbers2.index(max(numbers2)))
file.close()






