import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk  # Attractive theme library

# Predefined list of registration numbers
valid_reg_numbers = {101, 102, 103, 104, 105, 106, 107, 108}
used_reg_numbers = set()  # Store used registration numbers

# Candidates (IPL Teams)
teams = {
    "CSK (Chennai Super Kings)": 0,
    "MI (Mumbai Indians)": 0,
    "RCB (Royal Challengers Bangalore)": 0,
    "KKR (Kolkata Knight Riders)": 0,
    "LSG (Lucknow Super Giants)": 0
}

def vote():
    reg_no = reg_entry.get()
    
    # Validate registration number
    if not reg_no.isdigit():
        messagebox.showerror("Invalid Input", "Registration number must be numeric!")
        return
    
    reg_no = int(reg_no)
    
    if reg_no not in valid_reg_numbers:
        messagebox.showerror("Invalid Registration", "This registration number is not allowed!")
        return
    
    if reg_no in used_reg_numbers:
        messagebox.showwarning("Already Voted", "This registration number has already voted!")
        return

    selected_team = team_var.get()
    if not selected_team:
        messagebox.showerror("No Selection", "Please select a team before voting!")
        return

    # Record vote
    teams[selected_team] += 1
    used_reg_numbers.add(reg_no)
    messagebox.showinfo("Vote Recorded", f"Your vote for {selected_team} has been recorded!")

    # Check if all votes are done
    if len(used_reg_numbers) == len(valid_reg_numbers):
        release_results()

def release_results():
    result_text = "\n".join([f"{name}: {votes} votes" for name, votes in teams.items()])
    messagebox.showinfo("Final Voting Results", result_text)
    root.quit()  # Close the application automatically

# GUI Setup with ttkbootstrap
root = ttk.Window(themename="superhero")  # Cool theme
root.title("IPL Team Voting System")
root.geometry("400x450")

# Heading
title_label = ttk.Label(root, text="Vote for Your Favorite IPL Team!", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Registration Number Input
ttk.Label(root, text="Enter Registration No:", font=("Arial", 12)).pack(pady=5)
reg_entry = ttk.Entry(root, font=("Arial", 12), bootstyle="info")
reg_entry.pack(pady=5)

# Team Selection
ttk.Label(root, text="Select Your Team:", font=("Arial", 12)).pack(pady=5)
team_var = tk.StringVar()

for team in teams.keys():
    ttk.Radiobutton(root, text=team, variable=team_var, value=team, bootstyle="success").pack(anchor="w", padx=20)

# Vote Button
vote_btn = ttk.Button(root, text="Vote", bootstyle="primary", command=vote)
vote_btn.pack(pady=15)

root.mainloop()
