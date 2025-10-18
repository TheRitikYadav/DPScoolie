import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time

# ------------------ AUTOMATION FUNCTION ------------------
def run_dps_automation(data, status_label):
    """Runs DPS Selenium automation using data from GUI fields."""
    try:
        status_label.config(text="🚀 Starting automation...", fg="blue")

        URL = "https://www.txdpsscheduler.com/"
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        wait = WebDriverWait(driver, 25)

        def safe_click(xpath, label):
            try:
                el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                time.sleep(1.2)
                driver.execute_script("arguments[0].click();", el)
                print(f"✅ Clicked {label}")
                time.sleep(2)
            except Exception as e:
                print(f"⚠️ Failed to click {label}: {e}")

        # ------------------ XPATHS ------------------
        XPATH_LANG_BTN   = "/html/body/div/div[2]/div/div/div[2]/button[1]/span"
        XPATH_FIRST_NAME = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[2]/div/div[1]/div/input"
        XPATH_LAST_NAME  = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[3]/div/div[1]/div/input"
        XPATH_DOB        = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[4]/div/div[1]/div[1]/input"
        XPATH_SSN4       = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[5]/div/div[1]/div[1]/input"
        XPATH_FINAL_BTN  = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[4]"
        XPATH_SECOND_BTN = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/div[3]/div/button/span"
        XPATH_THIRD_BTN  = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/main/div/div/div[1]/div[1]/button"
        XPATH_EMAIL1     = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[1]/div/div[5]/div/div/div/div[1]/div/input"
        XPATH_EMAIL2     = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[1]/div/div[6]/div/div/div/div[1]/div/input"
        XPATH_ZIP        = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div[1]/input"
        XPATH_CELLPHONE  = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[1]/div/div[4]/div[2]/div/div/div[1]/div/input"
        XPATH_CHECKBOX   = "/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[1]/div/div[7]/div/div[1]/div/div[1]/div/div"

        # ------------------ AUTOMATION ------------------
        driver.get(URL)
        safe_click(XPATH_LANG_BTN, "English button")

        wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_FIRST_NAME))).send_keys(data["first_name"])
        wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_LAST_NAME))).send_keys(data["last_name"])
        wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_DOB))).send_keys(data["dob"])
        wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_SSN4))).send_keys(data["ssn4"])
        status_label.config(text="✅ Basic info entered.", fg="green")

        safe_click(XPATH_FINAL_BTN, "Log On button")
        safe_click(XPATH_SECOND_BTN, "New Appointment button")
        safe_click(XPATH_THIRD_BTN, "Apply for Texas button")

        email1 = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_EMAIL1)))
        email2 = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_EMAIL2)))
        email1.clear(); email1.send_keys(data["email"])
        email2.clear(); email2.send_keys(data["email"])
        print(f"✅ Entered email {data['email']}")

        zip_field = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_ZIP)))
        cell_field = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_CELLPHONE)))
        zip_field.clear(); zip_field.send_keys(data["zip"])
        cell_field.clear(); cell_field.send_keys(data["cell"])
        safe_click(XPATH_CHECKBOX, "Confirmation checkbox")

        status_label.config(text="🎯 Automation completed! Browser will stay open.", fg="green")

    except Exception as e:
        status_label.config(text=f"⚠️ Error: {e}", fg="red")

# ------------------ TKINTER GUI ------------------
def start_automation():
    """Collects form data and starts automation thread."""
    user_data = {
        "first_name": entry_fname.get(),
        "last_name": entry_lname.get(),
        "dob": entry_dob.get(),
        "ssn4": entry_ssn.get(),
        "email": entry_email.get(),
        "zip": entry_zip.get(),
        "cell": entry_phone.get()
    }

    if not all(user_data.values()):
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
        return

    threading.Thread(target=run_dps_automation, args=(user_data, status_label), daemon=True).start()

# --- GUI Layout ---
root = tk.Tk()
root.title("DPS Coolie - DPS Appointment Auto-Fill")
root.geometry("500x500")
root.resizable(True, True)

tk.Label(root, text="DPS Appointment Auto-Fill", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

labels = ["First Name", "Last Name", "Date of Birth (mm/dd/yyyy)",
          "Last 4 of SSN", "Email", "ZIP Code", "Phone Number"]
entries = []

for lbl in labels:
    tk.Label(frame, text=lbl).pack()
    e = tk.Entry(frame, width=35)
    e.pack(pady=2)
    entries.append(e)

entry_fname, entry_lname, entry_dob, entry_ssn, entry_email, entry_zip, entry_phone = entries

tk.Button(root, text="Start Automation", font=("Arial", 12, "bold"),
          bg="#0078D7", fg="white", command=start_automation).pack(pady=20)

status_label = tk.Label(root, text="Status: Waiting to start...", fg="gray")
status_label.pack(pady=15)

root.mainloop()
