-- models/staging/stg_order_payments.sql
select
  order_id::varchar(200) as order_id,
  payment_sequential::int as payment_sequential,
  payment_type::varchar(20) as payment_type,
  payment_installments::int as payment_installments,
  payment_value::decimal(20,2) as customer_state
from {{ source('raw','raw_order_payments') }}