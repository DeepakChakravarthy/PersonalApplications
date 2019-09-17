import tkinter as tk

def dc():
    from tkinter import messagebox
    import time
    current_time = time.strftime("%H:%M")
    messagebox.showinfo("Sticky Note","Ready to Create the Note")
    time.sleep(2)
    print("--------------NOTES-------------------")
    notes = input("#####ENTER THE NOTE------>:")
    note = ("*%s")%notes
    time.sleep(1)
    main = tk.Tk()
    main.title("STICKY NOTE")
    main.geometry("300x300")
    tk.Label(main,text=current_time).pack()
    tk.Label(main,text=note).pack()
    main.mainloop()
    main.withdraw()
dc()

    
    
