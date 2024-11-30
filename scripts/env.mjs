import dotenv from 'dotenv';

dotenv.config();

const { DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE = 'test', DATABASE_URL } = process.env;
// Notice: When using TiDb Cloud Serverless Tier, you **MUST** set the following flags to enable tls connection.
const SSL_FLAGS = 'pool_timeout=60&sslaccept=accept_invalid_certs';

if(DB_USERNAME && DB_HOST && DB_PORT) {
    console.log(`mysql://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_DB_NAME}?${SSL_FLAGS}`);
} else {
    console.log(`${DATABASE_URL}?${SSL_FLAGS}`);
}