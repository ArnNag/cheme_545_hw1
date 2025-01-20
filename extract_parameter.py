unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
}

def extract_parameter(unit_name: str, parameter_name: str, index: int) -> str:
    """
    :param unit_name: the lab equipment. Can be distillation_column, reactor, or heat_exchanger
    :param parameter_name: a physical quantity such as temperature or pressure
    :param index: the index into the list of possible parameters 
    :return: a string containing the unit name, parameter name, and value, or "Invalid input" if the unit name or parameter name is not found or index is out of range
    """
    try:
        return f"{unit_name}_{parameter_name}_{unit_operations_data[unit_name][parameter_name][index]}" # F-strings are a way to put variable values into strings. I use brackets to index into dictionaries and lists.
    except (KeyError, IndexError): # I only want to provide this output if a key or index isn't found
        return "Invalid input"
