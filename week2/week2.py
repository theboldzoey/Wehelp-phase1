def find_and_print(messages):

    strings =''
    names=''
    for i in messages:
        if "18" in messages[i] or "college" in messages[i] or "legal" in messages[i] or "vote" in messages[i]:
            names += i + ", "
    print("======= Task 1 =======")
    print(names)


find_and_print({
"Bob":"My name is Bob. I'm 18 years old.", "Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.", "Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week", "Jenny":"Good morning."
})

# ------------Task 2------------------------------------------------
def calculate_sum_of_bonus(data):
    print("======= Task 2 =======")
    employees = data["employees"]
    exchange_rate = 30
    bonus_sum = 0
    bonus_percentage = 0

    #先讀取 data 中的資料，放進指定變數中，後續可以計算
    for employee in employees:
        salary = employee["salary"]
        if isinstance(salary, str) and salary.endswith("USD"):
            salary = int(salary[:-3]) * exchange_rate
        elif isinstance(salary, str) and "," in salary:
            salary = str(salary).replace(",","")
        salary = int(salary)
        performance = employee["performance"]
        role = employee["role"]
        name = employee["name"]
    
        #定義獎金結構
        if role == "CEO":
            if performance == "above average":
                bonus_percentage = 0.08
            elif performance == "average":
                bonus_percentage = 0.05
            elif performance == "below average":
                bonus_percentage = 0.025
        elif role == "Sales" or role == "Engineer":
            if performance == "above average":
                bonus_percentage = 0.05
            elif performance == "average":
                bonus_percentage = 0.03
            elif performance == "below average":
                bonus_percentage = 0.15
        

        bonus = salary * bonus_percentage

        if (bonus_sum + bonus) > 10000:
            bonus = 10000 - bonus_sum   
        print(f"{role} {name}'s bonus is NT{bonus}")

        bonus_sum += bonus
    

    
    print(f"Sum of bonuses: {bonus_sum}")
        


calculate_sum_of_bonus({ "employees":[
{
    # Key-value pair
    "name":"John","salary":"1000USD", "performance":"above average", "role":"Engineer"
}, {
    "name":"Bob", "salary":60000, "performance":"average", "role":"CEO"
}, {
    "name":"Jenny", "salary":"50,000", "performance":"below average", "role":"Sales"
} ]
}) # call calculate_sum_of_bonus function

# ------Task 3 ------------------------------------------------------------------------
print("======= Task 3 =======")
def func(*data):
# your code here
    # 先用一個回圈把全部的中間名存到一個 list 裏面
    # for names in data:
    #     print(names[1])
    #     middlenames = []
    #     middlenames += names[1]

    # print(middlenames)
        #再用一個回圈讀取所有的名字，先將對應到該回圈 names 的 middlename remove
        #再把剩下的跟 names[1] 做比較，有重複的話不印，不重複才把 names 印出來
    # for names in data:
    #     actingMD = middlenames
    #     print(f"actingMD is {actingMD}")
    #     actingMD.remove(names[1])
    #     if names[1] in actingMD:
    #         print("")
    #     else:
    #         print(names)
    middle_names = [name.split(' ')[-1] if ' ' in name else name[-1] for name in data]
    unique_middle_names = [name for name in middle_names if middle_names.count(name) == 1]

    if len(unique_middle_names) == 1:
        return [name for name in data if unique_middle_names[0] in name][0]
    else:
        return '沒有'



func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有


print("======= Task 4 =======")
#There is a number sequence: 0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, ...
def get_number(index):
    sequence = [0]
    index += 1
    for i in range(1, index):
        if i % 2 != 0:
            sequence.append(sequence[i-1] + 4)
        else:
            sequence.append(sequence[i-1] - 1)

    print(sequence[-1])

get_number(5) # print 10 get_number(10) # print 15
get_number(10)


print("======= Task 5 =======")
def find_index_of_car(seats, status, number):
# your code here
    print("")



find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4 
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1 
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2


