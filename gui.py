# gui.py
import tkinter as tk
from function import index

class MyGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sentiment analyser")
        self.master.geometry("800x800")
        self.label = tk.Label(self.master, text="Enter any Sentence:" ,width=30 , height= 3,)
        self.label.pack()

        self.entry1 = tk.Entry(self.master,width=50)
        self.entry1.pack()

         

        self.add_button = tk.Button(self.master, text="click", command=self.index)
        self.add_button.pack()

         # Create a label to display the output
        self.output_label = tk.Label(self.master, text="")
        self.output_label.pack(pady=10)
        self.output_label1 = tk.Label(self.master, text="")
        self.output_label1.pack(pady=10)

    def update_color(self,sentiment_score):
        if sentiment_score > 0:
            self.output_label1.config(text="  positive Sentence ")
            self.master.configure(bg="lightgreen")
            
        elif sentiment_score < 0:
            self.output_label1.config(text="Negative Sentaince")
            self.master.configure(bg="red")
        else:
            self.output_label1.config(text="Neutral Sentence")
            self.master.configure(bg="yellow")

    def index(self):
        Uinput = self.entry1.get()
        result = index(Uinput)
        self.update_color(result)
        self.output_label.config(text="Sentiment :" + str(result)+"%")

        print("jk" , result)
    
     

if __name__ == "__main__":
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()
