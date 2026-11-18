print("=== ANDROMEYDA AI DIGITAL TWIN: BRAKE DISC TO ROBOT BRIDGE ===")

brake_temp = float(input("Enter max brake temp from virtual lap in °C (e.g. 845): "))
disc_thickness = float(input("Enter current brake disc thickness in mm (e.g.32.0): ")) 
cooling_vents = int(input("Enter current number of cooling vents (e.g. 36): "))

new_thickness = disc_thickness
new_vents = cooling_vents
robot_action = "NO_MODIFICATION_NEEDED"

print("\n--- [STAGE 1] AI THERMAL & STRUCTURAL ANALYSIS ---")

if brake_temp > 800:
    print(f"[!] CRITICAL FADE DETECTED ({brake_temp}°C > 800°C)")
    print("-> [AI solution]: increasing disc thickness & adding vents to prevent cracking.")
    new_thickness = round(disc_thickness + 2.5, 1)
    new_vents = cooling_vents + 12
    robot_action = "FABRICATE_REINFORCED_DISC"
elif brake_temp > 640:
    print(f"[!] HIGH THERMAL LOAD ({brake_temp}°C).")
    print("-> [AI solution]: optimizing cooling airflow by adding extra ventilation chaneels.")
    new_vents = cooling_vents + 6
    robot_action = "DRILL_EXTRA_VENTS"

else:
    print(f"[OK] OPTIMAL TEMPERATURE ({brake_temp}°C). Current CAD design is safe.")

print("\n--- [STAGE 2] TRANSMITTING UPDATED CAD DATA TO MANUFACTURING ROBOT ---")
print(f"TARGET THICKNESS: {new_thickness} mm (original: {disc_thickness} mm)")
print(f"TARGET VENTS     :{new_vents} channels (Original: {cooling_vents} channels) ")
print("START             Data packet sent to RobotDK / Industrial CNC Cell!")
print("====================================================================")