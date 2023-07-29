from sources.base import Source

class PostgresSource(Source):

    template_fields = ("sql", )

    def __init__(self, sql, *args, **kwargs):
        super(PostgresSource, self).__init__(*args, **kwargs)

        self.sql = sql
    
    def get(self, context, *args, **kwargs):
        self.render(**context)
        print(self.sql)