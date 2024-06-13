import trino
from pystarburst import Session

db_parameters = {
    "host": "shaktigoyal-data-eng-s3b-demo-virginia.trino.galaxy.starburst.io",
    "port": 443,
    "http_scheme": "https",
    # Setup authentication through login or password or any other supported authentication methods
    # See docs: https://github.com/trinodb/trino-python-client#authentication-mechanisms
    "auth": trino.auth.BasicAuthentication("toshaktigoyal@gmail.com/accountadmin", "<password>")
}
session = Session.builder.configs(db_parameters).create()
session.sql("SELECT * FROM system.runtime.nodes").collect()
