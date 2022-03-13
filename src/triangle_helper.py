import math

## Math Helper Functions
class TriangleHelper:
# Find oppisite leg given angle and adjacent leg
    def find_oppisite(angle, adj):
        opp = round(math.tan(math.radians(angle)) * adj, 3)
        return opp

    # Find short leg of post
    def short_leg(height, angle, adj):
        return height - TriangleHelper.find_oppisite(angle, adj)

    # Calculate Rail Angle
    def rail_angle(rise, run):
        angle = round(math.degrees(math.atan(rise/run)), 3)
        return angle

    # Calculate miter angle
    def mitre_angle(angle):
        mitre = abs(angle - 90) / 2
        return mitre

    def alt_angle(angle):
        return abs(angle - 90)