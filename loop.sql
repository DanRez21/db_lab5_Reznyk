DO $$ 
DECLARE
    i INT;
BEGIN
    FOR i IN 1..5 LOOP
        -- Ваші тестові дані та запит INSERT
        INSERT INTO evaluation(eva_id, points, taster_id) VALUES (i+5, 80+i, i);
    END LOOP;
END $$;