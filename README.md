# Automated Optoelectronic Instrument Controller

This project demonstrates hardware/software interfacing and automated data acquisition using Python and PyVISA. 

It was developed to showcase the ability to communicate with standard laboratory equipment (via SCPI commands), automate measurement sequences, and handle data acquisition layers without requiring immediate access to physical hardware by utilizing `pyvisa-sim`.

## Features
* Automated instrument discovery and connection setup.
* Execution of standard SCPI queries.
* Simulated multi-step data acquisition loop.
* Safe resource management and error handling.
## How to run

1. Install the required dependencies:

```bash
pip install pyvisa pyvisa-sim
python instrument_controller.py
```
Example output:
```bash
--- Starting Instrument Control Sequence ---
Detected devices: ('USB0::0x1111::0x2222::12345678::0::INSTR',)
Successfully connected to: SIM,Photodiode-DMM,SN00123,v1.0
--- Starting Data Acquisition (Photodiode Voltage) ---
Reading 1: 0.6823 V
Reading 2: 0.9813 V
Reading 3: 0.8104 V
Reading 4: 0.7465 V
Reading 5: 0.8542 V
--- Acquisition Complete ---
Average Photodiode Voltage: 0.8149 V
```