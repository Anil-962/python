questions = [["Whick language is used to create fb?","Python","Java","Erlang","C++"],
                ["Which language is used to create instagram?","Python","Java","Erlang","C++"],
                ["Which language is used to create youtube?","Python","Java","Erlang","C++"]]


levels = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]} ")
    print(f"a.{questions[1]}       b.{questions[2]}")
    print(f"c.{questions[3]}       d.{questions[4]}")
    reply=int(input("Enter your option 1/2/3/4: "))
    if(reply==1):
        print("Correct Answer")
    else:
        print("Wrong Answer")
        break