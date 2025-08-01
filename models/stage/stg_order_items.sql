-- models/staging/stg_order_items.sql
select
  order_id::varchar(200) as order_id,
  order_item_id::varchar(200) as order_item_id,
  product_id::varchar(200) as product_id,
  seller_id::varchar(200) as seller_id,
  shipping_limit_date::timestamp as shipping_imit_date,
  price::decimal(10,2) as price,
  freight_value::decimal(10,2) as freight_value
from {{ source('raw','raw_order_items') }}