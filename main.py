from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ----------------------------FIND PASSWORD---------------------------------------#
def find_password():

        website_search_by_user = my_website_entry.get().lower()


        try :
            with open("data.json") as data_file :
                data = json.load(data_file)

        #         this checks if user is checking for a password when there is no file , meaning there is no old data present
        # that means user has not stored any website till now
        except FileNotFoundError :
            messagebox.showerror(title="No data",message="Please store some data first")
        else:
            try:
                data[website_search_by_user]
            #     now we know that our file exist and there is data in it , now we check if the key entered by user exists or not
            # if it does not exist , the user might have left the field empty or the website is actually not in data
            except KeyError :
                if website_search_by_user == "" :
                    messagebox.showerror(title="empty field",message="please do not leave search field empty")
                else:
                    messagebox.showerror(title="No website found",message="This website has no data present , please check for any spelling errors.")
            else:
                # this means file exists , website searched by user also exists now we return the data to the user
                pass_to_show = data[website_search_by_user]["password"]
                messagebox.showinfo(title=f"website: {website_search_by_user}",message=f"password: {pass_to_show}")






# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    my_password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list_1 = [random.choice(letters) for num in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list_2 = [random.choice(symbols) for nums in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list_3 = [random.choice(numbers) for numss in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = password_list_1 + password_list_2 + password_list_3
    random.shuffle(password_list)

    password = "".join(password_list)
    my_password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = my_website_entry.get().lower()
    email = my_email_entry.get().lower()
    password = my_password_entry.get().lower()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if website.strip() == "" or password.strip() == "" or email.strip() == "":
        messagebox.showerror(title="Invalid Entry",message="You cant leave one or more fields empty.")
    else :

        user_choice = messagebox.askokcancel(title=website,
                                             message=f"Are these the correct details? \nEmail: {email} \nPassword: {password}")
        if user_choice:
            try :

                with open("data.json",mode="r") as data_file :
                    pass
            except FileNotFoundError :
                with open("data.json",mode="w") as data_file:

                    pass
                    #so if no file names data.json is present it get created as we already know it is a property of write mode


            finally:
                with open("data.json", mode="r") as data_file:
                    # reading the data
                    try :
                        data = json.load(data_file)
                    #     this data variable is like a dictionary so it works just like a dictionary,keep in mind
                    except json.decoder.JSONDecodeError:
                        data ={}
                    #     this ensures that our json file is not empty , as we know load(file) is not able to read empty
                    #     files and will end up throwing the error that we have covered already in our exception


                    # updating the data with new password ,email,website set
                    data.update(new_data)
                    # saving updated data
                with open("data.json", mode="w") as data_file:
                    json.dump(data,data_file,indent=4)


            clear()
            my_website_entry.focus()

def clear():
    my_website_entry.delete(0,END)
    my_password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
# window
my_window = Tk()
my_window.title("Password Manager")
my_window.config(padx=40,pady=40)


#canvas
my_canvas = Canvas(width=200,height=200)
my_image = PhotoImage(file = "logo.png")
my_canvas.create_image(100,100,image = my_image)
my_canvas.grid(row = 0, column = 1)
#website label
my_website_label = Label(text="Website:")
my_website_label.grid(row = 1 , column = 0)
# website entry
my_website_entry = Entry()
my_website_entry.config(width=33)
my_website_entry.focus()
my_website_entry.grid(row = 1 , column = 1, )
# search button
my_search_button = Button(text="Search",width = 14,command=find_password)
my_search_button.grid(row = 1,column = 2)
#email label
my_email_label = Label(text ="Email/Username:")
my_email_label.grid(row = 2, column = 0)
# email entry
my_email_entry = Entry()
my_email_entry.config(width = 52)
my_email_entry.grid(row =2, column = 1,columnspan = 2)
my_email_entry.insert(0,"ahuja17@gmail.com")
# password label
my_password_label = Label(text = "Password")
my_password_label.grid(row = 3 , column = 0)
# password entry
my_password_entry = Entry()
my_password_entry.config(width = 33)
my_password_entry.grid(row = 3 , column = 1)

#generate password button
my_generate_password_button = Button(text="Generate Password",command=generate_password)
my_generate_password_button.grid(row = 3, column = 2)
#add button
my_add_button = Button(text="Add",width=44,command=save)
my_add_button.grid(row = 4 , column = 1,columnspan = 2)


my_window.mainloop()