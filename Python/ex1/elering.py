import requests
from datetime import datetime
import zoneinfo  # Py3.9+: pip install tzdata kui vaja

elering_url = "https://dashboard.elering.ee/api/nps/price"

r = requests.get(elering_url, timeout=15)
r.raise_for_status()
data = r.json()

# Eesti hinnad: "ee" all on kohe list objektidest
rows = data["data"]["ee"]

# Teisendame unix sekundid Europe/Tallinn ajaks
tz = zoneinfo.ZoneInfo("Europe/Tallinn")
out = []
for x in rows:
    # timestamp on SEKUNDITES (ära jaga 1000-ga)
    dt_local = datetime.fromtimestamp(x["timestamp"], tz)
    out.append((dt_local, x["price"]))

# Näidis: prindi esimesed 5
for dt, price in out[:5]:
    print(dt.strftime("%Y-%m-%d %H:%M"), price)
