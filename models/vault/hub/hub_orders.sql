--models/vault/hub/hub_orders.sql

{{ config(
    schema='vault',
    materialized='incremental',
    unique_key='order_id',
    incremental_strategy='merge'
) }}
select
  {{ generate_hkey('order_id') }} as order_hk,
  order_id::varchar(200) as order_id,
  current_timestamp as load_dtm,
  'olist_files' as source
from {{ref('stg_orders')}}
where
{{incremental_condition_not_in('order_id')}}