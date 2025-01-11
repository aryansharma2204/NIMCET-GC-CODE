import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

# Get the values from environment variables
CALENDAR_ID = os.getenv('CALENDAR_ID')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')

# Load credentials using the environment variable for the service account file
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/calendar']
)
service = build('calendar', 'v3', credentials=credentials)

# Define colors for each subject
subject_colors = {
    "Maths": "1",          # Light blue
    "Quant": "2",          # Light green
    "Computer Science": "4",  # Light red
    "English": "6",        # Purple
}

# Helper function to create events in Google Calendar
def create_event(subject, video_name, video_link, event_date, color_id=None):
    event = {
        'summary': f'{subject} - {video_name}',
        'description': f'Watch this video: {video_link}',
        'start': {'date': event_date},
        'end': {'date': event_date},
    }
    if color_id:
        event['colorId'] = color_id
    return service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

# Function to select a date using a calendar
def select_date():
    # Initialize selected_date as a Tkinter StringVar
    selected_date = tk.StringVar()

    def set_date():
        # Get the selected date from the calendar widget and close the window
        selected_date.set(calendar.get_date())
        calendar_window.destroy()

    calendar_window = tk.Toplevel(root)
    calendar_window.title("Select Date")
    calendar_window.geometry("350x400")

    frame = ttk.Frame(calendar_window, padding="10")
    frame.pack(fill="both", expand=True)

    calendar = Calendar(frame, date_pattern="yyyy-mm-dd", 
                        selectmode='day', font=("Helvetica", 14))
    calendar.pack(pady=10)

    select_button = ttk.Button(calendar_window, text="Select", command=set_date, 
                               style="TButton")
    select_button.pack(pady=10)

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12, "bold"), relief="flat", padding=10)
    style.map("TButton", background=[('active', '#45a049')])

    calendar_window.wait_window()
    return selected_date.get()

# Function to add videos for a single subject
def get_video_data(subject):
    video_data = []
    while True:
        video_name = simpledialog.askstring("Input", f"Enter video name for {subject} (or press 'Esc' to finish):")
        if not video_name:
            break
        video_link = simpledialog.askstring("Input", f"Enter link for '{video_name}':")
        if not video_link:
            messagebox.showerror("Error", "Video link cannot be empty. Please try again.")
            continue

        video_date = select_date()
        if not video_date:
            messagebox.showerror("Error", "Invalid date selection. Please try again.")
            continue

        video_data.append({"name": video_name, "link": video_link, "date": video_date})
    
    return video_data

# Function to select a subject by number
def select_subject():
    subject_list = list(subject_colors.keys())
    subject_input = simpledialog.askstring(
        "Subject Selection",
        "Choose the subject by entering the corresponding number:\n\n" + 
        "\n".join([f"{i+1}. {subject_list[i]}" for i in range(len(subject_list))]) + 
        "\n\nOr press 'Esc' to finish."
    )

    if not subject_input:
        return None

    try:
        subject_index = int(subject_input) - 1
        if subject_index < 0 or subject_index >= len(subject_list):
            raise ValueError
        return subject_list[subject_index]
    except (ValueError, IndexError):
        messagebox.showerror("Error", "Invalid selection. Please choose a number between 1 and 4.")
        return None

# Create Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Main loop for adding subjects and videos
subjects = {}
while True:
    subject = select_subject()
    if subject is None:
        break

    if subject not in subjects:
        subjects[subject] = []

    messagebox.showinfo("Info", f"Adding videos for {subject}.")
    subjects[subject].extend(get_video_data(subject))

# Schedule events with colors
for subject, videos in subjects.items():
    color_id = subject_colors.get(subject)
    for video in videos:
        create_event(subject, video["name"], video["link"], video["date"], color_id)

messagebox.showinfo("Success", "All-day events with colors have been added to your Google Calendar.")
root.quit()  # Close the Tkinter window
