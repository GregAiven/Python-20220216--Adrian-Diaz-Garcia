CREATE TABLE IF NOT EXISTS public.check_results (
    id SERIAL PRIMARY KEY,
    url text NOT NULL,
    regex text NOT NULL,
    http_status integer NOT NULL,
    check_result boolean NOT NULL,
    elapsed float NOT NULL,
    created TIMESTAMPTZ DEFAULT Now()
                                  );
