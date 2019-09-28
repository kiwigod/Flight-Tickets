BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "tickets" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"start_dt"	TEXT NOT NULL,
	"end_dt"	TEXT NOT NULL,
	"start_iata"	TEXT NOT NULL,
	"end_iata"	TEXT NOT NULL,
	"airline"	TEXT NOT NULL,
	"duration"	INTEGER NOT NULL,
	"price"	INTEGER NOT NULL,
	"transfers"	INTEGER DEFAULT NULL,
	"ts"	TEXT DEFAULT 'strftime(''%Y-%m-%d %H:%M:%S'',''now'')'
);
CREATE INDEX IF NOT EXISTS "idxAirline" ON "tickets" (
	"airline"
);
CREATE INDEX IF NOT EXISTS "idxRoute" ON "tickets" (
	"start_iata",
	"end_iata"
);
COMMIT;
