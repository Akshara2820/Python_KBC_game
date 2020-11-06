
print("apka question apki screen ke upar ")
question=["1. what is the capital of INDIA ","2. who's won first cricket wold cup ","3. how many times has INDIA won the ICC world cup ",
"4.which is the national game in INDIA ","5. which is the national tree of india"]

first_option=["1.Dehradun","1.England","1. three time","1. cricket","1. Mango Tree"]
second_option=["2.Delhi","2.India","2. one time","2.hockey","2.Neem tree"]
third_option=["3.Rajsthan","3. pakistan","3.two time","3.Base Ball","3.Ficus bengalensis"]
forth_option=["4. Mumbai","4. Australia","4. Five time","4. Athletics","4.Banana tree"]
ans_key=[2,1,3,2,3]
i=0
l=(len(question))

while i<l:
    print(question[i])
    print(first_option[i])
    print(second_option[i])
    print(third_option[i])
    print(forth_option[i])
    
    user_answer=int(input("enter answer--"))
    
    if user_answer==ans_key[i]:
        print("your ans correct :) ")
    else:
        print("ohh!! sad :( you ans wrong")
        break
    i+=1