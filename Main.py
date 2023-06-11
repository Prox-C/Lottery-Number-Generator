import tkinter as tk
import customtkinter as ctk
import random

# Function Declaration
def main():
	mode = mode_selector.get()
	
	generated_nums = []
	nums = ""
	
	if mode == "EZ2":
		for i in range(2):
			generated_nums.append(random.randint(0,31))
	elif mode == "Swertres":
		for i in range(3):
			generated_nums.append(random.randint(0,9))
	elif mode == "Megalotto":
		for i in range(6):
			generated_nums.append(random.randint(0,45))
	elif mode == "Superlotto":
		for i in range(6):
			generated_nums.append(random.randint(0,49))
	elif mode == "Grandlotto":
		for i in range(6):
			generated_nums.append(random.randint(0,55))
			
	for i in range(len(generated_nums)):
		nums += str(generated_nums[i]) + "  "
	
	display_text_var.set(nums)
	
	return

# Root Config
root = ctk.CTk()
root.geometry("800x500")
root.title("Lotto Number Generator")
root.resizable(False, False)

# Top Frame Config
display_frame = ctk.CTkFrame(
    master = root,
    width = 800,
    height = 250,
    fg_color = "#0078D7",
    corner_radius = 0
)
display_frame.pack()
display_frame.grid_columnconfigure((0,1,2,3), weight=1, minsize=200)
display_frame.grid_rowconfigure(0, weight=1, minsize=250)

# Bottom Frame Config
button_frame = ctk.CTkFrame(
    master = root,
    width = 800,
    height = 250,
    fg_color = "#FFF",
    corner_radius = 0
)
button_frame.pack()
button_frame.grid_columnconfigure((0,1,2,3), weight=1, minsize=200)
button_frame.grid_rowconfigure(0, weight=1, minsize=250)

# Top Frame Widgets
mode_selector = ctk.CTkOptionMenu(
    master = display_frame,
    width = 150,
    height = 25,
    values = ["EZ2","Swertres", "Megalotto", "Superlotto", "Grandlotto"],
    font = ("Futura", 18),
    dropdown_font = ("Futura", 14),
    dropdown_fg_color = "#FFF",
    dropdown_text_color	= "#0078D7",
    dropdown_hover_color = "#C7E1FF",
    button_hover_color = "#001D85"
)
mode_selector.grid(row=0, column=0, columnspan=2, sticky="nw", padx=15, pady=15)

nums = ":)"
display_text_var = tk.StringVar(value=nums)
display_text = ctk.CTkLabel(
    master = display_frame,
    width = 800,
    height = 84,
    textvariable = display_text_var,
    font = ("Futura", 40, "bold"),
    text_color = "#FFF"
)
display_text.grid(row=0, column=0, columnspan=4)

# Bottom Frame Widgets
main_button = ctk.CTkButton(
    master = button_frame,
    width = 400,
    height = 84,
    corner_radius = 50,
    fg_color = "#0078D7",
    hover_color = "#001D85",
    text = "Generate",
    font = ("Futura", 40),
    text_color = "#FFF",
    command = lambda: main()
)
main_button.grid(row=0, column=1, columnspan=2)

# Run
root.mainloop()
