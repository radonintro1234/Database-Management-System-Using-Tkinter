#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from csvToPdf import CsvtoPDF
from dbToCSV import toCSV
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

__version__ = "0.1.1 for Windows 10"
__author__ = "Rishi Mule, Shubham Mulik, Gaurav Gend"
__license__ = 'MIT'

# from dialog import OptionDialog
# import pymysql


def create_database():
    """Function to create a Database"""
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books_data (book_id INTEGER PRIMARY KEY AUTOINCREMENT, book_name text , author_name text , pages INTEGER , genre text , book_type text ,rating INTEGER, comment text)")
    conn.commit()
    conn.close()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Inventory():
    """Creating a main window on My Book App"""

    def __init__(self, root):
        """Default __INIT__ Function"""

        self.root = root
        self.root.title("My Book Management App")
        self.root.geometry("1200x660+160+80")
        self.root.resizable(0, 0)

        self.book_id_var = StringVar()
        self.book_name_var = StringVar()
        self.author_name_var = StringVar()
        self.pages_var = StringVar()
        self.genre_var = StringVar()
        self.book_type_var = StringVar()
        self.rating_var = StringVar()

        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()

        head_title = Label(self.root, text="My Books", bd=10, relief=GROOVE, font=(
            "ariel", 20, "bold"), bg="NAVY BLUE", fg="white")
        head_title.pack(side="top", pady=20, padx=10, fill=X)

        # ===================================================================================================================================
        # ===============================MANAGE_FRAME========================================================================================
        # ===================================================================================================================================

        Manage_Frame = Frame(self.root, bd=5, relief=RIDGE, bg="ROYALBLUE")
        Manage_Frame.place(x=10, y=80, width=350, height=570)

        m_title = Label(Manage_Frame, text="Manage Book Details",
                        font=("", 20, "bold"), bg="ROYALBLUE", fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        # ------------------------------------------------------------------------------------------------------------------------------------

        def caps(event):
            """Function to Convert Text To UPPERCAP"""
            self.book_id_var.set(self.book_id_var.get().upper())
            self.book_name_var.set(self.book_name_var.get().upper())
            self.author_name_var.set(self.author_name_var.get().upper())
            self.pages_var.set(self.pages_var.get().upper())
            self.book_type_var.set(self.book_type_var.get().upper())
            self.rating_var.set(self.rating_var.get().upper())
            self.search_txt_var.set(self.search_txt_var.get().upper())

        # ------------------------------------------------------------------------------------------------------------------------------------

        lbl_book_id = Label(Manage_Frame, text="Book No. : ", font=(
            "", 10, "bold"), bg="ROYALBLUE", fg="white")
        lbl_book_id.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        txt_book_id = Entry(Manage_Frame, font=(
            "times new roman", 13, "bold"), bd=2, relief=GROOVE, textvariable=self.book_id_var)
        txt_book_id.bind("<KeyRelease>", caps)
        txt_book_id.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # ------------------------------------------------------------------------------------------------------------------------------------

        lbl_type = Label(Manage_Frame, text="Book Name : ", font=(
            "", 10, "bold"), bg="ROYALBLUE", fg="white")
        lbl_type.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        txt_type = Entry(Manage_Frame, font=("times new roman", 13, "bold"),
                         bd=2, relief=GROOVE, textvariable=self.book_name_var)
        txt_type.bind("<KeyRelease>", caps)
        txt_type.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # ------------------------------------------------------------------------------------------------------------------------------------

        lbl_author_name = Label(Manage_Frame, text="Author : ", font=(
            "", 10, "bold"), bg="ROYALBLUE", fg="white")
        lbl_author_name.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        txt_model_id = Entry(Manage_Frame, font=(
            "times new roman", 13, "bold"), bd=2, relief=GROOVE, textvariable=self.author_name_var)
        txt_model_id.bind("<KeyRelease>", caps)
        txt_model_id.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # ------------------------------------------------------------------------------------------------------------------------------------

        lbl_pages = Label(Manage_Frame, text="Pages : ", font=(
            "", 10, "bold"), bg="ROYALBLUE", fg="white")
        lbl_pages.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        txt_pages = Entry(Manage_Frame, font=(
            "times new roman", 13, "bold"), bd=2, relief=GROOVE, textvariable=self.pages_var)
        txt_pages.bind("<KeyRelease>", caps)
        txt_pages.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # ------------------------------------------------------------------------------------------------------------------------------------

        lbl_genre = Label(Manage_Frame, text="Genre : ", font=(
            "", 10, "bold"), bg="ROYALBLUE", fg="white")
        lbl_genre.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        combo_genre = ttk.Combobox(Manage_Frame, width=18, font=(
            "", 13, "bold"), state="readonly", textvariable=self.genre_var)
        combo_genre["values"] = ("SCIENCE FICTION",
        						 "BIOGRAPHY",
                                 "FANTASY",
                                 "ADVENTURE",
                                 "MYSTERY",
                                 "HORROR",
                                 "SUSPENSE",
                                 "ROMANCE",
                                 "GRAPHIC NOVEL",
                                 "SHORT STORIES",
                                 "OTHERS"
                                 )
        combo_genre.current(0)
        combo_genre.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        # ------------------------------------------------------------------------------------------------------------------------------------

        lbl_book_type = Label(Manage_Frame, text="Book Type : ", font=(
            "", 10, "bold"), bg="ROYALBLUE", fg="white")
        lbl_book_type.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        txt_book_type = Entry(Manage_Frame, font=(
            "times new roman", 13, "bold"), bd=2, relief=GROOVE, textvariable=self.book_type_var)
        txt_book_type.bind("<KeyRelease>", caps)
        txt_book_type.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        # ------------------------------------------------------------------------------------------------------------------------------------

        lbl_rating = Label(Manage_Frame, text="Rating : ", font=(
            "", 10, "bold"), bg="ROYALBLUE", fg="white")
        lbl_rating.grid(row=7, column=0, padx=10, pady=10, sticky="w")

        txt_rating = Entry(Manage_Frame, font=(
            "times new roman", 13, "bold"), bd=2, relief=GROOVE, textvariable=self.rating_var)
        txt_rating.bind("<KeyRelease>", caps)
        txt_rating.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # ------------------------------------------------------------------------------------------------------------------------------------

        lbl_comment = Label(Manage_Frame, text="Comment : ", font=(
            "", 10, "bold"), bg="ROYALBLUE", fg="white")
        lbl_comment.grid(row=8, column=0, padx=10, pady=10, sticky="w")

        self.txt_comment = Text(Manage_Frame, width=20, height=3,
                                bd=2, relief=GROOVE, font=("times new roman", 13, ""))
        self.txt_comment.grid(row=8, column=1, padx=10, pady=10, sticky="w")

        # ------------------------------------------------------------------------------------------------------------------------------------

        # ===================================================================================================================================
        # ==========================BUTTON_FRAME=============================================================================================
        # ===================================================================================================================================

        Button_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="SLATEGREY")
        Button_Frame.place(x=5, y=500, width=330, height=50)

        # ------------------------------------------------------------------------------------------------------------------------------------
        add_button = Button(Button_Frame, text="Add", width=8,
                            highlightbackground="SLATEGREY", command=self.add_items)
        add_button.grid(row=0, column=0, padx=5, pady=7)

        # ------------------------------------------------------------------------------------------------------------------------------------
        update_button = Button(Button_Frame, text="Update", width=8,
                               highlightbackground="SLATEGREY", command=self.update_data)
        update_button.grid(row=0, column=1, padx=5, pady=7)

        # ------------------------------------------------------------------------------------------------------------------------------------
        delete_button = Button(Button_Frame, text="Delete", width=8,
                               highlightbackground="SLATEGREY", command=self.delete_data)
        delete_button.grid(row=0, column=2, padx=5, pady=7)

        # ------------------------------------------------------------------------------------------------------------------------------------
        clear_button = Button(Button_Frame, text="Clear", width=10,
                              highlightbackground="SLATEGREY", command=self.clear)
        clear_button.grid(row=0, column=3, padx=5, pady=7)

        # ===================================================================================================================================
        # ==========================DETAIL_FRAME=============================================================================================
        # ===================================================================================================================================

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="ROYALBLUE")
        Detail_Frame.place(x=370, y=80, width=820, height=570)

        # ===================================================================================================================================
        # ==========================SEARCH_FRAME=============================================================================================
        # ===================================================================================================================================

        Search_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="NAVYBLUE")
        Search_Frame.place(x=10, y=10, width=792, height=60)

        lbl_search = Label(Search_Frame, text="Search By : ",
                           font=("", 13, "bold"), bg="NAVYBLUE", fg="WHITE")
        lbl_search.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        combo_search_by = ttk.Combobox(Search_Frame, width=13, font=(
            "", 13, ""), state="readonly", textvariable=self.search_by_var)
        combo_search_by["values"] = ("All",
                                     "Book No.",
                                     "Book Title",
                                     "Author",
                                     "Pages",
                                     "Genre",
                                     "Type",
                                     "Rating")
        combo_search_by.current(0)
        combo_search_by.grid(row=0, column=1, padx=2, pady=10, sticky="w")

        txt_search = Entry(Search_Frame, width=22, font=(
            "times new roman", 15), bd=2, relief=GROOVE, textvariable=self.search_txt_var)
        txt_search.bind("<KeyRelease>", caps)
        txt_search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        search_button = Button(Search_Frame, text="Search", width=8,
                               highlightbackground="NAVYBLUE", command=self.search_data)
        search_button.grid(row=0, column=3, padx=4, pady=5)

        view_button = Button(Search_Frame, text="View All", width=8,
                             highlightbackground="NAVYBLUE", command=self.view_data)
        view_button.grid(row=0, column=4, padx=9, pady=5)

        tocsv_button = Button(Search_Frame, text="Export", width=8,
                              highlightbackground="NAVYBLUE", command=self.export_data)
        tocsv_button.grid(row=0, column=5, padx=9, pady=5)

        # ===================================================================================================================================
        # ==========================TABLE_FRAME=============================================================================================
        # ===================================================================================================================================

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="NAVYBLUE")
        Table_Frame.place(x=10, y=80, width=792, height=472)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.View_Table = ttk.Treeview(Table_Frame, columns=("bookid", "bookname", "author", "pages", "genre",
                                                             "book_type", "rating", "comment"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.View_Table.xview)
        scroll_y.config(command=self.View_Table.yview)

        self.View_Table.heading("bookid", text="Book No.")
        self.View_Table.heading("bookname", text="Book Title")
        self.View_Table.heading("author", text="Author")
        self.View_Table.heading("pages", text="Pages")
        self.View_Table.heading("genre", text="Genre")
        self.View_Table.heading("book_type", text="Type")
        self.View_Table.heading("rating", text="Rating")
        self.View_Table.heading("comment", text="Comment")

        self.View_Table.column("bookid", width=60, anchor=CENTER)
        self.View_Table.column("bookname", width=400, anchor=CENTER)
        self.View_Table.column("author", width=170, anchor=CENTER)
        self.View_Table.column("pages", width=60, anchor=CENTER)
        self.View_Table.column("genre", width=110, anchor=CENTER)
        self.View_Table.column("book_type", width=150, anchor=CENTER)
        self.View_Table.column("rating", width=60, anchor=CENTER)
        self.View_Table.column("comment", width=500, anchor=CENTER)

        self.View_Table["show"] = "headings"
        self.View_Table.pack(fill=BOTH, expand=1)
        self.View_Table.bind("<ButtonRelease-1>", self.get_cursor)

        self.view_data()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def add_items(self):
        """Function to ADD item to Database"""

        from math import floor
        checks = True

        if self.book_id_var.get() == "":
            checks = False
            messagebox.showerror("Error", "Book ID. cannot be blank!!!")

        if self.rating_var.get() != "":
            if int(floor(float(self.rating_var.get()))) > 10 or int(floor(float(self.rating_var.get()))) < 0:
                checks = False
                messagebox.showerror("Error", "Rating should be less than 10.")

        if checks:
            try:
                con = sqlite3.connect('inventory.db')
                cur = con.cursor()
                cur.execute(" insert into books_data values (?,?,?,?,?,?,?,?)", (
                    self.book_id_var.get(),
                    self.book_name_var.get(),
                    self.author_name_var.get(),
                    self.pages_var.get(),
                    self.genre_var.get(),
                    self.book_type_var.get(),
                    int(floor(float(self.rating_var.get()))),
                    self.txt_comment.get('1.0', END),
                ))

                con.commit()
                self.view_data()
                con.close()

            except:
                print("error")
                pass

            else:
                self.clear()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def export_data(self):
        """Function to Expoet data into various Formats"""
        que1 = messagebox.askquestion("Export",
                                      "Do you want to export to CSV?",
                                      icon='info')
        if que1 == 'yes':
            toCSV()

        que2 = messagebox.askquestion("Export",
                                      "Do you want to export to PDF?",
                                      icon='info')

        if que2 == 'yes':
            CsvtoPDF()


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def view_data(self):
        """Function to VIEW data into Table"""

        self.search_txt_var.set("")
        con = sqlite3.connect('inventory.db')
        cur = con.cursor()
        cur.execute("select * from books_data ORDER BY book_id")
        rows = cur.fetchall()
        self.View_Table.delete(*self.View_Table.get_children())
        if len(rows) != 0:
            for row in rows:
                self.View_Table.insert("", END, values=row)
            con.commit()
        con.close()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def clear(self):
        """Function to CLEAR all Input Fields"""

        self.book_id_var.set("")
        self.book_name_var.set("")
        self.author_name_var.set("")
        self.pages_var.set("")
        self.book_type_var.set("")
        self.rating_var.set("")
        self.txt_comment.delete("1.0", END)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_cursor(self, event):
        """Function to SELECT a particular item"""

        try:
            cursor_row = self.View_Table.focus()
            contents = self.View_Table.item(cursor_row)
            row = contents["values"]

            self.book_id_var.set(row[0])
            self.book_name_var.set(row[1])
            self.author_name_var.set(row[2])
            self.pages_var.set(row[3])
            self.genre_var.set(row[4])
            self.book_type_var.set(row[5])
            self.rating_var.set(row[6])
            self.txt_comment.delete("1.0", END)
            self.txt_comment.insert(END, row[7])

        except:
            pass

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def update_data(self):
        """Function to UPDATE an item of Database"""

        con = sqlite3.connect('inventory.db')
        cur = con.cursor()
        cur.execute("update books_data set  book_name=? , author_name=? , pages=? , genre=? , book_type=? ,rating=?, comment=? where book_id=?", (
            self.book_name_var.get(),
            self.author_name_var.get(),
            self.pages_var.get(),
            self.genre_var.get(),
            self.book_type_var.get(),
            self.rating_var.get(),
            self.txt_comment.get('1.0', END),
            self.book_id_var.get()
        ))
        con.commit()
        self.view_data()
        self.clear()
        con.close()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def delete_data(self):
        """Function to DELETE an item from the Database"""

        con = sqlite3.connect('inventory.db')
        cur = con.cursor()
        cur.execute("delete from books_data where book_id=?",
                    (self.book_id_var.get(),))
        con.commit()
        self.view_data()
        self.clear()
        con.close()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def search_data(self):
        """Function to Search for items in Database"""

        con = sqlite3.connect('inventory.db')
        cur = con.cursor()

        if self.search_by_var.get() == "Book No.":
            cur.execute("select * from books_data where book_id LIKE ?",
                        ("%" + self.search_txt_var.get() + "%",))
            rows = cur.fetchall()

        elif self.search_by_var.get() == "Book Title":
            cur.execute("select * from books_data where book_name LIKE ?",
                        ("%" + self.search_txt_var.get() + "%",))
            rows = cur.fetchall()

        elif self.search_by_var.get() == "Author":
            cur.execute("select * from books_data where author_name LIKE ?",
                        ("%" + self.search_txt_var.get() + "%",))
            rows = cur.fetchall()

        elif self.search_by_var.get() == "Pages":
            cur.execute("select * from books_data where pages LIKE ?",
                        ("%" + self.search_txt_var.get() + "%",))
            rows = cur.fetchall()

        elif self.search_by_var.get() == "Genre":
            cur.execute("select * from books_data where genre LIKE ?",
                        ("%" + self.search_txt_var.get() + "%",))
            rows = cur.fetchall()

        elif self.search_by_var.get() == "Type":
            cur.execute("select * from books_data where book_type LIKE ?",
                        ("%" + self.search_txt_var.get() + "%",))
            rows = cur.fetchall()

        elif self.search_by_var.get() == "Rating":
            cur.execute("select * from books_data where rating LIKE ?",
                        ("%" + self.search_txt_var.get() + "%",))
            rows = cur.fetchall()

        else:
            cur.execute("select * from books_data where book_id LIKE ? OR book_name LIKE ? OR author_name LIKE ? OR pages LIKE ? OR genre LIKE ? OR book_type LIKE ? OR rating LIKE ?", ("%" + self.search_txt_var.get() + "%",
                                                                                                                                                                                         "%" + self.search_txt_var.get() + "%",
                                                                                                                                                                                         "%" + self.search_txt_var.get() + "%",
                                                                                                                                                                                         "%" + self.search_txt_var.get() + "%",
                                                                                                                                                                                         "%" + self.search_txt_var.get() + "%",
                                                                                                                                                                                         "%" + self.search_txt_var.get() + "%",
                                                                                                                                                                                         "%" + self.search_txt_var.get() + "%",
                                                                                                                                                                                         ))
            rows = cur.fetchall()

        self.View_Table.delete(*self.View_Table.get_children())
        if len(rows) != 0:
            for row in rows:
                self.View_Table.insert("", END, values=row)
            con.commit()
        con.close()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    """START THE PROGRAM"""

    create_database()
    root = Tk()
    root.title("My Books")
    root.iconbitmap("icon.ico")
    ob = Inventory(root)
    root.mainloop()
