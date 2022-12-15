from datasette import hookimpl
from datasette.utils.asgi import Response

QUERIES_FOR_FIELD_TYPE = {
  bool: [
    ("SUM({})", "# True {}", ),
    ("COUNT({})", "Count {}", ),
  ],
  int: [
    ("SUM({})", "Sum {}", ),
    ("MIN({})", "Min {}", ),
    ("MAX({})", "Max {}", ),
    ("AVG({})", "Avg {}", ),
    ("COUNT({})", "Count {}", ),
    ("COUNT(DISTINCT {})", "Distinct {}", ),
  ], 
  "datetime": [ # TODO - # of unique years, months, etc
    ("MIN({})", "Min {}", ),
    ("MAX({})", "Max {}", ),
    ("AVG({})", "Avg {}", ),
  ],
  bytes: [
    ("COUNT({})", "Count {}", ),
    ("COUNT(DISTINCT {})", "Distinct {}", ),
    ("MAX(LENGTH({}))", "Max Length {}", ),
    ("MIN(LENGTH({}))", "Min Length {}", ),
  ],
}
QUERIES_FOR_FIELD_TYPE[float] = QUERIES_FOR_FIELD_TYPE[int]
QUERIES_FOR_FIELD_TYPE[str] = QUERIES_FOR_FIELD_TYPE[bytes]


def can_render_diagnostics(datasette, columns):
    return True


async def render_diagnostics(datasette, columns, rows, sql, table, request, database):
    if not can_render_diagnostics(datasette, columns):
        from datasette.views.base import DatasetteError
        raise DatasetteError("Insufficient data for running diagnostics.")

    column_types = [type(col) for col in rows[0]]
    selects = []
    diagnostic_queries = zip(columns, [QUERIES_FOR_FIELD_TYPE[t] for t in column_types])
    for name, queries in diagnostic_queries:
        for query, label in queries:
            selects.append(query.format(name) + " as \"" + label.format(name) + "\"")

    selects = ', '.join(selects)
    print("selects", selects)
    query = "SELECT {} FROM ({});".format(selects, sql)
    print ("query is", query)


    db = datasette.get_database(database)
    result = await db.execute(query);

    # package back up the results by column name
    diagnostics = {}
    i = 0;
    for cname, ctype in zip(columns, column_types):
        d = {}
        for query, label in QUERIES_FOR_FIELD_TYPE[ctype]:
            d[label.format(cname)] = result.rows[0][i]
            i += 1
        diagnostics[cname] = d
 
    return Response.html(
        await datasette.render_template(
            "diagnostics.html",{'diagnostics': diagnostics}, request=request, 
        )
    )

@hookimpl
def register_output_renderer(datasette):
    return {
        "extension": "diagnostics",
        "render": render_diagnostics,
        "can_render": can_render_diagnostics,  # Optional
    }



