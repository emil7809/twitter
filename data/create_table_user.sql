DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_id                TEXT,
    user_username          TEXT,
    user_name              TEXT,
    user_last_name         TEXT,
    user_total_followers   TEXT,
    user_total_following   TEXT,
    user_total_tweets      TEXT,
    user_avatar            TEXT,
    PRIMARY KEY(user_id)

)WITHOUT ROWID;

INSERT INTO users VALUES("773fb079-ed8d-464e-b8be-f39d2c843128","elonmusk","Elon","Musk","129200000","178","22900","773fb079-ed8d-464e-b8be-f39d2c843128.jpg");
INSERT INTO users VALUES("32d322f9-8580-4fea-8e9f-7525053df778","matpat","MatPat","","5500000","491","4348","32d322f9-8580-4fea-8e9f-7525053df778.jpg");
INSERT INTO users VALUES("1ad43d14-5740-45a3-9006-da33bc476d20","Daniel_Sloss","Daniel","Sloss","180500","1133","28400","1ad43d14-5740-45a3-9006-da33bc476d20.jpg");