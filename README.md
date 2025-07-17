# WhizZap – Role-Based WhatsApp Automation Bot with Natural Language Input

WhizZap is an intelligent, role-based WhatsApp automation bot powered by Python. Designed for admin teams, educational institutions, and HR departments, WhizZap interprets natural language instructions and automatically sends messages to the appropriate person on WhatsApp, using contact details from an Excel sheet.


## Features

* **Smart Role Recognition**: Understands roles like Principal, Vice-Principal, Assistant Professor, etc., directly from your natural language command.
* **Fuzzy Matching Engine**: Corrects minor typos and variations using Python’s intelligent string matching.
* **WhatsApp Message Automation**: Sends WhatsApp messages instantly via pywhatkit without manual intervention.
* **Excel Integration**: Reads staff details (Name, Phone Number, Role) directly from .xlsx files using pandas and openpyxl.
* **FAISS Vector Search**: Provides highly scalable and fast similarity search for roles using embeddings.
* **Modular Python Codebase**: Clean, customizable structure for quick integration into existing systems.


## Getting Started

```bash
pip install -r requirements.txt

python main.py

Enter prompt: (eg.,Ask the Assistant Professor to arrange the class committee meeting at the department)

WhizZap will process the input, find the correct number, and send the message.
```


## Notes
* Ensure your WhatsApp Web is logged in and open in your default browser.
* Message sending might take a few seconds (uses pywhatkit delay).
* The phone number format should include country code (e.g., +91).




