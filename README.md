# Automated Optoelectronic Instrument Controller

This project demonstrates hardware/software interfacing and automated data acquisition using Python and PyVISA. 

It was developed to showcase the ability to communicate with standard laboratory equipment (via SCPI commands), automate measurement sequences, and handle data acquisition layers without requiring immediate access to physical hardware by utilizing `pyvisa-sim`.

## Features
* Automated instrument discovery and connection setup.
* Execution of standard SCPI queries.
* Simulated multi-step data acquisition loop.
* Safe resource management and error handling.
