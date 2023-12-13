INSERT INTO Taster (taster_id, taster_name, taster_twitter_handle)
VALUES
(1, 'Kerin O’Keefe', '@kerinokeefe'),
(2, 'Roger Voss', '@vossroger'),
(3, 'Paul Gregutt', '@paulgwine'),
(4, 'Michael Schachner', '@wineschach'),
(5, 'Virginie Boone', '@vboone');

INSERT INTO Evaluation (eva_id, points, taster_id)
VALUES
(1, 87, 1),
(2, 93, 2),
(3, 80, 3),
(4, 96, 4),
(5, 90, 5);

INSERT INTO Wine (wine_id, description, points, price, title, variety, eva_id)
VALUES
(1, 'Aromas include tropical fruit, broom, brimstone and dried herb.', 87, 15, 'Nicosia 2013 Vulkà Bianco (Etna)', 'White Blend', 1),
(2, 'This is ripe and fruity, a wine that is smooth while still structured.', 93, 14, 'Quinta dos Avidagos 2011 Avidagos Red (Douro)', 'Portuguese Red', 2),
(3, 'Tart and snappy, the flavors of lime flesh and rind dominate.', 80, 13, 'Rainstorm 2013 Pinot Gris (Willamette Valley)', 'Pinot Gris', 3),
(4, 'Pineapple rind, lemon pith and orange blossom start off the aromas.', 96, 65, 'St. Julian 2013 Reserve Late Harvest Riesling (Lake Michigan Shore)', 'Riesling', 4),
(5, 'Blackberry and raspberry aromas show a typical Navarran whiff of green herbs', 90, 15, 'Tandem 2011 Ars In Vitro Tempranillo-Merlot (Navarra)', 'Tempranillo-Merlot', 5);

INSERT INTO location_ (location_id, country, designation, province, region_1, region_2, winery, wine_id)
VALUES
(1, 'Italy', 'Vulkà Bianco', 'Sicily & Sardinia', 'Etna', 'Etna', 'Nicosia', 1),
(2, 'Portugal', 'Avidagos', 'Douro', NULL, NULL, 'Quinta dos Avidagos', 2),
(3, 'US', 'Reserve Late', 'Oregon', 'Willamette Valley', 'Willamette Valley', 'Rainstorm', 3),
(4, 'US', 'Vintners Reserve', 'Michigan', 'Lake Michigan Shore', 'Lake Michigan Shore', 'St. Julian', 4),
(5, 'Spain', 'Ars In Vitro', 'Northern Spain', 'Navarra', 'Navarra', 'Tandem', 5);
