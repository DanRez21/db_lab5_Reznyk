CREATE TABLE Taster
(
  taster_name CHAR(40),
  taster_twitter_handle CHAR(20),
  taster_id INT NOT NULL,
  PRIMARY KEY (taster_id)
);

CREATE TABLE Evaluation
(
  eva_id INT NOT NULL,
  points INT NOT NULL,
  taster_id INT NOT NULL,
  PRIMARY KEY (eva_id),
  FOREIGN KEY (taster_id) REFERENCES Taster(taster_id)
);

CREATE TABLE Wine
(
  wine_id INT NOT NULL,
  description CHAR(300) NOT NULL,
  points INT NOT NULL,
  price INT,
  title CHAR(100) NOT NULL,
  variety CHAR(20) NOT NULL,
  eva_id INT NOT NULL,
  PRIMARY KEY (wine_id),
  FOREIGN KEY (eva_id) REFERENCES Evaluation(eva_id)
);

CREATE TABLE Location_
(
  country CHAR(20) NOT NULL,
  designation CHAR(20) NOT NULL,
  province CHAR(20) NOT NULL,
  region_1 CHAR(20),
  region_2 CHAR(20),
  winery CHAR(20) NOT NULL,
  location_id INT NOT NULL,
  wine_id INT NOT NULL,
  PRIMARY KEY (location_id),
  FOREIGN KEY (wine_id) REFERENCES Wine(wine_id)
);