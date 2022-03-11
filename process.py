log_file = open("um-server-01.txt") #this is opening the file allowing it to be used by the current file


# def sales_reports(log_file): #creating a function called sales_reports and passing in log_file as the parameter needed
#     for line in log_file: #this is a for loop iterating through each line in the file
#         line = line.rstrip() #this is stripping the white space off the right side of each line
#         day = line[0:3] #this is asking the loop to find the day located at the particular location on the line
#         if day == "Mon": #if statement to check if the day set on the previos line is equal to monday
#             print(line) #printing the completed line on our console


# sales_reports(log_file) #invoking the function, providing log_file as the parameter

def big_melon_order(log_file):
    for line in log_file:
        line = line.rstrip()
        melon_amount = int(line[16:18].rstrip())
        if melon_amount > 10:
            print(line)

big_melon_order(log_file)
