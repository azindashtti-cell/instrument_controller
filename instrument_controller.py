import pyvisa
import random
import time

def main():
    print("--- Starting Instrument Control Sequence ---")

    # 1. Point @sim at a real device definitions file (bare '@sim' has no
    #    commands defined, so MEAS:VOLT:DC? would fail).
    rm = pyvisa.ResourceManager('instruments.yaml@sim')

    # 2. Find connected devices
    resources = rm.list_resources()
    print(f"Detected devices: {resources}")

    if not resources:
        print("No devices found. Exiting.")
        return

    # 3. Connect to the first found device
    instrument = rm.open_resource(resources[0])
    instrument.read_termination = "\n"
    instrument.write_termination = "\n"
    instrument.timeout = 5000  # ms

    # 4. Establish communication: Send *IDN? command
    identity = instrument.query("*IDN?")
    print(f"Successfully connected to: {identity.strip()}")

    # 5. Simulate a Data Acquisition campaign
    print("\n--- Starting Data Acquisition (Photodiode Voltage) ---")
    measurements = []

    for i in range(5):
        # The simulated property is static unless written, so set a fresh
        # value each cycle to mimic a changing photodiode reading.
        sim_value = round(random.uniform(0.1, 1.0), 4)
        instrument.write(f"VOLT {sim_value}")

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