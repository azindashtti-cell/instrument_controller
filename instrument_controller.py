import os
import pyvisa
import time

# We define the exact YAML configuration here in Python as a raw string 
# to guarantee there are no invisible formatting errors.
YAML_CONFIG = r"""spec: "1.0"
interfaces:
  ASRL:
    1:
      device: device 1
devices:
  device 1:
    eom:
      ASRL INSTR:
        q: "\n"
        r: "\n"
    error: ERROR
    dialogues:
      - q: "*IDN?"
        r: "Telecom_SudParis_Simulated_Optic_Sensor_V1.0"
      - q: "MEAS:LIGHT?"
        r: "4.82"
"""

def main():
    print("--- Starting Instrument Control Sequence ---")
    
    # 1. Force Python to create/overwrite the YAML file itself
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(current_dir, 'simulated_sensor.yaml')
    
    with open(yaml_path, 'w') as f:
        f.write(YAML_CONFIG)
        
    print(f"[DEBUG] Simulated hardware file generated at: {yaml_path}")
    
    # 2. Load the simulated device using the newly generated file
    try:
        rm = pyvisa.ResourceManager(f'{yaml_path}@sim')
    except Exception as e:
        print(f"[DEBUG] Absolute path failed, falling back to relative. Error: {e}")
        rm = pyvisa.ResourceManager('simulated_sensor.yaml@sim')
    
    # 3. Find connected devices
    resources = rm.list_resources()
    print(f"Detected devices: {resources}")
    
    if not resources:
        print("No devices found. Exiting.")
        return

    # 4. Connect to the first found device (ASRL1::INSTR)
    instrument = rm.open_resource(resources[0])
    
    # 5. Establish communication: Send *IDN? command
    identity = instrument.query("*IDN?")
    print(f"Successfully connected to: {identity.strip()}")
    
    # 6. Simulate a Data Acquisition campaign
    print("\n--- Starting Data Acquisition ---")
    measurements = []
    
    for i in range(5):
        # Query the light sensor data
        data = instrument.query("MEAS:LIGHT?")
        measurements.append(float(data))
        print(f"Reading {i+1}: {data.strip()} mW")
        time.sleep(0.5)
        
    print("\n--- Acquisition Complete ---")
    print(f"Average Light Intensity: {sum(measurements)/len(measurements)} mW")
    
    # 7. Safely close the connection
    instrument.close()

if __name__ == "__main__":
    main()