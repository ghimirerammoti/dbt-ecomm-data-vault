--macros/generate_hkey.sql
{%- macro generate_hkey(columns) -%}
   encode(digest(
      {% for col in columns %}
         {{col}}
         {% if not loop.last %}||{% endif %}
      {% endfor %}
         ,'sha256'),'hex')
{%- endmacro -%}