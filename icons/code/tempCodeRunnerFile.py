 self.book_name=StringVar()
        self.lbl_name=Label(self.bottomFrame,text="Book:",font='arial 15 bold',fg='white',bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.combo_name=ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
        self.combo_name['values']=book_list
        self.combo_name.current(self.book_id-1)
        self.combo_name.place(x=150,y=45)
        
    
        
        #PHone no-----
        self.member_name = StringVar()
        self.lbl_phone=Label(self.bottomFrame,text="Member:",font='arial 15 bold',fg='white',bg='#fcc324')
        self.lbl_phone.place(x=40,y=80)
        self.combo_member=ttk.Combobox(self.bottomFrame,textvariable=self.member_name)
        self.combo_member['values']=member_list
        self.combo_member.place(x=150,y=85)
   
    
    
    
    ##Buttonn---------
        btn=Button(self.bottomFrame,text='Lend Book')
        btn.place(x=270,y=120)