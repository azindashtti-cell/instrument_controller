import pyvisa
import time

def main():
    print("--- Starting Instrument Control Sequence ---")
    
    rm = pyvisa.ResourceManager('simulated_sensor.yaml@sim')
    
    resources = rm.list_resources()
    print(f"Detected devices: {resources}")
    
    if not resources:
        print("No devices found. Exiting.")
        return

    instrument = rm.open_resource(resources[0])
    
   identity = instrument.query("*IDN?")
    print(f"Successfully connected to: {identity.strip()}")
    
    print("\n--- Starting Data Acquisition ---")
    measurements = []
    
    for i in range(5):
       
        data = instrument.query("MEAS:LIGHT?")
        measurements.append(float(data))
        print(f"Reading {i+1}: {data.strip()} mW")
        time.sleep(0.5) 
    print("\n--- Acquisition Complete ---")
    print(f"Average Light Intensity: {sum(measurements)/len(measurements)} mW")
    
    instrument.close()

if __name__ == "__main__":
    main()