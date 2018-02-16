RFID_code = str(input("Enter the code: "))
# print(RFID_code)

event_ids = {
  '1': "Code N Code",
  '2': "Ensemble",
  '3': "Model Presentation",
  '4': "Circuitry",
  '5': "Trouble Shooting",
  '6': "Technical Quiz",
  '7': "Photography and Short films",
  '8': "Paper Presentation"
}

first_name = str(input("Enter first name: "))
last_name = str(input("Enter last name: "))

college = str(input("Enter college: "))
phone_number = str(input("Enter phone number: "))
email_id = str(input("Enter email: "))

def enter_events():
  print("-------------------------------")
  print("Events:")
  print("-------------------------------")
  print("[1] Code N Code.")
  print("[2] Ensemble.")
  print("[3] Model Presentation.")
  print("[4] Circuitry.")
  print("[5] Trouble Shooting.")
  print("[6] Technical Quiz.")
  print("[7] Photography and Short films.")
  print("[8] Paper Presentation.")
  print("--------------------------------")
  events = str(input("Enter any three event options: "))
  events = list(events.split())
  
  print("The events interested are: ")
  for event in events:
    print(event_ids[event])
    
# if __name__ == "__main__":
enter_events()
