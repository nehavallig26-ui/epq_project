import math

# -----------------------
# Constants
# -----------------------
AIR_DENSITY = 1.225  # kg/m^3
FRONTAL_AREA = 2.2   # m^2 (typical supercar)
BASE_CD = 0.30       # base drag coefficient
BASE_CL = -0.10      # base lift coefficient (negative = downforce)



# -----------------------
def modify_drag(body_kit, spoiler):
    cd = BASE_CD

    if body_kit == "wide":
        cd += 0.02
    elif body_kit == "track":
        cd += 0.04

    if spoiler == "large":
        cd += 0.05
    elif spoiler == "medium":
        cd += 0.02

    return cd


def modify_lift(spoiler, wing_angle):
    cl = BASE_CL

    if spoiler == "large":
        cl -= 0.20
    elif spoiler == "medium":
        cl -= 0.10

    # Wing angle increases downforce
    try:
        angle = float(wing_angle)
        cl -= angle * 0.005
    except:
        pass

    return cl


# -----------------------
# Main Simulation Function
# -----------------------
def calculate_aero(config):
    """
    config = {
        "body_kit": str,
        "spoiler": str,
        "wheels": str,
        "color": str,
        "ride_height": str,
        "wing_angle": str
    }
    """

    speed = 70  # m/s (~250 km/h)

    cd = modify_drag(config["body_kit"], config["spoiler"])
    cl = modify_lift(config["spoiler"], config["wing_angle"])

    # Drag Force
    drag = 0.5 * AIR_DENSITY * speed**2 * cd * FRONTAL_AREA

    # Downforce
    downforce = 0.5 * AIR_DENSITY * speed**2 * abs(cl) * FRONTAL_AREA

    # Efficiency metric
    efficiency = downforce / drag if drag != 0 else 0

    return {
        "drag": round(drag, 2),
        "downforce": round(downforce, 2),
        "efficiency": round(efficiency, 3),
        "cd": round(cd, 3),
        "cl": round(cl, 3)
    }
