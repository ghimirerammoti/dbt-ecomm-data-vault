--models/vault/hub/hub_customers.sql

{{ config(
    schema='vault',
    materialized='incremental',
    unique_key='customer_id',
    incremental_strategy='merge'
) }}
select
  {{ generate_hkey('customer_id') }} as customer_hk,
  customer_id::varchar(200) as customer_id,
  current_timestamp as load_dtm,
  'olist_files' as source
from {{ref('stg_customers')}}
where
{{incremental_condition_not_in('customer_id')}}