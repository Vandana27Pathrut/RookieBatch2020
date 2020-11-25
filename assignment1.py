import csv
emps = []

def read_records():
    global emps
    with open('emp.csv','r') as f:
        rows = csv.DictReader(f)
        emps = [x for x in rows]

def correct_types():
    for e in emps:
        e['age'] = int(e['age'])

def find_average_age():
    avg_age = sum([x['age'] for x in emps]) / len(emps)
    return avg_age

def find_average_age_for_dept(dept):
    count = 0
    sum_age = 0
    for x in emps:
        if(x['dept'] == dept):
            x['age'] = int(x['age'])
            sum_age += x['age']
            count = count+1
    avg_age = sum_age / count
    return avg_age

def main():
    read_records()
    correct_types()
    print("Average emp age is : ", find_average_age())
    print("Average emp age for dept d1 is : ", find_average_age_for_dept("d1"))
    print("Average emp age for dept d2 is : ", find_average_age_for_dept("d2"))

if __name__ == "__main__":
    main()