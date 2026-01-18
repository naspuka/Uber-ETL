{{
    config(
        materialized='incremental',
        unique_key=['pickup_date', 'time_of_day'],
        file_format='delta'
    )
}}

with silver as (
    select * from {{source('silver', 'yellow_tripdata')}}
    {% if is_incremental() %}
        where pickup_date > (select max(pickup_date) from {{ this }})
    {% endif %}
)

select
    pickup_date,
    time_of_day,
    count(*) as total_trips,
    round(avg(trip_duration_minutes)/60, 2) as avg_trip_duration_min,
    round(avg(fare_amount), 2) as avg_fare
from silver
group by pickup_date, time_of_day