# Google Calendar Scheduler with Tkinter UI

This project allows you to schedule tasks and events directly to your Google Calendar with a user-friendly graphical interface. You can add tasks for various subjects, select dates using a calendar widget, and assign colors to events based on the subject. It's optimized for macOS and Linux users, with steps to automate execution on macOS.

---

## Features

- **Subject-Based Scheduling**: Add tasks for predefined subjects: Maths, Quant, Computer Science, and English.
- **Graphical Date Picker**: Use a graphical calendar widget (via `tkcalendar`) to select event dates easily.
- **Color-Coded Events**: Automatically assign unique colors to events for each subject in Google Calendar.
- **Flexible Exit**: Exit the task creation process at any time using the `Escape` key.
- **Automation**: Automate script execution on macOS using Automator.

---

## Prerequisites

### 1. **Python Installation**
Ensure Python 3 is installed on your system.

Check your Python version:
```bash
python3 --version
```

If not installed, download Python 3 from [python.org](https://www.python.org/downloads/).

### 2. **Google Calendar API Setup**

1. **Enable API**: Go to the [Google Cloud Console](https://console.cloud.google.com/) and enable the Google Calendar API for your project.
2. **Create Service Account**:
   - Navigate to **IAM & Admin > Service Accounts**.
   - Create a new service account and download the JSON key file.
3. **Share Calendar**:
   - Share your Google Calendar with the service account email (e.g., `your-service-account@project-id.iam.gserviceaccount.com`) with **Editor** permissions.
4. **Save Credentials**: Save the JSON key file (e.g., `credentials.json`) in the project directory.

---

## Installation

### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/google-calendar-scheduler.git
cd google-calendar-scheduler
```

### 2. **Install Dependencies**
Install the necessary Python libraries using `pip`:
```bash
pip3 install -r requirements.txt
```

#### Packages in `requirements.txt`:
- `google-api-python-client`
- `google-auth`
- `google-auth-oauthlib`
- `tkcalendar`
- `tkinter` (pre-installed with Python for most systems)

### 3. **Run the Script**
Test the script to verify functionality:
```bash
python3 google_calender_schedule.py
```

---

## Usage

### **Running the Script**

1. **Start the Program**:
   ```bash
   python3 google_calender_schedule.py
   ```

2. **Add Event Details**:
   - Enter the subject name (e.g., Maths, Quant, etc.).
   - Add video/task names, links, and pick a date using the calendar widget.
   - Press `Escape` to exit a subject or the entire program.

3. **Check Your Calendar**:
   Events will appear in your Google Calendar, color-coded by subject.

---

## Automating Script Execution on macOS

### 1. **Create an Automator App**

1. Open **Automator**.
2. Create a new document and select **Application**.
3. Drag **Run Shell Script** into the workflow area.
4. Set the shell script to:
   ```bash
   /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 /path/to/google_calender_schedule.py
   ```
5. Save the Automator app (e.g., `GoogleCalendarScheduler.app`).

### 2. **Run the Automator App**
Double-click the app to execute the script easily.

---

## Notes for Linux Users
Linux users can run the script directly from the terminal:
```bash
python3 google_calender_schedule.py
```
Ensure all required Python libraries are installed.

---

## Troubleshooting

### **Common Issues**

#### 1. **Module Not Found Error**
Ensure all required packages are installed:
```bash
pip3 install -r requirements.txt
```

#### 2. **Credential Errors**
- Verify the `credentials.json` file is in the same directory as the script.
- Ensure your Google Calendar is shared with the service account email.

#### 3. **Mac Automation Issues**
- Use `which python3` in the terminal to find your Python path.
- Verify the Automator app's script points to the correct Python path.

---

## Contributing

We welcome contributions! Feel free to submit issues or pull requests to improve this project.

---

## Contact

For any questions or feedback, reach out to [aryansde2204@gmail.com].
