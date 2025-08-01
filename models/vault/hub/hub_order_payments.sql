--models/vault/hub/hub_order_payments.sql

{{ config(
    schema='vault',
    materialized='incremental',
    unique_key='order_id,payment_sequential',
    incremental_strategy='merge'
) }}
select
  {{ generate_hkey(['order_id','payment_sequential']) }} as order_payment_hk,
  order_id::varchar(200) as order_id,
  payment_sequential::int as payment_sequential,
  current_timestamp as load_dtm,
  'olist_files' as source
from {{ref('stg_order_payments')}}
where
{{incremental_condition_not_in(['order_id', 'payment_sequential'])}}