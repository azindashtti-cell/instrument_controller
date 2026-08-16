import pyvisa
import time

def main():
    print("--- Starting Instrument Control Sequence ---")
    
    # 1. Load the simulated device using the YAML file
    rm = pyvisa.ResourceManager('simulated_sensor.yaml@sim')
    
    # 2. Find connected devices
    resources = rm.list_resources()
    print(f"Detected devices: {resources}")
    
    if not resources:
        print("No devices found. Exiting.")
        return

    # 3. Connect to the first found device
    instrument = rm.open_resource(resources[0])
    
    # 4. Establish communication: Send *IDN? command
    identity = instrument.query("*IDN?")
    print(f"Successfully connected to: {identity.strip()}")
    
    # 5. Simulate a Data Acquisition campaign
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
    
    # 6. Safely close the connection
    instrument.close()

if __name__ == "__main__":
    main()