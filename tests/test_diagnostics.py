from datasette.app import Datasette
import pytest
import sqlite3

@pytest.mark.asyncio
async def test_plugin_is_installed():
    datasette = Datasette(memory=True)
    response = await datasette.client.get("/-/plugins.json")
    assert response.status_code == 200
    installed_plugins = {p["name"] for p in response.json()}
    assert "datasette-diagnostics" in installed_plugins


@pytest.fixture(scope="session")
def datasette(tmp_path_factory):
    db_directory = tmp_path_factory.mktemp("dbs")
    db_path = db_directory / "test.db"
    
    import sqlite3
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE everytype (
        id INTEGER PRIMARY KEY,
        text_column TEXT,
        real_column REAL,
        integer_column INTEGER,
        blob_column BLOB
    )
    ''')

    # insert 50 rows of data into the example table
    for i in range(1, 51):
        cursor.execute('''
            INSERT INTO everytype (text_column, real_column, integer_column, blob_column)
            VALUES (?, ?, ?, ?)
    ''', (f'Row {i}', i / 2, i, bytes(i)))

    conn.commit()
    cursor.close()
    conn.close()

    datasette = Datasette(
        [db_path],
        metadata={
            "databases": {
                "test": {
                    "tables": {
                        "everytype": {"title": "A column for every type"}
                    }
                }
            }
        },
        pdb=True,
    )
    return datasette


@pytest.mark.asyncio
async def test_example_table_json(datasette):
    response = await datasette.client.get(
        "/test/everytype.json?_shape=array"
    )
    assert response.status_code == 200
    assert len(response.json()) == 50
    assert list(dict(response.json()[0]).keys()) == ['id', 'text_column', 'real_column', 'integer_column', 'blob_column']


@pytest.mark.asyncio
async def test_example_table_html(datasette):
    response = await datasette.client.get("/test/everytype")
    assert ">A column for every type</h1>" in response.text

