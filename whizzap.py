import pandas as pd
import pywhatkit as kit
import faiss
import numpy as np
import os
from difflib import get_close_matches


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 🔧 FAISS Index Builder
def build_faiss_index(contact_list):
    vector_db = faiss.IndexFlatL2(768)
    embeddings = np.random.rand(len(contact_list), 768).astype("float32")
    vector_db.add(embeddings)
    return vector_db, embeddings

# Find matching contact(s)
def find_contacts(name, contact_list, embeddings, vector_db):
    name_lower = name.lower()
    matches = [i for i, n in enumerate(contact_list) if name_lower == n.lower()]

    if not matches:
        # Try fuzzy matching if exact match fails
        fuzzy_matches = get_close_matches(name_lower, [n.lower() for n in contact_list], cutoff=0.7)
        matches = [i for i, n in enumerate(contact_list) if n.lower() in fuzzy_matches]

    if matches:
        numbers_found = [numbers[i] for i in matches]
        return numbers_found
    else:
        print(f"Error: '{name}' not found or matched in contact list.")
        return []

# Send message to multiple recipients
def send_whatsapp_message(phone_numbers, message):
    for phone_number in phone_numbers:
        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            print(f"Message sent to {phone_number}")
        except Exception as e:
            print(f"Failed to send message to {phone_number}: {e}")

# Extract role and message from user input
def extract_position_and_clean_message(prompt, contact_list):
    for position in contact_list:
        if position.lower() in prompt.lower():
            message = prompt.split(position, 1)[-1].strip()
            message = (
                message.replace("Ask the", "")
                .replace("to", "")
                .replace("send", "")
                .strip()
                .capitalize()
            )
            return position, message
    print("Error: Position not found in the prompt.")
    return None, None

# Load Excel contacts
try:
    df = pd.read_excel("contacts.xlsx", dtype={"Phone Number": str})
except FileNotFoundError:
    print("Error: 'contacts.xlsx' file not found.")
    exit()

df["Phone Number"] = df["Phone Number"].apply(
    lambda x: f"+91{x}" if not x.startswith("+") and len(x) == 10 else x
)

contact_list = df["Position"].tolist()
numbers = df["Phone Number"].tolist()

vector_db, embeddings = build_faiss_index(contact_list)

# User Input
prompt = input("Enter the prompt: ")

# Extract role & message content
position, message_content = extract_position_and_clean_message(prompt, contact_list)

if position and message_content:
    message_to_send = (
        f"Respected {position},\n\n{message_content}.\n\nThank you.\n\nBest regards!"
    )
    print("Generated message:\n", message_to_send)

    matching_numbers = find_contacts(position, contact_list, embeddings, vector_db)

    if matching_numbers:
        send_whatsapp_message(matching_numbers, message_to_send)
