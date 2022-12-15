from datasette import hookimpl
from datasette.utils.asgi import Response

QUERIES_FOR_FIELD_TYPE = {
  "null": [
  ],
  "integer": [
    ("COUNT({})", "Count {}", ),
    ("COUNT(DISTINCT {})", "Distinct {}", ),
    ("SUM({})", "Sum {}", ),
    ("MIN({})", "Min {}", ),
    ("MAX({})", "Max {}", ),
    ("AVG({})", "Avg {}", ),
  ], 
  "blob": [
    ("COUNT({})", "Count {}", ),
    ("COUNT(DISTINCT {})", "Distinct {}", ),
    ("MAX(LENGTH({}))", "Max Length {}", ),
    ("MIN(LENGTH({}))", "Min Length {}", ),
  ],
}
QUERIES_FOR_FIELD_TYPE["real"] = QUERIES_FOR_FIELD_TYPE["integer"]
QUERIES_FOR_FIELD_TYPE["text"] = QUERIES_FOR_FIELD_TYPE["blob"]


def can_render_diagnostics(datasette, columns):
    return True


async def render_diagnostics(datasette, columns, rows, sql, table, request, database):
    if not can_render_diagnostics(datasette, columns):
        from datasette.views.base import DatasetteError
        raise DatasetteError("Insufficient data for running diagnostics.")

    db = datasette.get_database(database)
    # Note - it's faster and potentially just as reliable to get column types from the first row:
    # column_types = [type(col) for col in rows[0]]  
    column_types_query = "SELECT {} FROM ({});".format(', '.join('typeof({})'.format(col) for col in columns), sql)
    result = await db.execute(column_types_query);
    column_types = result.first()
    
    selects = []
    diagnostic_queries = zip(columns, [QUERIES_FOR_FIELD_TYPE[t] for t in column_types])
    for name, queries in diagnostic_queries:
        for query, label in queries:
            selects.append(query.format(name) + " as \"" + label.format(name) + "\"")

    selects = ', '.join(selects)
    query = "SELECT {} FROM ({});".format(selects, sql)
    result = await db.execute(query);

    # package back up the results by column name
    diagnostics = {}
    i = 0;
    for cname, ctype in zip(columns, column_types):
        d = []
        for query, label in QUERIES_FOR_FIELD_TYPE.get(ctype, ()):
            d.append((label.format(cname), result.rows[0][i]))
            i += 1
        diagnostics[cname] = d
 
    return Response.html(
        await datasette.render_template(
            "diagnostics.html", {'diagnostics': diagnostics, 'column_types': column_types}, request=request, 
        )
    )

@hookimpl
def register_output_renderer(datasette):
    return {
        "extension": "diagnostics",
        "render": render_diagnostics,
        "can_render": can_render_diagnostics,  # Optional
    }



