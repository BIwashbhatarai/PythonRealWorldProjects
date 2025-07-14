from tkinter import *           # Import everything from tkinter for GUI
import speedtest                # Import speedtest module to check internet speed
import threading                # Import threading to run speed test in background

def speedTest():
    # This function runs speed test in a separate thread to avoid GUI freezing
    def run():
        print("Starting speed test...")  # Print to console when test starts
        st = speedtest.Speedtest()       # Create Speedtest object
        st.get_servers()                 # Get list of servers (optional)
        st.get_best_server()             # Select best server based on latency
        # Calculate download speed in Mbps (megabits per second)
        down = str(round(st.download() / (10**6), 3))
        # Calculate upload speed in Mbps
        up = str(round(st.upload() / (10**6), 3))
        # Update download speed label on GUI
        lab_down.config(text=down + " Mbps")
        # Update upload speed label on GUI
        lab_up.config(text=up + " Mbps")
    # Start the speed test function in a new thread so GUI stays responsive
    threading.Thread(target=run).start()


window = Tk()                     # Create main Tkinter window
window.title("Internet Speed")   # Set window title
window.geometry("500x630")       # Set window size
window.config(bg="#1e1e2f")      # Set background color (dark blue/grey)

# Create and place the title label at top
label = Label(window, text="Internet Speed Test", font=("Segoe UI", 20, "bold"),
              bg="#1e1e2f", fg="#00FFFF")
label.place(x=60, y=50, height=50, width=385)

# Create and place the "Download Speed" heading label
label = Label(window, text="Download Speed", font=("Segoe UI", 30, "bold"),
              bg="#1e1e2f", fg="white")
label.place(x=60, y=130, height=50, width=385)

# Create and place the label to show download speed value
lab_down = Label(window, text="00 Mbps", font=("Arial", 30, "bold"),
                 bg="#1e1e2f", fg="#39FF14")
lab_down.place(x=60, y=200, height=50, width=385)

# Create and place the "Upload Speed" heading label
label = Label(window, text="Upload Speed", font=("Segoe UI", 30, "bold"),
              bg="#1e1e2f", fg="white")
label.place(x=60, y=290, height=50, width=385)

# Create and place the label to show upload speed value
lab_up = Label(window, text="00 Mbps", font=("Arial", 30, "bold"),
               bg="#1e1e2f", fg="#FF1493")
lab_up.place(x=60, y=360, height=50, width=385)

# Create and place the button to start speed test
button = Button(window, text="Check Speed", font=("Segoe UI", 16, "bold"),
                bg="#F0F0F0", fg="#1e1e2f", activebackground="#00FFFF",
                activeforeground="#1e1e2f", relief=RIDGE, command=speedTest)
button.place(x=60, y=460, height=50, width=385)

window.mainloop()  # Start the Tkinter event loop to run the GUI
