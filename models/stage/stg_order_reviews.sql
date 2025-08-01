-- models/staging/stg_order_reviews.sql
select
  review_id::varchar(200) as review_id,
  order_id::varchar(200) as order_id,
  review_score::int as review_score,
  review_comment_title::varchar(1000) as review_comment_title,
  review_comment_message::text as review_comment_message,
  review_creation_date::timestamp as review_creation_date,
  review_answer_timestamp::timestamp as review_answer_timestamp
from {{ source('raw','raw_order_reviews') }}