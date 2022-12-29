# Enter your code here. Read input from STDIN. Print output to STDOUT
tot_eng = input()
eng_student = set(map(lambda a: int(a), input().split(" ")))
tot_french = input()
french_student = set(map(lambda a: int(a), input().split(" ")))

union = eng_student.union(french_student)
print(len(union))
