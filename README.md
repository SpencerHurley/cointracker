1. Set up environment

`source env/bin/activate`

2. Install requirements

`pip install -r requirements.txt`

3. Start server

`flask run`


4. Assumptions:

For the scope of this project, I assumed that all data could be stored in-memory, without needing
to spin up a database to store address info. Given more time I would have set up a SQL-like database
with an address info entity, storing current balance and a last_updated timestamp, and a transaction entity
storing `hash`, `size`, `relayed_by`, `block_height`, `tx_index`, `inputs` and `outputs` to capture the output of the blockchain.info API details on transactions for an address.


There are 4 endpoints in this server-side implementation:

`POST /addresses/:address` will query the blockchain.info API for balance and transaction data for this address 
and store the result in local memory, returning a subset of blockchain.info's API response

`DELETE /addresses/:address` will delete the given address and its balance // transactions from the in-memory store

`POST /addresses/:address/synchronize` will update the in-memory information for an address from the blockchain.info API. 
Currently works with one address at a time, could expand functionality in the future to allow for several addresses to be batch-updated
for some cron job implementation of background synchronization. Functionality of this endpoint is currently identical to the `POST /addresses/:address` endpoint.

`GET /addresses/:address` will return the in-memory info on a particular address's balance and transactions, has the potential to
be out-of-sync with the blockchain. Made the assumption that a single endpoint could serve to retrieve an address's balance and transactions. 
Could be split into 2 separate endpoints for balance and transactions to lighten the load when querying for info on wallets with many tx's. 

