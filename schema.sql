create table aircraft(
    _id INTEGER PRIMARY KEY,
    hexcode TEXT,
    squawk TEXT,
    flight TEXT,
    lat REAL,
    lon REAL,
    altitude INT,
    vertRate INT,
    track INT,
    speed INT,
    messages INT,
    mlat INT,
    timeSeen INT,
    rssi REAL
);

create table stats(
    _id INTEGER PRIMARY KEY,
    aircraftSeenToday INT,
    totalAircraftSeen INT,
    lastUpdated TEXT
);

