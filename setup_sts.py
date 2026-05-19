from pypot.feetech import FeetechSTS3215IO
import time

gripper = FeetechSTS3215IO(port="/dev/serial/by-id/usb-1a86_USB_Single_Serial_5AE6058210-if00", baudrate=1000000)

ID = 1

gripper.enable_torque([ID])
time.sleep(0.5)
gripper.disable_torque([ID])
time.sleep(0.5)

pos_open = gripper.get_present_position([ID])
time.sleep(0.5)
print(pos_open)
pos_close = gripper.get_present_position([ID])
time.sleep(0.5)

gripper.set_lock({ID: 0})
time.sleep(0.5)
gripper.set_acceleration({ID: 50})
time.sleep(0.5)

gripper.set_min_angle_limit({ID: -180})
time.sleep(0.5)
gripper.set_max_angle_limit({ID: 180})
time.sleep(0.5)

gripper.set_torque_limit({ID: 1000})
time.sleep(0.5)

gripper.set_overload_torque({ID: 40})
time.sleep(0.5)

gripper.set_protective_torque({ID: 5})
time.sleep(0.5)

gripper.set_protection_time({ID: 7})
time.sleep(0.5)

gripper.set_lock({ID: 1})
time.sleep(0.5)

def open():
    gripper.enable_torque([ID])
    gripper.set_goal_position({ID: -8})

def close():
    gripper.enable_torque([ID])
    gripper.set_goal_position({ID: -180})
    
def seta(ang):
    gripper.enable_torque([ID])
    gripper.set_goal_position({ID: ang})

# open()
# time.sleep(1.0)
# close()
# time.sleep(1.0)
while True:
    x = int(input("Open or Close (1 or 0):"))
    seta(x)
    #if x:
     #   open()
    #else:
     #   close()


