def ms_to_kmh(ms):
    kmh = ms * 3.6
    return f'{ms} m/s = {int(kmh)} km/h' 

print(ms_to_kmh(10))
print(ms_to_kmh(35))