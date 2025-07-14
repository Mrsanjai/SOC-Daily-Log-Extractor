# geoip_lookup.py
import requests

def get_country_from_ip(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        if data['status'] == 'success':
            return data['country']
        else:
            return "Unknown"
    except Exception as e:
        print(f"[GeoIP Error] {e}")
        return "Error"

def get_geo_data(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        if data['status'] == 'success':
            return {
                "country": data['country'],
                "lat": data['lat'],
                "lon": data['lon']
            }
        else:
            return {"country": "Unknown", "lat": 0, "lon": 0}
    except Exception as e:
        print(f"[GeoIP Error] {e}")
        return {"country": "Error", "lat": 0, "lon": 0}
