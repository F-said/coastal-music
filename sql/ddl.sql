CREATE TABLE IF NOT EXISTS song(
	song_id INT PRIMARY KEY,
    title TEXT,
    musician TEXT,
    album TEXT,
    acoustiness REAL NOT NULL,
    danceability REAL NOT NULL,
    energy REAL NOT NULL,
    instrumentalness REAL NOT NULL,
    liveliness REAL NOT NULL,
    loudness REAL NOT NULL,
    speechiness REAL NOT NULL,
    valence REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS entry(
	entry_id INT PRIMARY KEY,
   	song_id TEXT NOT NULL,
	state TEXT NOT NULL,
    FOREIGN KEY (song_id) 
        REFERENCES song(song_id) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);

