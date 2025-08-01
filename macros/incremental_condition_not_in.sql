--macros/incremental_condition_not_in.sql
{%- macro incremental_condition_not_in(columns) -%}
({% for col in columns %}
    {{ col }} 
    {% if not loop.last %},{% endif %}
{% endfor %})
    not in (
    select 
        {% for col in columns %}
        {{ col }} 
        {% if not loop.last %},{% endif %}
        {% endfor %} 
        from {{ this }})
{%- endmacro -%} 