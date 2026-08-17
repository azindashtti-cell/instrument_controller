import pyvisa
import time

def main():
    print("--- Starting Instrument Control Sequence ---")
    
    # 1. Load the built-in default simulated backend (bypasses all YAML file issues)
    rm = pyvisa.ResourceManager('@sim')
    
    # 2. Find connected devices
    resources = rm.list_resources()
    print(f"Detected devices: {resources}")
    
    if not resources:
        print("No devices found. Exiting.")
        return

    # 3. Connect to the first found device (usually a simulated multimeter/oscilloscope)
    instrument = rm.open_resource(resources[0])
    
    # 4. Establish communication: Send *IDN? command
    identity = instrument.query("*IDN?")
    print(f"Successfully connected to: {identity.strip()}")
    
    # 5. Simulate a Data Acquisition campaign
    # In an optics lab, you measure light by reading the voltage of a photodiode
    print("\n--- Starting Data Acquisition (Photodiode Voltage) ---")
    measurements = []
    
    for i in range(5):
        # Query the voltage from the simulated instrument
        data = instrument.query("MEAS:VOLT:DC?")
        measurements.append(float(data))
        print(f"Reading {i+1}: {data.strip()} V")
        time.sleep(0.5)
        
    print("\n--- Acquisition Complete ---")
    print(f"Average Photodiode Voltage: {sum(measurements)/len(measurements):.4f} V")
    
    # 6. Safely close the connection
    instrument.close()

if __name__ == "__main__":
    main()