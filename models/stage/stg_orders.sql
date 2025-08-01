-- models/staging/stg_orders.sql
select
  order_id::varchar(200) as order_id,
  customer_id::varchar(200) as customer_id,
  order_status::varchar(20) as order_status,
  order_purchase_timestamp ::timestamp as order_purchase_timestamp,
  order_approved_at::timestamp as order_approved_at,
  order_delivered_carrier_date::timestamp as order_delivered_carrier_date,
  order_delivered_customer_date::timestamp as order_delivered_customer_date,
  order_estimated_delivery_date::timestamp as order_estimated_delivery_date
from {{ source('raw','raw_orders') }}