import streamlit as st

# Ohm's Law Calculator
def ohms_law_calculator(voltage, current, resistance):
    if voltage and current:
        resistance = voltage / current
        return f"Resistance = {resistance} Ohms"
    elif voltage and resistance:
        current = voltage / resistance
        return f"Current = {current} Amps"
    elif current and resistance:
        voltage = current * resistance
        return f"Voltage = {voltage} Volts"
    else:
        return "Please provide any two values."

# LED Resistor Calculator
def led_resistor_calculator(voltage, forward_voltage, forward_current):
    if forward_voltage <= 0 or forward_current <= 0:
        return "Forward voltage and forward current must be greater than 0."
    else:
        resistance = (voltage - forward_voltage) / forward_current
        return f"Resistor value = {resistance} Ohms"

# Transistor HFE Calculator
def transistor_hfe_calculator(ib, ic):
    if ic <= 0:
        return "Collector current must be greater than 0."
    else:
        hfe = ic / ib
        return f"HFE (Beta) = {hfe}"

# OpAmp Calculator
def opamp_calculator(voltage_in, voltage_out, gain):
    if voltage_in is not None and voltage_out is not None:
        gain = voltage_out / voltage_in
        return f"Gain = {gain}"
    elif voltage_in is not None and gain is not None:
        voltage_out = voltage_in * gain
        return f"Output Voltage = {voltage_out} Volts"
    elif voltage_out is not None and gain is not None:
        voltage_in = voltage_out / gain
        return f"Input Voltage = {voltage_in} Volts"
    else:
        return "Please provide any two values."

# Streamlit UI
st.title("Electronics Calculators")

calculator_choice = st.sidebar.selectbox(
    "Choose Calculator",
    ("Ohm's Law Calculator", "LED Resistor Calculator", "Transistor HFE Calculator", "OpAmp Calculator")
)

if calculator_choice == "Ohm's Law Calculator":
    st.header("Ohm's Law Calculator")
    voltage = st.number_input("Enter Voltage (Volts)", min_value=0.0)
    current = st.number_input("Enter Current (Amps)", min_value=0.0)
    resistance = st.number_input("Enter Resistance (Ohms)", min_value=0.0)
    st.write(ohms_law_calculator(voltage, current, resistance))

elif calculator_choice == "LED Resistor Calculator":
    st.header("LED Resistor Calculator")
    voltage = st.number_input("Enter Supply Voltage (Volts)", min_value=0.0)
    forward_voltage = st.number_input("Enter LED Forward Voltage (Volts)", min_value=0.0)
    forward_current = st.number_input("Enter LED Forward Current (Amps)", min_value=0.0)
    st.write(led_resistor_calculator(voltage, forward_voltage, forward_current))

elif calculator_choice == "Transistor HFE Calculator":
    st.header("Transistor HFE Calculator")
    ib = st.number_input("Enter Base Current (Amps)", min_value=0.0)
    ic = st.number_input("Enter Collector Current (Amps)", min_value=0.0)
    st.write(transistor_hfe_calculator(ib, ic))

elif calculator_choice == "OpAmp Calculator":
    st.header("OpAmp Calculator")
    voltage_in = st.number_input("Enter Input Voltage (Volts)", min_value=0.0)
    voltage_out = st.number_input("Enter Output Voltage (Volts)", min_value=0.0)
    gain = st.number_input("Enter Gain", min_value=0.0)
    st.write(opamp_calculator(voltage_in, voltage_out, gain))
