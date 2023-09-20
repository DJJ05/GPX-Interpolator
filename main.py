# Assumes f1.gpx exists whereby:
# <wpt>...</wpt>
# with nothing above or below the list of wpts

class Point:
    def __init__(self, lat: float, long: float) -> None:
        self.lat = lat
        self.long = long
        
    def __repr__(self) -> str:
        return f"[Point lat={format(self.lat, '.6f')} long={format(self.long, '.6f')}]"
        
    def display(self) -> str:
        return f"<wpt lat=\"{format(self.lat, '.6f')}\" lon=\"{format(self.long, '.6f')}\"></wpt>"

with open("f1.gpx") as f:
    raw = f.read().splitlines()

points = []
last = None
for point in raw:
    lat = float(point.lstrip('<wpt lat="').split('"')[0])
    long = float(point.rstrip('"></wpt>').split('"')[-1])
    
    if not last:
        points.append(Point(lat, long))
        last = Point(lat, long)
        continue
    
    mid_lat = last.lat + ((lat - last.lat) / 2)
    mid_long = last.long + ((long - last.long) / 2)
    points.append(Point(mid_lat, mid_long))
    points.append(Point(lat, long))
    last = Point(lat, long)

# This is just a demo script, edit the below lines
# for further processing or file dumping
for point in points:
    print(point.display())
