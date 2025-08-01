-- models/staging/stg_sellers.sql
select
  seller_id::varchar(200) as seller_id,
  seller_zip_code_prefix::int as seller_zip_code_prefix,
  seller_city::varchar(200) as seller_city,
  seller_state ::varchar(4) as seller_state
from {{ source('raw','raw_sellers') }}