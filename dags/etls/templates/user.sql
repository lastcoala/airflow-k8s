{% extends "base.sql" %}

{% block cond %}select * from user where updated_at = "{{ ds }}"{% endblock %}