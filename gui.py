import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, expand=True)

label = customtkinter.CTkLabel(master=frame, text="Supplement Tracker")
label.pack(pady=12, padx=10)

root.mainloop()