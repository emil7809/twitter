DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_id                TEXT NOT NULL UNIQUE,
    user_email             TEXT NOT NULL UNIQUE,
    user_password          TEXT NOT NULL,
    user_username          TEXT NOT NULL UNIQUE,
    user_name              TEXT,
    user_last_name         TEXT,
    user_createdat         TEXT NOT NULL,
    user_total_followers   TEXT,
    user_total_following   TEXT,
    user_total_tweets      TEXT,
    user_avatar            TEXT UNIQUE,
    user_cover             TEXT UNIQUE,
    PRIMARY KEY(user_id)

)WITHOUT ROWID;

INSERT INTO users VALUES("773fb079ed8d464eb8bef39d2c843128", "elon@mail.com", "pass", "elonmusk","Elon","Musk", "1244132713","129200000","178","22900","773fb079ed8d464eb8bef39d2c843128.jpg","773fb079ed8d464eb8bef39d2c843128.jpg");
INSERT INTO users VALUES("32d322f985804fea8e9f7525053df778", "mat@mail.com", "pass", "matpat","MatPat","", "1244132713","5500000","491","4348","32d322f985804fea8e9f7525053df778.jpg", "32d322f985804fea8e9f7525053df778.jpg");
INSERT INTO users VALUES("1ad43d14574045a39006da33bc476d20", "daniel@mail.com", "pass", "Daniel_Sloss","Daniel","Sloss", "1244132713","180500","1133","28400","1ad43d14574045a39006da33bc476d20.jpg", "1ad43d14574045a39006da33bc476d20.jpg");
INSERT INTO users VALUES("cdd0a0a3be06427f84111a767e9729f9", "emily@hellyeah.com", "pass", "emilyhoolahan","Emily","Hoolahan", "1678536902","0","0","0","cdd0a0a3be06427f84111a767e9729f9.jpg", "cdd0a0a3be06427f84111a767e9729f9.jpg");

CREATE INDEX inx_user_name ON users(user_name);
CREATE INDEX inx_user_last_name ON users(user_last_name);