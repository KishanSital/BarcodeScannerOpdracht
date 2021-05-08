from tkinter import *
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


image = cv2.imread("Capture.PNG")

decodedObjects = pyzbar.decode(image)
for obj1 in decodedObjects:

        b = obj1.data

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
error = 0

while True:
        _, frame = cap.read()

        decodedobjects = pyzbar.decode(frame)
        for obj in decodedobjects:
            a = obj.data


            if b == a:
                cv2.destroyAllWindows()


                def open_encode():

                    def show_data():
                        txt.delete(0.0, 'end')
                        textName = ent.get()
                        textName1 = ent1.get()
                        b = str(textName)
                        a = int(textName1)
                        h = str(a)
                        dic = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
                               "L": 11,
                               "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20,
                               "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "0": 26, "1": 27, "2": 28, "3": 29, "4": 30,
                               "5": 31,
                               "6": 32, "7": 33, "8": 34, "9": 35, " ": 36}
                        dic2 = {v: k for k, v in dic.items()}

                        string = (b).upper()
                        key = (a)

                        list = (dic[x] for x in string)
                        encodeNums = ((x + key) % 37 for x in list)
                        encodeStr = (dic2[x] for x in encodeNums)
                        d = str("".join(encodeStr))
                        txt.insert(1.0, d)

                        file = open(b + "." + h + ".txt", "w+")
                        file.write(d)
                        file.close()

                    root = Tk()
                    root.geometry("360x300")

                    l1 = Label(root, text="Naam & Gebruikers: ")
                    l2 = Label(root, text="Sleutel", )
                    l3 = Label(root, text="Encoded", )

                    ent = Entry(root)
                    ent1 = Entry(root)

                    l1.grid(row=0)
                    l2.grid(row=1)
                    l3.grid(row=4)
                    ent.grid(row=0, column=1)
                    ent1.grid(row=1, column=1)

                    btn = Button(root, text="Bereken", bg="blue", fg="white", command=show_data)
                    btn.grid(row=2, column=1)

                    txt = Text(root, width=25, height=1, wrap=WORD)
                    txt.grid(row=4, column=1, sticky=W)

                    root.mainloop()


                def open_decode():

                    def show_data():
                        txt.delete(0.0, 'end')
                        textName = ent.get()
                        textName1 = ent1.get()
                        b = str(textName)
                        a = int(textName1)

                        f = open(b + ".txt", "r")
                        if f.mode == "r":
                            contents = f.read()
                            txt1.insert(1.0, contents)

                        dic = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
                               "L": 11,
                               "M": 12,
                               "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20,
                               "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "0": 26, "1": 27, "2": 28, "3": 29, "4": 30,
                               "5": 31,
                               "6": 32,
                               "7": 33, "8": 34, "9": 35, " ": 36}
                        dic2 = {v: k for k, v in dic.items()}

                        string = (contents).upper()
                        key = (a)
                        key = -key

                        list = (dic[x] for x in string)
                        encodeNums = ((x + key) % 37 for x in list)
                        encodeStr = (dic2[x] for x in encodeNums)
                        d = str("".join(encodeStr))
                        txt.insert(1.0, d)

                        file = open(b + "d" + ".txt", "w+")
                        file.write(d)
                        file.close()

                    root = Tk()
                    root.geometry("360x300")

                    l1 = Label(root, text="File naam: ")
                    l2 = Label(root, text="Sleutel", )
                    l3 = Label(root, text="Encode", )
                    l4 = Label(root, text="Decode", )

                    ent = Entry(root)
                    ent1 = Entry(root)

                    l1.grid(row=0)
                    l2.grid(row=1)
                    l3.grid(row=4)
                    l4.grid(row=5)
                    ent.grid(row=0, column=1)
                    ent1.grid(row=1, column=1)

                    btn = Button(root, text="Bereken", bg="blue", fg="white", command=show_data)
                    btn.grid(row=2, column=1)

                    txt = Text(root, width=25, height=1, wrap=WORD)
                    txt.grid(row=5, column=1, sticky=W)

                    txt1 = Text(root, width=25, height=1, wrap=WORD)
                    txt1.grid(row=4, column=1, sticky=W)

                    root.mainloop()


                menu = Tk()
                menu.title("License")
                menu.configure(background='lightyellow')

                label_1 = Label(menu, text="License",
                                bd=1,
                                relief="solid",
                                background='lightblue',
                                font="Times 32",
                                width=55,
                                height=4)

                label_1.pack()

                button: Button = Button(menu, text="                  Encode                  ", command=open_encode,
                                        bg='lightblue')
                button.pack(side=LEFT)

                button: Button = Button(menu, text="          Decode         ", command=open_decode,
                                        bg='lightblue')
                button.pack(side=RIGHT)

                menu.geometry("550x300+120+120")
                menu.mainloop()



            else :
                print("Porbeer opnieuw")
                c = "Probeer opnieuw"
                cv2.putText(frame, str(c), (50, 50), font, 2,
                          (255, 0, 0), 3)
                if error == 2:

                    cv2.destroyAllWindows()

                    from tkinter import *
                    import os


                    def login():


                        def delete3():
                            screen4.destroy()

                        def delete4():
                            screen5.destroy()


                        def password_not_recognised():
                            global screen4
                            screen4 = Toplevel(screen)
                            screen4.title("Success")
                            screen4.geometry("150x100")
                            Label(screen4, text="Wachtwoord verkeerd").pack()
                            Button(screen4, text="OK", command=delete3).pack()

                        def user_not_found():
                            global screen5
                            screen5 = Toplevel(screen)
                            screen5.title("Success")
                            screen5.geometry("150x100")
                            Label(screen5, text="Gebruiker niet in systeem").pack()
                            Button(screen5, text="OK", command=delete4).pack()

                        def login_verify():
                            username1 = username_verify.get()
                            password1 = password_verify.get()
                            username_entry1.delete(0, END)
                            password_entry1.delete(0, END)

                            list_of_files = os.listdir()
                            if username1 in list_of_files:
                                file1 = open(username1, "r")
                                verify = file1.read().splitlines()
                                if password1 in verify:
                                    cv2.destroyAllWindows()

                                    def open_encode():

                                        def show_data():
                                            txt.delete(0.0, 'end')
                                            textName = ent.get()
                                            textName1 = ent1.get()
                                            b = str(textName)
                                            a = int(textName1)
                                            h = str(a)
                                            dic = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
                                                   "I": 8, "J": 9, "K": 10,
                                                   "L": 11,
                                                   "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18,
                                                   "T": 19, "U": 20,
                                                   "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "0": 26, "1": 27,
                                                   "2": 28, "3": 29, "4": 30,
                                                   "5": 31,
                                                   "6": 32, "7": 33, "8": 34, "9": 35, " ": 36}
                                            dic2 = {v: k for k, v in dic.items()}

                                            string = (b).upper()
                                            key = (a)

                                            list = (dic[x] for x in string)
                                            encodeNums = ((x + key) % 37 for x in list)
                                            encodeStr = (dic2[x] for x in encodeNums)
                                            d = str("".join(encodeStr))
                                            txt.insert(1.0, d)

                                            file = open(b + "." + h + ".txt", "w+")
                                            file.write(d)
                                            file.close()

                                        root = Tk()
                                        root.geometry("360x300")

                                        l1 = Label(root, text="Naam & Gebruikers: ")
                                        l2 = Label(root, text="Sleutel", )
                                        l3 = Label(root, text="Encoded", )

                                        ent = Entry(root)
                                        ent1 = Entry(root)

                                        l1.grid(row=0)
                                        l2.grid(row=1)
                                        l3.grid(row=4)
                                        ent.grid(row=0, column=1)
                                        ent1.grid(row=1, column=1)

                                        btn = Button(root, text="Bereken", bg="blue", fg="white", command=show_data)
                                        btn.grid(row=2, column=1)

                                        txt = Text(root, width=25, height=1, wrap=WORD)
                                        txt.grid(row=4, column=1, sticky=W)

                                        root.mainloop()

                                    def open_decode():

                                        def show_data():
                                            txt.delete(0.0, 'end')
                                            textName = ent.get()
                                            textName1 = ent1.get()
                                            b = str(textName)
                                            a = int(textName1)

                                            f = open(b + ".txt", "r")
                                            if f.mode == "r":
                                                contents = f.read()
                                                txt1.insert(1.0, contents)

                                            dic = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
                                                   "I": 8, "J": 9, "K": 10,
                                                   "L": 11,
                                                   "M": 12,
                                                   "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
                                                   "U": 20,
                                                   "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "0": 26, "1": 27,
                                                   "2": 28, "3": 29, "4": 30,
                                                   "5": 31,
                                                   "6": 32,
                                                   "7": 33, "8": 34, "9": 35, " ": 36}
                                            dic2 = {v: k for k, v in dic.items()}

                                            string = (contents).upper()
                                            key = (a)
                                            key = -key

                                            list = (dic[x] for x in string)
                                            encodeNums = ((x + key) % 37 for x in list)
                                            encodeStr = (dic2[x] for x in encodeNums)
                                            d = str("".join(encodeStr))
                                            txt.insert(1.0, d)

                                            file = open(b + "d" + ".txt", "w+")
                                            file.write(d)
                                            file.close()

                                        root = Tk()
                                        root.geometry("360x300")

                                        l1 = Label(root, text="File naam: ")
                                        l2 = Label(root, text="Sleutel", )
                                        l3 = Label(root, text="Encode", )
                                        l4 = Label(root, text="Decode", )

                                        ent = Entry(root)
                                        ent1 = Entry(root)

                                        l1.grid(row=0)
                                        l2.grid(row=1)
                                        l3.grid(row=4)
                                        l4.grid(row=5)
                                        ent.grid(row=0, column=1)
                                        ent1.grid(row=1, column=1)

                                        btn = Button(root, text="Bereken", bg="blue", fg="white", command=show_data)
                                        btn.grid(row=2, column=1)

                                        txt = Text(root, width=25, height=1, wrap=WORD)
                                        txt.grid(row=5, column=1, sticky=W)

                                        txt1 = Text(root, width=25, height=1, wrap=WORD)
                                        txt1.grid(row=4, column=1, sticky=W)

                                        root.mainloop()

                                    menu = Tk()
                                    menu.title("License")
                                    menu.configure(background='lightyellow')

                                    label_1 = Label(menu, text="License",
                                                    bd=1,
                                                    relief="solid",
                                                    background='lightblue',
                                                    font="Times 32",
                                                    width=55,
                                                    height=4)

                                    label_1.pack()

                                    button: Button = Button(menu, text="                  Encode                  ",
                                                            command=open_encode,
                                                            bg='lightblue')
                                    button.pack(side=LEFT)

                                    button: Button = Button(menu, text="          Decode         ", command=open_decode,
                                                            bg='lightblue')
                                    button.pack(side=RIGHT)

                                    menu.geometry("550x300+120+120")
                                    menu.mainloop()

                                else:
                                    password_not_recognised()

                            else:
                                user_not_found()

                        def login():
                            global screen
                            screen2 = Toplevel(screen)
                            screen2.title("Login")
                            screen2.geometry("300x250")
                            Label(screen2, text="Voer uw gegevens in").pack()
                            Label(screen2, text="").pack()

                            global username_verify
                            global password_verify

                            username_verify = StringVar()
                            password_verify = StringVar()

                            global username_entry1
                            global password_entry1

                            Label(screen2, text="Gebruikersnaam ").pack()
                            username_entry1 = Entry(screen2, textvariable=username_verify)
                            username_entry1.pack()
                            Label(screen2, text="").pack()
                            Label(screen2, text="Wachtwoord ").pack()
                            password_entry1 = Entry(screen2, textvariable=password_verify)
                            password_entry1.pack()
                            Label(screen2, text="").pack()
                            Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()

                        def main_screen():
                            global screen
                            screen = Tk()
                            screen.geometry("300x250")
                            screen.title("Log in scherm")
                            Label(text="Log in systeem", bg="grey", width="300", height="2",
                                  font=("Calibri", 13)).pack()
                            Label(text="").pack()
                            Button(text="Login", height="2", width="30", command=login).pack()
                            Label(text="").pack()

                            screen.mainloop()

                        main_screen()


                    login()



                else:
                    error = error + 1
                    cv2.destroyAllWindows()


            #print("Data", a)
            #print( obj.data)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:


            break


mainloop()
