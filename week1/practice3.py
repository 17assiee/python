#1
def is_alive(health):
    if health <= 0:
        return False
    else:
        return True
print(is_alive(21))
print(is_alive(-21))
print(is_alive(0))
print("\n")

#2
import datetime
def season_events(number_of_month):
    months = ('January','February','March','April','May','June','July','August','September','October','November','December')

    if number_of_month > 12:
        return "You need to enter the real number of the month"
    elif number_of_month == 12 or number_of_month <= 2:
        return "You were born in " + months[number_of_month-1] + ", when white snow fell outside the window."
    elif number_of_month > 2 and number_of_month <= 5:
        return "You were born in " + months[number_of_month-1] + ", when birds sang beautiful songs."
    elif number_of_month > 5 and number_of_month <= 8:
        return "You were born in " + months[number_of_month-1] + ", when the sun shone brighter than ever."
    else:
        return "You were born in " + months[number_of_month-1] + ", when the harvest was incredible."

month_number = int(input("month number: "))
print(season_events(month_number))

#3
def check_pass(pswd):
    err = {
        "uppercase_error" : "You need to have at least 1 uppercase character",
        "lowecase_error" : "You need to have at least 1 lowercase character",
        "num_error" : "You need to have at least 1 number",
        "sp_char_error" : "You need to have at least 1 special character",
        "too_long_error" : "Your password is might be difficult to remember. you should make it shorter",
        "too_short_error" : "Your password is too short. It will be easy to crack it. Again"
    }

    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    specialcharacters="*-#"
    u, l, n, s = 0, 0, 0, 0

    
    if len(pswd) > 8:
        return err["too_long_error"]
    elif len(pswd) < 8:
        return err["too_short_error"]
    else:
        
        for i in pswd:
            if (i in uppercase):
                u+=1           
            if (i in lowercase):
                l+=1           
            if (i in numbers):
                n+=1           
            if(i in specialcharacters):
                s+=1
        
        if u > 0 and l > 0 and n > 0 and s > 0:
            return "The password is perfect"
        else:
            if u == 0:
                return err["uppercase_error"]
            elif l == 0:
                return err["lowecase_error"]
            elif n == 0:
                return err["num_error"]
            else:
                return err["sp_char_error"]


print(check_pass("loooooooooooooooooong"))
print(check_pass("short"))

