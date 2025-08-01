-- models/staging/stg_customers.sql
select
  customer_id::varchar(200) as customer_id,
  customer_unique_id::varchar(200) as customer_unique_id,
  customer_zip_code_prefix::int as customer_zip_code_prefix,
  customer_city::varchar(100) as customer_city,
  customer_state::varchar(10) as customer_state
from {{ ref('olist_customers_dataset') }}