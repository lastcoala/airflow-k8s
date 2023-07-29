from jinja2 import Environment, FileSystemLoader
from airflow.templates import FILTERS

def render_file(filepath, context):
    temp = filepath.split("/")
    dir = "/".join(temp[:-1])
    file = temp[-1]
    env = Environment(
        loader=FileSystemLoader(dir)
    )
    env.filters = {**env.filters, **FILTERS}

    template = env.get_template(file)
    result = template.render(**context)

    return result

def render_text(text, context):
    env = Environment()
    env.filters = {**env.filters, **FILTERS}
    template = env.from_string(text)
    result = template.render(**context)

    return result