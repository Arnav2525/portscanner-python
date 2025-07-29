from neo4j import GraphDatabase

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "Himanshu@07"

def get_discovered_ips():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    ips = []
    with driver.session() as session:
        result = session.run("MATCH (ip:IP) RETURN ip.address AS address")
        ips = [record["address"] for record in result]
    driver.close()
    return ips
