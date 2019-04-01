## Assertion

# Here is a function that converts a temperature from degrees Kelvin to degrees Fahrenheit.
# Since zero degrees Kelvin is as cold as it gets, the function bails out if it sees a negative temperature:

def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero"
    return((Temperature - 273) * 1.8) + 32

KelvinToFahrenheit(273)
KelvinToFahrenheit(505.78)
KelvinToFahrenheit(-5)