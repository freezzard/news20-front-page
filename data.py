"""Story data for the Friday 20 November 2026 world-news page.

Every story below happened, or was first reported, on Friday
20 November 2026 in some time zone, and was checked against wire
reporting (Reuters, AP, AFP and agency copy) on the day itself.
Claims that rest on one side's account carry an epistemic chip.
Summaries are sized to their cards: heroes get three lines, the
mid cards two, so nothing on the page is cut off mid-sentence.
"""

PAGE_DATE_LONG = "Friday 20 November 2026"
PAGE_KICKER_LEFT = "THE WORLD IN ONE DAY"
PAGE_KICKER_RIGHT = "40 STORIES - EVERY CONTINENT - ALL FROM THIS ONE DAY"
PAGE_SUBHEAD = (
    "Cyclone Akvan comes ashore in Odisha - Kyiv's bridges are hit in the "
    "war's biggest barrage - COP31 ends in deadlock over fossil fuels"
)

REGION_TALLY = [
    ("ASIA", 9, "#c0532f"),
    ("EUROPE", 8, "#33629e"),
    ("MIDDLE EAST", 4, "#4c7a34"),
    ("AFRICA", 1, "#a5832f"),
    ("AMERICAS", 12, "#74478f"),
    ("OCEANIA", 3, "#2f7f7a"),
    ("GLOBAL", 3, "#5a5a55"),
]

DAY_NUMBERS = [
    ("372,000", "people evacuated in Odisha"),
    ("3", "Dnipro bridges hit in Kyiv"),
    ("$2.36bn", "GTA VI's first day of sales"),
    ("-8.3%", "Asia-Pacific shares this week"),
    ("48-51", "Senate blocks the Iran curb"),
    ("175*", "Nicholls not out at Wellington"),
]

# Card fields: number, kicker, place line, headline, summary, source,
# chip (or ""), scene key, map longitude, map latitude.
HERO_CARDS = [
    {
        "num": 1,
        "kicker": "ODISHA - STORM",
        "place": "GOPALPUR - BAY OF BENGAL",
        "headline": "Cyclone Akvan makes landfall in Odisha",
        "summary": (
            "The third cyclone in a month crossed the coast near Gopalpur "
            "at dawn, winds gusting to 90 km/h. Over 372,000 people were "
            "sheltered; no deaths reported."
        ),
        "source": "Reuters - IMD",
        "chip": "REPORTED",
        "scene": "akvan",
        "lon": 84.9,
        "lat": 19.8,
    },
    {
        "num": 2,
        "kicker": "KYIV - WAR",
        "place": "KYIV - UKRAINE",
        "headline": "Missiles hit Kyiv's three river bridges",
        "summary": (
            "Missiles struck the Darnytskyi, Pivdennyi and "
            "Podilsko-Voskresenskyi bridges, killing three and wounding "
            "15 - the war's biggest bridge attack."
        ),
        "source": "Reuters - Kyiv Independent",
        "chip": "REPORTED",
        "scene": "kyiv",
        "lon": 30.5,
        "lat": 50.4,
    },
    {
        "num": 3,
        "kicker": "ANTALYA - CLIMATE",
        "place": "ANTALYA - COP31 FINAL DAY",
        "headline": "COP31 deadlocked as fossil fuels vanish from the text",
        "summary": (
            "The final draft drops fossil fuels and the $120bn adaptation "
            "goal. Nearly 200 countries argued past the Friday deadline."
        ),
        "source": "Reuters - AFP - UN News",
        "chip": "REPORTED",
        "scene": "cop31",
        "lon": 30.7,
        "lat": 36.9,
    },
]

MID_CARDS = [
    {
        "num": 4,
        "kicker": "TOKYO - MARKETS",
        "place": "TOKYO - SEOUL - TAIPEI",
        "headline": "Asia's AI rout: worst week since 2020",
        "summary": "Nikkei -4.1%, Kospi -4.7%; Taiwan's week is its worst since 1991.",
        "source": "Reuters",
        "chip": "",
        "scene": "selloff",
        "lon": 139.7,
        "lat": 35.7,
    },
    {
        "num": 5,
        "kicker": "HORMUZ - ENERGY",
        "place": "STRAIT OF HORMUZ",
        "headline": "Oil falls a third week as Hormuz flows recover",
        "summary": "Brent near $92. Iran's Guards claim two tankers hit mines.",
        "source": "Reuters",
        "chip": "CLAIM",
        "scene": "hormuz",
        "lon": 56.3,
        "lat": 26.6,
    },
    {
        "num": 6,
        "kicker": "WASHINGTON - POLITICS",
        "place": "US SENATE",
        "headline": "Senate refuses to curb Trump's Iran war",
        "summary": "War-powers vote fails 48-51; Democrats vow a 2027 funding fight.",
        "source": "Reuters - AP",
        "chip": "",
        "scene": "senate",
        "lon": -77.0,
        "lat": 38.9,
    },
    {
        "num": 7,
        "kicker": "SHENZHEN - DIPLOMACY",
        "place": "AFTER THE APEC SUMMIT",
        "headline": "Middle powers cut their own deals",
        "summary": "Canada extends its China tariff deal; Japan chases ASEAN minerals.",
        "source": "Reuters - Xinhua",
        "chip": "",
        "scene": "shenzhen",
        "lon": 114.1,
        "lat": 22.5,
    },
    {
        "num": 8,
        "kicker": "JAKARTA - DIPLOMACY",
        "place": "JAKARTA - BEIJING",
        "headline": "Prabowo and Xi talk South China Sea",
        "summary": "The two leaders discuss trade, investment and the disputed sea.",
        "source": "Reuters",
        "chip": "",
        "scene": "jakarta",
        "lon": 106.8,
        "lat": -6.2,
    },
    {
        "num": 9,
        "kicker": "THE HAGUE - JUSTICE",
        "place": "MYANMAR ANSWERS THE COURT",
        "headline": "Myanmar calls the genocide ruling 'unfair'",
        "summary": "Naypyidaw rejects the verdict; Dhaka floats returns in 1-1.5 years.",
        "source": "Reuters",
        "chip": "",
        "scene": "hague",
        "lon": 4.5,
        "lat": 52.1,
    },
    {
        "num": 10,
        "kicker": "GAZA - WAR",
        "place": "CENTRAL GAZA",
        "headline": "Israeli forces cross the truce line in Gaza",
        "summary": "First ground incursion since the ceasefire; families flee.",
        "source": "Reuters",
        "chip": "REPORTED",
        "scene": "gaza",
        "lon": 34.3,
        "lat": 31.4,
    },
    {
        "num": 11,
        "kicker": "WELLINGTON - CRICKET",
        "place": "FIRST TEST - DAY TWO",
        "headline": "Nicholls 175* lifts New Zealand to 368",
        "summary": "Nicholls and Phillips (118) add 216 after 70-5. India reply 159-1.",
        "source": "Reuters",
        "chip": "",
        "scene": "cricket",
        "lon": 174.8,
        "lat": -41.3,
    },
    {
        "num": 12,
        "kicker": "WORLDWIDE - GAMES",
        "place": "LAUNCH DAY TOTALS",
        "headline": "GTA VI's first day: an estimated $2.36bn",
        "summary": "24.6m copies on day one, near 3x GTA V, plus 125m stream hours.",
        "source": "Sensor Tower - VGC",
        "chip": "ESTIMATE",
        "scene": "gtavi",
        "lon": -74.0,
        "lat": 40.7,
    },
    {
        "num": 13,
        "kicker": "LAS VEGAS - FORMULA 1",
        "place": "STRIP CIRCUIT - PRACTICE",
        "headline": "Rain washes out Las Vegas practice",
        "summary": "First session flooded, no timed laps. Russell tops wet FP2.",
        "source": "Reuters - FIA",
        "chip": "",
        "scene": "f1",
        "lon": -115.1,
        "lat": 36.2,
    },
]

# Brief fields: number, place, text, source.
BRIEFS = [
    (14, "Gopalpur", "Odisha's assembly adjourns to 23 Nov as Akvan crosses the coast.", "IMD"),
    (15, "Puri", "69 trains cancelled across the cyclone zone; 423 rescue teams deployed.", "PTI"),
    (16, "Warsaw", "Poland probes unknown objects that fell near the Ukraine border.", "Reuters"),
    (17, "Brussels", "EU will summon Russia's envoy over embassy damage in Kyiv.", "Euronews"),
    (18, "London", "Britain pledges 1,000+ drones for Ukraine in a GBP 260m package.", "UK MoD"),
    (19, "Moscow", "Ryabkov rejects NATO-style security guarantees for Ukraine.", "Reuters"),
    (20, "Baghdad", "Iraqi forces to deploy in the militia stronghold of Jurf al-Sakhar.", "Reuters"),
    (21, "New York", "Dollar index at 103.9, its highest since April 2025, on haven flows.", "Reuters"),
    (22, "Cook Islands", "Record November cyclone Xavier weakens south of Manihiki.", "NASA - MetService"),
    (23, "San Salvador", "President Bukele registers to seek a third term.", "AP"),
    (24, "Caracas", "US and Venezuela sign a military cooperation deal.", "Wire reports"),
    (25, "Al-Dahi", "A mosque is set on fire in northern Israel.", "Wire reports"),
    (26, "Sydney", "Man charged over an alleged car-bomb plot and IS material.", "AP"),
    (27, "Buenos Aires", "Senate approves a permanent disability framework, 71-0.", "Telam"),
    (28, "Paris", "Kamala Harris meets Macron amid talk of a 2028 bid.", "AFP"),
    (29, "Zurich", "Diallo and Tashima confirmed as challengers for the FIFA presidency.", "AFP"),
    (30, "Mexico City", "Christie's halts a Frida Kahlo sale at Mexico's request.", "AP"),
    (31, "Rome", "A long-buried ancient library opens to the public, restored.", "AP"),
    (32, "Brasilia", "Lula moves to protect Chief Raoni's birthplace in the Amazon.", "AP"),
    (33, "Port-au-Prince", "Heavy fighting as Haiti's forces battle gangs for a key corridor.", "AP"),
    (34, "New York", "Security Council ballots on Grynspan's bid for the UN's top job.", "UN News"),
    (35, "Washington", "US sanctions the Comancheros and 'Ndrangheta crime networks.", "US Treasury"),
    (36, "Washington", "Trump announces a posthumous pardon for baseball's Pete Rose.", "AP"),
    (37, "London", "589 million children live in war zones, a record share.", "Save the Children"),
    (38, "Cotonou", "Benin seeks the return of artworks looted by France.", "AFP"),
    (39, "Seoul", "Exchange halts trading briefly as the Kospi plunges 5.7%.", "Dow Jones"),
    (40, "Tokyo", "Yen steadies near 159.5 after Japanese inflation data.", "Reuters"),
]

LEFT_OUT = (
    "18 Nov: Voyager 1 reaches one light-day from Earth - Yunus home fire "
    "in Chattogram. 17 Nov: Hayabusa2 retargeted. 19 Nov: the Shenzhen "
    "summit itself - the World Court verdict - GTA VI launch day."
)
NOT_YET = (
    "COP31's closing plenary (Sat) - Las Vegas qualifying (Fri night) - "
    "India's day-three reply at Wellington."
)
DATE_CHECK_LINE = (
    "Every story on this page happened, or was first reported, on Friday "
    "20 November 2026 (any time zone)."
)
DISCLAIMER_LINE = "Claims are attributed, not stated as fact."
SOURCES_LINE = (
    "Sources: Reuters, AP, AFP, UN News, IMD, NASA, Sensor Tower, FIA, PTI "
    "- Pictures and map drawn in code - 2026-11-20"
)
