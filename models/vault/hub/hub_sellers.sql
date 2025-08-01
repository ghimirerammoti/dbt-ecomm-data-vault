--models/vault/hub/hub_orders.sql

{{ config(
    schema='vault',
    materialized='incremental',
    unique_key='customer_id',
    incremental_strategy='merge'
) }}
select
  {{ generate_hkey('seller_id') }} as seller_hk,
  seller_id::varchar(200) as seller_id,
  current_timestamp as load_dtm,
  'olist_files' as source
from {{ref('stg_sellers')}}
where
{{incremental_condition_not_in('seller_id')}}