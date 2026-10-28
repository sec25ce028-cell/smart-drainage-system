
def check_drainage(water_level_cm, blockage_detected):
    """Check drainage readings and return a status."""

    if water_level_cm >= 30:
        return "WARNING: High water level"

    if blockage_detected:
        return "WARNING: Possible blockage detected"

    return "NORMAL: Drainage flow appears normal"


# Example sensor readings for simulation
readings = [
    (5, False),
    (15, False),
    (25, True),
    (35, True),
]

for level, blockage in readings:
    status = check_drainage(level, blockage)
    print(f"Water level: {level} cm | {status}")
