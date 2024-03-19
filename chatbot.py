from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  


class ChatBot:
     def __init__(self, root):
          self.root=root
          self.root.title("ChatBot")
          self.root.geometry("730x620+0+0")
          self.root.bind('<Return>', self.enter_func)


          main_frame= Frame(self.root,bd=4,bg='powder blue',width=610)
          main_frame.pack()


          img_chat=Image.open('vesitlogo.jpg')
          img_chat=img_chat.resize((100,70), Image.ANTIALIAS)
          self.photoimg=ImageTk.PhotoImage(img_chat)

          Title_label=Label(main_frame,bd=3,relief=RAISED, anchor='nw', width=730,compound=LEFT,image=self.photoimg,text='Chat with Me',font=('arial',30,'bold'), fg='navy blue', bg= 'white')
          Title_label.pack(side=TOP)

          self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
          self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
          self.scroll_y.pack(side=RIGHT,fill=Y)
          self.text.pack()


          btn_frame=Frame(self.root,bd=2,bg='powder blue',width=730)
          btn_frame.pack()

          label_1=Label(btn_frame,text="Type Something",font=('arial',14),fg='navy blue',bg= 'white')
          label_1.grid(row=0,column=0,padx=5,sticky=W)

          
          self.entry=StringVar()
          self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16))
          self.entry1.grid(row=0,column=1,padx=5,sticky=W)

          self.send=Button(btn_frame,text="send>>", command=self.send, font=('arial',16),fg='white',width=8,bg='navy blue')
          self.send.grid(row=0,column=2,padx=5,sticky=W)

          self.msg=''
          self.clear=Button(btn_frame,text="Clear", command=self.clear,font=('arial',16),fg='white',width=8,bg='navy blue')
          self.clear.grid(row=1,column=0,padx=5,sticky=W)

          self.label_11=Label(btn_frame,text=self.msg,font=('arial',14),fg='grey',bg= 'powder blue')
          self.label_11.grid(row=1,column=1,padx=5,sticky=W)



     # =====================Function Declaration======================================
     
     def enter_func(self,event):
          self.send.invoke()
          # self.entry.set('')

     def clear(self):
          self.text.delete('1.0', END)
          self.entry.set('')



     
     def send(self):
          send='\t\t\t'+'You: '+self.entry.get()
          self.text.insert(END, '\n'+send)
          self.text.yview(END)
          if (self.entry.get()=='hello'):
               self.text.insert(END, '\n'+ 'Bot: Hi, how may i assist you? \n\n')
          
          elif (self.entry.get()=='hi'):
              self.text.insert(END, '\n'+ 'Bot:  Hi, how may i assist you?\n\n')
         
          elif (self.entry.get()=='Hello'):
              self.text.insert(END, '\n'+ 'Bot: Hi, how may i assist you? \n\n')

          elif (self.entry.get()=='Hi'):
              self.text.insert(END, '\n'+ 'Bot: Hi, how may i assist you? \n\n')
        
          elif (self.entry.get()=='Helloo'):
              self.text.insert(END, '\n'+ 'Bot: Hi, how may i assist you? \n\n')

          elif (self.entry.get()=='Hii'):
              self.text.insert(END, '\n'+ 'Bot: Hi, how may i assist you? \n\n')
        
          
          elif (self.entry.get()=='when is traditional day'):
              self.text.insert(END, '\n'+ 'Bot: Traditional day is on the 15th of March \n\n')

          elif (self.entry.get()=='When is traditional day'):
              self.text.insert(END, '\n'+ 'Bot: Traditional day is on the 15th of March \n\n')

          elif (self.entry.get()=='when is Traditional day'):
              self.text.insert(END, '\n'+ 'Bot: Traditional day is on the 15th of March \n\n')

          elif (self.entry.get()=='When is Traditional day'):
              self.text.insert(END, '\n'+ 'Bot: Traditional day is on the 15th of March \n\n')

          elif (self.entry.get()=='WHEN IS TRADITIONAL DAY'):
              self.text.insert(END, '\n'+ 'Bot:  Traditional day is on the 15th of March\n\n')


          elif (self.entry.get()=='when is suit day'):
              self.text.insert(END, '\n'+ 'Bot: Suit day is on the 17th of March \n\n')

          elif (self.entry.get()=='When is suit day'):
              self.text.insert(END, '\n'+ 'Bot:  Suit day is on the 17th of March\n\n')

          elif (self.entry.get()=='when is Suit day'):
              self.text.insert(END, '\n'+ 'Bot: Suit day is on the 17th of March \n\n')

          elif (self.entry.get()=='suit day'):
              self.text.insert(END, '\n'+ 'Bot:  Suit day is on the 17th of March\n\n')

          elif (self.entry.get()=='SUIT DAY IS WHEN'):
              self.text.insert(END, '\n'+ 'Bot:  Suit day is on the 17th of March\n\n')


          elif (self.entry.get()=='is sleeveless allowed'):
              self.text.insert(END, '\n'+ 'Bot: sleeveless is not allowed in the college premises. Only decent piece \n of clothing is encouraged. \n\n')

          elif (self.entry.get()=='Is sleeveless allowed'):
              self.text.insert(END, '\n'+ 'Bot:  sleeveless is not allowed in the college premises. Only decent piece \n of clothing is encouraged. \n\n')

          elif (self.entry.get()=='sleeveless'):
              self.text.insert(END, '\n'+ 'Bot:  sleeveless is not allowed in the college premises. Only decent piece \n of clothing is encouraged. \n\n')

          elif (self.entry.get()=='sleeveless is allowed in utsav?'):
              self.text.insert(END, '\n'+ 'Bot: sleeveless is not allowed in the college premises. Only decent piece \n of clothing is encouraged. \n\n')

          elif (self.entry.get()=='sleeveless is allowed'):
              self.text.insert(END, '\n'+ 'Bot: sleeveless is not allowed in the college premises. Only decent piece \n of clothing is encouraged. \n\n')


          elif (self.entry.get()=='when is chocolate day'):
              self.text.insert(END, '\n'+ 'Bot: Chocolate day is on the 15th of March \n\n')

          elif (self.entry.get()=='WHEN IS CHOCOLATE DAY'):
              self.text.insert(END, '\n'+ 'Bot: Chocolate day is on the 15th of March \n\n')

          elif (self.entry.get()=='When is chocoalate day'):
              self.text.insert(END, '\n'+ 'Bot:  Chocolate day is on the 15th of March\n\n')

          elif (self.entry.get()=='chocolate day'):
              self.text.insert(END, '\n'+ 'Bot: Chocolate day is on the 15th of March \n\n')

          elif (self.entry.get()=='Chocolate'):
              self.text.insert(END, '\n'+ 'Bot: Chocolate day is on the 15th of March \n\n')


          elif (self.entry.get()=='what is umeed'):
              self.text.insert(END, '\n'+ 'Bot: Umeed is a five day camp orgainized by sort council in order to raise \n funds for Various Ngos.\n\n')

          elif (self.entry.get()=='What is Umeed'):
              self.text.insert(END, '\n'+ 'Bot: Umeed is a five day camp orgainized by sort council in order to raise \n funds for Various Ngos. \n\n')

          elif (self.entry.get()=='umeed'):
              self.text.insert(END, '\n'+ 'Bot: Umeed is a five day camp orgainized by sort council in order to raise \n funds for Various Ngos. \n\n')

          elif (self.entry.get()=='sort event umeed'):
              self.text.insert(END, '\n'+ 'Bot:  Umeed is a five day camp orgainized by sort council in order to raise \n funds for Various Ngos.\n\n')

          elif (self.entry.get()=='What is Umeed'):
              self.text.insert(END, '\n'+ 'Bot: Umeed is a five day camp orgainized by sort council in order to raise \n funds for Various Ngos. \n\n')

          elif (self.entry.get()=='how many Ngos does Umeed have'):
              self.text.insert(END, '\n'+ 'Bot: Umeed has products from about 5 Ngos \n\n')

          elif (self.entry.get()=='ngos of umeed'):
              self.text.insert(END, '\n'+ 'Bot:  Umeed has products from about 5 Ngos\n\n')
      


          elif (self.entry.get()=='what products are sold in umeed'):
              self.text.insert(END, '\n'+ 'Bot: The products in Umeed range from crafts like scrunchies, necklaces, diaries, \n folders,bags to edibles like chocolates, brownies etc. \n\n')

          elif (self.entry.get()=='products of umeed'):
              self.text.insert(END, '\n'+ 'Bot: The products in Umeed range from crafts like scrunchies, necklaces, diaries, \n folders,bags to edibles like chocolates, brownies etc. \n\n')

          elif (self.entry.get()=='umeed products'):
              self.text.insert(END, '\n'+ 'Bot:  The products in Umeed range from crafts like scrunchies, necklaces, diaries, \n folders,bags to edibles like chocolates, brownies etc.\n\n')

          elif (self.entry.get()=='what is sold in umeed'):
              self.text.insert(END, '\n'+ 'Bot:  The products in Umeed range from crafts like scrunchies, necklaces, diaries, \n folders,bags to edibles like chocolates, brownies etc.\n\n')

          elif (self.entry.get()=='what all products are sold in umeed?'):
              self.text.insert(END, '\n'+ 'Bot: The products in Umeed range from crafts like scrunchies, necklaces, diaries, \n folders,bags to edibles like chocolates, brownies etc. \n\n')


          elif (self.entry.get()=='who gets the money collected in umeed'):
              self.text.insert(END, '\n'+ 'Bot: The money collected in Umeed by selling products goes back to the respective \n NGO whose products are sold. \n\n')

          elif (self.entry.get()=='where does the umeed money go'):
              self.text.insert(END, '\n'+ 'Bot: The money collected in Umeed by selling products goes back to the respective \n NGO whose products are sold.  \n\n')

          elif (self.entry.get()=='umeed money'):
              self.text.insert(END, '\n'+ 'Bot: The money collected in Umeed by selling products goes back to the respective \n NGO whose products are sold.  \n\n')

          elif (self.entry.get()=='money collected in umeed'):
              self.text.insert(END, '\n'+ 'Bot:  The money collected in Umeed by selling products goes back to the respective \n NGO whose products are sold. \n\n')

          elif (self.entry.get()=='UMEED MONEY'):
              self.text.insert(END, '\n'+ 'Bot:  The money collected in Umeed by selling products goes back to the respective \n NGO whose products are sold. \n\n')

          elif (self.entry.get()=='where can we find the products of Umeed'):
              self.text.insert(END, '\n'+ 'Bot: You can find the products  on stalls set up in the reception, amphitheatre \n and 5th floor. \n\n')

          elif (self.entry.get()=='where are the products sold'):
              self.text.insert(END, '\n'+ 'Bot: You can find the products  on stalls set up in the reception, amphitheatre \n and 5th floor.  \n\n')

          elif (self.entry.get()=='how can i buy umeed products'):
              self.text.insert(END, '\n'+ 'Bot: You can find the products  on stalls set up in the reception, amphitheatre \n and 5th floor.  \n\n')

          elif (self.entry.get()=='i want to buy umeed products'):
              self.text.insert(END, '\n'+ 'Bot: You can find the products  on stalls set up in the reception, amphitheatre \n and 5th floor.  \n\n')

          elif (self.entry.get()=='umeed products to buy'):
              self.text.insert(END, '\n'+ 'Bot: You can find the products  on stalls set up in the reception, amphitheatre \n and 5th floor.  \n\n')

          elif (self.entry.get()=='can fe participate in Invictus'):
              self.text.insert(END, '\n'+ 'Bot: No, FEs cannot participate in Invictus \n\n')

          elif (self.entry.get()=='im an fe can i particopate in invictus'):
              self.text.insert(END, '\n'+ 'Bot: FEs cannot participate in Invictus, only students from SE, TE and BE can participate in Invictus \n\n')

          elif (self.entry.get()=='im an se can i participate in fe'):
              self.text.insert(END, '\n'+ 'Bot:  FEs cannot participate in Invictus, only students from SE, TE and BE can participate in Invictus\n\n')

          elif (self.entry.get()=='which year can participate in invictus'):
              self.text.insert(END, '\n'+ 'Bot: FEs cannot participate in Invictus, only students from SE, TE and BE can participate in Invictus \n\n')

          elif (self.entry.get()=='invictus'):
              self.text.insert(END, '\n'+ 'Bot: FEs cannot participate in Invictus, only students from SE, TE and BE can participate in Invictus \n\n')

          elif (self.entry.get()=='Can fe participate in praxis'):
              self.text.insert(END, '\n'+ 'Bot: Yes, FEs can participate in Praxis \n\n')


          elif (self.entry.get()=='what is the membership fees'):
              self.text.insert(END, '\n'+ 'Bot: The membership fees is Rs 650 for 3yrs \n\n')

          elif (self.entry.get()=='membership fees of iste'):
              self.text.insert(END, '\n'+ 'Bot: The membership fees is Rs 650 for 3yrs \n\n')

          elif (self.entry.get()=='membership fees'):
              self.text.insert(END, '\n'+ 'Bot:  The membership fees is Rs 650 for 3yrs\n\n')

          elif (self.entry.get()=='iste membership fees'):
              self.text.insert(END, '\n'+ 'Bot: The membership fees is Rs 650 for 3yrs \n\n')


          elif (self.entry.get()=='when is vcl '):
              self.text.insert(END, '\n'+ 'Bot: VCL will be starting from 7th October \n\n')
          
          elif (self.entry.get()=='WHEN IS VCL'):
              self.text.insert(END, '\n'+ 'Bot: VCL will be starting from 7th October\n\n')

          elif (self.entry.get()=='VCL is when'):
              self.text.insert(END, '\n'+ 'Bot:  VCL will be starting from 7th October\n\n')

          elif (self.entry.get()=='when is VCL'):
              self.text.insert(END, '\n'+ 'Bot: VCL will be starting from 7th October \n\n')

          elif (self.entry.get()=='When is sphurti'):
              self.text.insert(END, '\n'+ 'Bot:  Sphurti will be starting from 1st March to 14th March\n\n')

          elif (self.entry.get()=='WHEN IS SPHURTI'):
              self.text.insert(END, '\n'+ 'Bot:  Sphurti will be starting from 1st March to 14th March\n\n')

          elif (self.entry.get()=='sphurti'):
              self.text.insert(END, '\n'+ 'Bot: Sphurti will be starting from 1st March to 14th March \n\n')

          elif (self.entry.get()=='SPHURTI'):
              self.text.insert(END, '\n'+ 'Bot:  Sphurti will be starting from 1st March to 14th March\n\n')

          elif (self.entry.get()=='When is octaves'):
              self.text.insert(END, '\n'+ 'Bot:  Octaves is on the 13th and 14th of March\n\n')

          elif (self.entry.get()=='octaves'):
              self.text.insert(END, '\n'+ 'Bot: Octaves is on the 13th and 14th of March \n\n')

          elif (self.entry.get()=='OCTAVES'):
              self.text.insert(END, '\n'+ 'Bot: Octaves is on the 13th and 14th of March \n\n')

          elif (self.entry.get()=='WHEN IS OCTAVES'):
              self.text.insert(END, '\n'+ 'Bot: Octaves is on the 13th and 14th of March \n\n')

          elif (self.entry.get()=='When is Veslit week'):
              self.text.insert(END, '\n'+ 'Bot:  VESLit week will be from 1st March to 7th March 2023\n\n')

          elif (self.entry.get()=='Veslit week'):
              self.text.insert(END, '\n'+ 'Bot:  VESLit week will be from 1st March to 7th March 2023\n\n')

          elif (self.entry.get()=='VESLIT WEEK'):
              self.text.insert(END, '\n'+ 'Bot: VESLit week will be from 1st March to 7th March 2023 \n\n')

          elif (self.entry.get()=='Veslit week is when'):
              self.text.insert(END, '\n'+ 'Bot: VESLit week will be from 1st March to 7th March 2023 \n\n')

          elif (self.entry.get()=='How many Technical societies are there'):
              self.text.insert(END, '\n'+ 'Bot: There are 4 technical societies- ISTE, IEEE, CSI and ISA \n\n')

          elif (self.entry.get()=='technical societies'):
              self.text.insert(END, '\n'+ 'Bot: There are 4 technical societies- ISTE, IEEE, CSI and ISA \n\n')

          elif (self.entry.get()=='TECHNICAL SOCIETIES'):
              self.text.insert(END, '\n'+ 'Bot:  There are 4 technical societies- ISTE, IEEE, CSI and ISA\n\n')

          elif (self.entry.get()=='what is the mebership fees of csi'):
              self.text.insert(END, '\n'+ 'Bot:  The membership fees of CSI is Rs 650 for 1 year \n\n')

          elif (self.entry.get()=='what is the mebership fees of ieee'):
              self.text.insert(END, '\n'+ 'Bot: The membership fees is IEEE is Rs 350 \n\n')

          elif (self.entry.get()=='who is the secretary of cultural council'):
              self.text.insert(END, '\n'+ 'Bot: Sejal Bishoyi is the secretary of Cultural Council \n\n')

          elif (self.entry.get()=='who is the secretary of sports council'):
              self.text.insert(END, '\n'+ 'Bot: Prathamesh Gudame is the secretary of Sports Council \n\n')

          elif (self.entry.get()=='who is the secretary of veslit circle'):
              self.text.insert(END, '\n'+ 'Bot: Kaushal Jagasia is the secretary of VESLit Circle \n\n')

          elif (self.entry.get()=='who is the secretary of sort council'):
              self.text.insert(END, '\n'+ 'Bot: Sonia Deshmuksh is the secretary of SoRT Council \n\n')

          elif (self.entry.get()=='when is Prarambh'):
              self.text.insert(END, '\n'+ 'Bot:  Prarambh will be starting from 2nd December 2022\n\n')

          elif (self.entry.get()=='prarambh merch price '):
              self.text.insert(END, '\n'+ 'Bot: The price of prarambh merch is Rs 275 \n\n')

          elif (self.entry.get()=='can ses participate in prarambh'):
              self.text.insert(END, '\n'+ 'Bot: Prarambh is an event, solely for the FEs, so students from SE, TE and BE \ncannot participate in prarambh\n\n')

          elif (self.entry.get()=='1'):
              self.text.insert(END, '\n'+ 'Bot: Cultural Council: cultural.vesit@ves.ac.in \n\n')

          elif (self.entry.get()=='2'):
              self.text.insert(END, '\n'+ 'Bot: Sports Coucil: sport.vesit@ves.ac.in \n\n')

          elif (self.entry.get()=='3'):
              self.text.insert(END, '\n'+ 'Bot: SoRT Council: sort.vesit@ves.ac.in \n\n')

          elif (self.entry.get()=='4'):
              self.text.insert(END, '\n'+ 'Bot: Music Council: musiccouncil.vesit@ves.ac.in \n\n')

          elif (self.entry.get()=='5'):
              self.text.insert(END, '\n'+ 'Bot: VESLit Circle: veslit.circle@ves.ac.in \n\n')

          elif (self.entry.get()=='6'):
              self.text.insert(END, '\n'+ 'Bot: VESLang Circle: veslang.circle@ves.ac.in \n\n')

          elif (self.entry.get()=='7'):
              self.text.insert(END, '\n'+ 'Bot:  ISTE-VESIT: iste.vesit@ves.ac.in\n\n')

          elif (self.entry.get()=='8'):
              self.text.insert(END, '\n'+ 'Bot: IEEE-VESIT: ieee.vesit@ves.ac.in \n\n')

          elif (self.entry.get()=='9'):
              self.text.insert(END, '\n'+ 'Bot: ISA-VESIT: isa.vesit@ves.ac.in \n\n')

          elif (self.entry.get()=='10'):
              self.text.insert(END, '\n'+ 'Bot: CSI-VESIT: csi.vesit@ves.ac.in \n\n')

         
         
          else:
               self.text.insert(END, "\n\n"+ "Bot: Sorry, I didn't get it\n Please contact the respective council to know details about your queries\n to know their contact details choose\n 1. CULTURAL COUNCIL\n 2. SPORTS COUNCIL\n 3. SoRT COUNCIL\n 4. MUSIC COUNCIL\n 5. VESLit CIRCLE\n 6. VESLang CIRCLE\n 7. ISTE-VESIT\n 8. IEEE-VESIT\n 9. ISA-VESIT\n 10. CSI-VESIT\n\n")

          
          




     

if __name__ == '__main__':
     root=Tk()
     obj = ChatBot(root)
     root.mainloop()
