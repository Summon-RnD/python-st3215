from st3215 import ST3215

servo = ST3215('/dev/serial/by-id/usb-1a86_USB_Single_Serial_5AE6058210-if00')
ids = servo.ListServos()
print(ids)
current_id = 1
new_id = 2

# 1. Unlock EEPROM so writes are saved after power loss
#servo.UnLockEprom(current_id)

# 2. Change the ID
#result = servo.ChangeId(1, new_id)

if result is None:
    print(f"ID changed successfully to {new_id}")
else:
    print(f"Error: {result}")

# 3. Lock EEPROM again to protect saved values
#servo.LockEprom(new_id)  # Use the NEW id now!
