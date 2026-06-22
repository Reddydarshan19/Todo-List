


print('                 TODO LIST BY DARSHAN 😎')
print('')
while True:

    print('1. For Add Task')
    print('2. for View all task')
    print('3. for Delete task')
    print('4. for Exit App')
    print("")
    try:
        a = int(input('Enter Your Choise : '))
        if a >= 5:
            print("BRO Choose From The Menu Only (1 To 4) 🛑🛑")
        print("")

        if a == 1:
            task = (input('Enter Your Task : '))
            if task == "":
                print("You Didn't Type Your Task first fill it 😐")
                print("")
            
            else:
                tasks = task.split(' ')
                
                file = open("tasks.txt", "a")
                for t in tasks:
                    file.write(t.strip() + "\n")
                file.close()
                print('Task added successfully ✅')
                print("")

        elif a == 2:
            try:
                file = open("tasks.txt", "r")
                task = file.readlines()
                file.close()
                if not task:
                    print("File Is Empty 🙄")
                    print("")
                else:   
                    print('⬇️   Your Task : ')
                    print("")
                    
                    for i in range(len(task)):
                        print(f'{i + 1}. {task[i].strip()}')
                    print("")
            except FileNotFoundError:
                print("First Add Task 😄")
                print("")

        elif a == 3:
            try:
                file = open("tasks.txt", "r")
                tasks = file.readlines()
                file.close()
                if not tasks:
                    print("Your File Is Empty Task Not Added Yet 😄")
                    print("")
                else:
                    print("⬇️   Your Tasks:")
                    print("")
                    for i in range(len(tasks)):
                        print(f'{i + 1}. {tasks[i].strip()}')
                        print("")
                    nums = input("Enter task number to delete : ")
                    if nums == "":
                        print("You Left It Empty 🤨")
                        print("")
                    nums = nums.split()
                    
                    try:
                        for n in sorted(nums, reverse = True):
                            n = int(n)
                            if 1<= n <= len(tasks):
                                tasks.pop(n - 1)
                                file = open("tasks.txt", "w")
                                file.writelines(tasks)
                                file.close()
                                print("")
                                print("Task deleted successfully ✅")       
                                print("")
                            else:
                                print("")
                                print("Write Task Number Only. (To Delete It 🙄)")
                                print("")
                    except ValueError:
                        print("")
                        print("Write Task Number Only. (To Delete It 🙄)")
                        print("")
            except FileNotFoundError:
                print("First Add Task 😄")
                print("")

        elif a == 4:
           print('App Closed Bye 😁👋🏻')
           break

    except ValueError:
        print("Choose From The Menu Only (1 To 4) 🛑")
        print("")