DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
  tweet_id              TEXT,
  tweet_user_fk         TEXT,
  tweet_created_at      TEXT,
  tweet_message         TEXT,
  tweet_image           TEXT,
  tweet_updated_at      TEXT,
  tweet_total_retweets  TEXT,
  tweet_total_likes     TEXT,
  tweet_total_views     TEXT,
  tweet_total_replies   TEXT,
  PRIMARY KEY(tweet_id)
) WITHOUT ROWID;

INSERT INTO tweets VALUES(
  "4e638cbcd027472facf5080f336bdb83", 
  "1ad43d14574045a39006da33bc476d20",
  "1672064261",
  "I’m delighted",
  "4e638cbcd027472facf5080f336bdb83.jpg",
  "0",
  "362",
  "2582",
  "216900",
  "36"
  );

INSERT INTO tweets VALUES(
  "a600818947644cfdbd51987e81886091", 
  "32d322f985804fea8e9f7525053df778",
  "1676729861",
  "IT'S HERE! Did you guess the new channel right??",
  "a600818947644cfdbd51987e81886091.jpg",
  "0",
  "2988",
  "33800",
  "2700000",
  "1723"
  );

INSERT INTO tweets VALUES(
  "ab9210ead6154bc3b16014acbf47fd6c", 
  "32d322f985804fea8e9f7525053df778",
  "1675347461",
  "Exciting news: Theorist is HIRING! ",
  "",
  "0",
  "309",
  "4913",
  "2552000",
  "157"
  );

INSERT INTO tweets VALUES(
  "b7036182edf1490cb5ad78e981df647d", 
  "773fb079ed8d464eb8bef39d2c843128",
  "1676740661",
  "Surround your house with treadmills set to jogging speed to stop walking dead ur welcome",
  "b7036182edf1490cb5ad78e981df647d.jpg",
  "0",
  "36200",
  "454300",
  "64200000",
  "171000"
  );