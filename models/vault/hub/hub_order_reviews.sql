--models/vault/hub/hub_order_reviews.sql

{{ config(
    schema='vault',
    materialized='incremental',
    unique_key='review_id',
    incremental_strategy='merge'
) }}
select
  {{ generate_hkey('review_id') }} as review_hk,
  review_id::varchar(200) as review_id,
  current_timestamp as load_dtm,
  'olist_files' as source
from {{ref('stg_order_reviews')}}
where
{{incremental_condition_not_in('review_id')}}