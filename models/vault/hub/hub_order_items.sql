--models/vault/hub/hub_order_items.sql

{{ config(
    schema='vault',
    materialized='incremental',
    unique_key='order_item_id',
    incremental_strategy='merge'
) }}
select
  {{ generate_hkey('order_item_id') }} as order_item_hk,
  order_item_id::varchar(200) as order_item_id,
  current_timestamp as load_dtm,
  'olist_files' as source
from {{ref('stg_order_items')}}
where
{{incremental_condition_not_in('order_item_id')}}