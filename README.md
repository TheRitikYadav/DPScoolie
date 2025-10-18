# DPS Coolie – Automated DPS Appointment Form Filler

## Overview
`DPScoolie.py` is a **Tkinter-based GUI automation tool** that simplifies and accelerates the process of filling out the **Texas Department of Public Safety (DPS) appointment scheduling form**.  
It uses **Selenium WebDriver** to interact with the DPS website automatically after the user provides their personal information through a simple GUI.

---

## Key Features
- **User-Friendly GUI:** Built using `tkinter` for easy data entry.  
- **Automated Form Filling:** Uses `selenium` to open the DPS website and automatically fill required fields such as name, date of birth, SSN, email, ZIP, and phone number.  
- **Threaded Execution:** Runs automation in a separate thread to prevent GUI freezing.  
- **Error Handling:** Displays warnings for missing fields and updates the status label in real-time.  
- **ChromeDriver Auto-Management:** Uses `webdriver_manager` to install and manage ChromeDriver automatically.

---

## Requirements

### Python Libraries
Install the dependencies using:
```bash
pip install selenium webdriver-manager
```

The script also uses the built-in `tkinter`, `threading`, and `time` modules (no installation needed).

### Software Requirements
- Python 3.8 or newer  
- Google Chrome browser  

---

## How It Works

### 1. GUI Data Input
Users are prompted to enter:
- First Name  
- Last Name  
- Date of Birth (mm/dd/yyyy)  
- Last 4 digits of SSN  
- Email Address  
- ZIP Code  
- Phone Number  

Once all fields are filled, clicking the **“Start Automation”** button begins the process.

---

### 2. Selenium Automation
The function `run_dps_automation(data, status_label)` performs the following steps:

1. Launches Chrome and navigates to [txdpsscheduler.com](https://www.txdpsscheduler.com/).  
2. Clicks the **English language** button.  
3. Fills in the personal details using the provided XPaths.  
4. Clicks through multiple form stages:
   - “Log On”
   - “New Appointment”
   - “Apply for Texas”  
5. Enters email, ZIP, and phone information.  
6. Checks the confirmation checkbox.  
7. Leaves the browser open after automation completion.

---

### 3. Status Updates
The GUI displays real-time progress messages, such as:
- 🚀 Starting automation...
- ✅ Basic info entered.
- 🎯 Automation completed! Browser will stay open.
- ⚠️ Error messages in red with error details.

---

## Code Structure

| Section | Description |
|----------|--------------|
| **Imports** | Required modules (`tkinter`, `selenium`, `threading`, etc.) |
| **run_dps_automation()** | Main automation logic using Selenium |
| **start_automation()** | Collects user input and starts automation in a thread |
| **Tkinter GUI Setup** | Creates the window, input fields, start button, and status label |

---

## Usage
1. Run the script:
   ```bash
   python DPScoolie.py
   ```
2. Fill in your details in the GUI.  
3. Click **“Start Automation”**.  
4. The script will open Chrome, fill the form, and leave the browser open for any manual steps (e.g., CAPTCHA or confirmation).

---

## Legal and Ethical Disclaimer
This tool is **for educational and personal productivity purposes only**.  
Automating web interactions may **violate terms of service** of some websites, including government portals.  
Users are responsible for ensuring their actions comply with all applicable **laws and policies**.  
Manual confirmation or CAPTCHA solving may still be required for legal compliance.

---

## Future Enhancements
- CAPTCHA detection pause with prompt.
- Secure database or Excel integration for bulk user data.
- GUI design improvements (theme, input validation).
- Auto-screenshot capture for verification.
