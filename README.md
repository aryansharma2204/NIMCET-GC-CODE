# Google Calendar Scheduler with Tkinter UI

Effortlessly manage your study schedule with this interactive tool. Designed with students in mind, it enables seamless task scheduling directly to Google Calendar via a user-friendly graphical interface.

---

## 🌟 Features

- **Subject-Based Scheduling**:
  - Add tasks for predefined subjects: `Maths`, `Quant`, `Computer Science`, and `English`.
- **Graphical Date Picker**:
  - Use an intuitive calendar widget powered by `tkcalendar`.
- **Color-Coded Events**:
  - Automatically assign unique colors to events for each subject in Google Calendar.
- **Flexible Exit**:
  - Exit the task creation process anytime using the `Escape` key.
- **Environment File**:
  - Store sensitive data securely with `.env` support.
- **macOS Automation**:
  - Automate script execution using Automator.

---

## 🔧 Prerequisites

### 1. **Python Installation**
Ensure Python 3 is installed:
```bash
python3 --version
```
If not installed, download Python 3 from [python.org](https://www.python.org/downloads/).

### 2. **Google Calendar API Setup**

1. **Enable API**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google Calendar API for your project.

2. **Create Service Account**:
   - Navigate to **IAM & Admin > Service Accounts**.
   - Create a service account and download the JSON key file.
   - Rename the file (e.g., `service_account.json`) for clarity and save it to your project directory.

3. **Share Calendar**:
   - Share your Google Calendar with the service account email (e.g., `your-service-account@project-id.iam.gserviceaccount.com`) with **Editor** permissions.

4. **Save Credentials**:
   - Place the JSON key file (e.g., `service_account.json`) in the project directory.
   - Set the `SERVICE_ACCOUNT_FILE` variable in your script to point to this file.

### Script Code Snippet

Ensure your Python script includes the following to authenticate with the service account:

```python
from google.oauth2 import service_account

# Path to your service account file
SERVICE_ACCOUNT_FILE = "service_account.json"

# Google Calendar API Scopes
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Create credentials object
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
```

---

## 🚀 Installation

### 1. **Clone the Repository**
```bash
git clone https://github.com/aryansharma2204/NIMCET-GC-CODE.git
cd NIMCET-GC-CODE
```

### 2. **Install Dependencies**
Install the necessary Python libraries:
```bash
pip3 install -r requirements.txt
```

#### Packages in `requirements.txt`:
- `google-api-python-client`
- `google-auth`
- `google-auth-oauthlib`
- `tkcalendar`
- `dotenv`

### 3. **Run the Script**
Test the script to verify functionality:
```bash
python3 google_calendar_schedule.py
```

---

## 💻 Usage

### **Running the Script**

1. **Start the Program**:
   ```bash
   python3 google_calendar_schedule.py
   ```

2. **Add Event Details**:
   - Enter the subject name (e.g., Maths, Quant, etc.).
   - Add video/task names, links, and pick a date using the calendar widget.
   - Press `Escape` to exit a subject or the entire program.

3. **Check Your Calendar**:
   - Events will appear in your Google Calendar, color-coded by subject.

---

## 🛠 Automating Script Execution on macOS

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

## 🐧 Notes for Linux Users

Linux users can run the script directly from the terminal:
```bash
python3 google_calendar_schedule.py
```
Ensure all required Python libraries are installed.

---

## 🔄 Troubleshooting

### **Common Issues**

#### 1. **Module Not Found Error**
Ensure all required packages are installed:
```bash
pip3 install -r requirements.txt
```

#### 2. **Credential Errors**
- Verify the `service_account.json` file is in the same directory as the script.
- Ensure your Google Calendar is shared with the service account email.

#### 3. **Mac Automation Issues**
- Use `which python3` in the terminal to find your Python path.
- Verify the Automator app's script points to the correct Python path.

---

## 🤝 Contributing

We welcome contributions! Feel free to submit issues or pull requests to improve this project.

---

## 📧 Contact

For any questions or feedback, reach out to: [aryansde2204@gmail.com].
