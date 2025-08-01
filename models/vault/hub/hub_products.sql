--models/vault/hub/hub_orders.sql

{{ config(
    schema='vault',
    materialized='incremental',
    unique_key='product_id',
    incremental_strategy='merge'
) }}
select
  {{ generate_hkey('product_id') }} as product_hk,
  product_id::varchar(200) as product_id,
  current_timestamp as load_dtm,
  'olist_files' as source
from {{ref('stg_products')}}
where
{{incremental_condition_not_in('product_id')}}