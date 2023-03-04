DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_id                TEXT,
    user_username          TEXT,
    user_name              TEXT,
    user_last_name         TEXT,
    user_createdat         TEXT,
    user_total_followers   TEXT,
    user_total_following   TEXT,
    user_total_tweets      TEXT,
    user_avatar            TEXT,
    user_cover             TEXT,
    PRIMARY KEY(user_id)

)WITHOUT ROWID;

INSERT INTO users VALUES("773fb079ed8d464eb8bef39d2c843128","elonmusk","Elon","Musk", "1244132713","129200000","178","22900","773fb079ed8d464eb8bef39d2c843128.jpg","773fb079ed8d464eb8bef39d2c843128.jpg");
INSERT INTO users VALUES("32d322f985804fea8e9f7525053df778","matpat","MatPat","", "1244132713","5500000","491","4348","32d322f985804fea8e9f7525053df778.jpg", "32d322f985804fea8e9f7525053df778.jpg");
INSERT INTO users VALUES("1ad43d14574045a39006da33bc476d20","Daniel_Sloss","Daniel","Sloss", "1244132713","180500","1133","28400","1ad43d14574045a39006da33bc476d20.jpg", "1ad43d14574045a39006da33bc476d20.jpg");