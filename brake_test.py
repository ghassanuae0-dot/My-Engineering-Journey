import datetime


class VentilatedBrakeDisc:
    def __init__(self, model, thickness, vents, lap_temps):
        self.model = model
        self.thickness = thickness
        self.vents = vents
        self.lap_temps = lap_temps

    
    def analyze_and_export_to_robot(self):
        max_temp = max(self.lap_temps)
        new_thickness = self.thickness
        new_vents = self.vents
        robot_action = "NO_MODIFICATION_NEEDED"

        if max_temp > 800:
            new_thickness = round(self.thickness + 2.5, 1)
            new_vents = self.vents + 12
            robot_action = "FABRICATE_REINFORCED_DISC"
        elif max_temp > 650:
            new_vents = self.vents + 6
            robot_action = "DRILL_EXTRA_VENTS"

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        
        with open("robot_instructions.txt", "a") as file:
            file.write(f"--- REPORT AT {timestamp} ---\n")
            file.write(f"COMPONENT       : {self.model}\n")
            file.write(f"PEAK_TEMP       : {max_temp} C\n")
            file.write(f"ROBOT_COMMAND   : {robot_action}\n")
            file.write(f"TARGET_THICKNESS: {new_thickness} mm (Original: {self.thickness} mm)\n")
            file.write(f"TARGET_VENTS    : {new_vents} channels (Original: {self.vents} channels)\n\n")

        print(f"[{self.model}] Peak: {max_temp}°C -> Command: {robot_action}")

        print(f"   -> New thickness: {new_thickness} mm | New vents: {new_vents}")

print("=== ANDROMEYDA AI DIGITAL TWIN: 4-WHEEL BRAKE TO ROBOT SYSTEM ===")


front_right = VentilatedBrakeDisc("FRONT-RIGHT-V1", 32.0, 36, [620.0, 710.5, 795.0, 845.0, 810.0])
front_left  = VentilatedBrakeDisc("FRONT-LEFT-V1",  32.0, 36, [600.0, 680.0, 720.0, 740.0, 710.0])
rear_right  = VentilatedBrakeDisc("REAR-RIGHT-V1",  28.0, 30, [480.0, 510.0, 540.0, 560.0, 550.0])
rear_left   = VentilatedBrakeDisc("REAR-LEFT-V1",   28.0, 30, [475.0, 505.0, 535.0, 555.0, 545.0])


front_right.analyze_and_export_to_robot()
front_left.analyze_and_export_to_robot()
rear_right.analyze_and_export_to_robot()
rear_left.analyze_and_export_to_robot()

print("\n[DONE] All 4 brake disc reports exported to 'robot_instructions.txt'!")
