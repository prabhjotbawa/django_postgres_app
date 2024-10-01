DO $$
BEGIN
    -- Create database if it doesn't exist
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mydatabase') THEN
        CREATE DATABASE mydatabase;
    END IF;
END $$;

-- Connect to the mydatabase
\c mydatabase

DO $$
BEGIN
    -- Create user if it doesn't exist
    IF NOT EXISTS (SELECT FROM pg_user WHERE usename = 'myuser') THEN
        CREATE USER myuser WITH PASSWORD 'mypassword';
    END IF;

    -- Grant privileges (this is idempotent, so no need for existence check)
    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
END $$;