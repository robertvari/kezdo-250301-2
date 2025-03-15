name_list = ['Olivia Robinson', 'Ella Lewis', 'Isabella Rodriguez', 'Sophia White', 'Mason Taylor', 'Mason Thomas', 'Alexander Taylor', 'Elijah Thompson', 'Sophia Harris', 'Mason Taylor', 'Olivia Clark', 'Emma Taylor', 'Elijah Lewis', 'Charlotte Walker', 'Mia Robinson', 'Isabella Lee', 'Olivia Brown', 'Alexander Smith', 'Noah Hall', 'James Brown']

def split_name(name):
    result = name.split()[-1]
    return result

print(sorted(    name_list, key=lambda name: name.split()[-1]  ))