import subprocess

# Run pip install command
def start_in_terminal():
    result = subprocess.run(["pip", "install", "neo4j"], capture_output=True, text=True)

    if result.returncode == 0:
        print("Installation successful!")
        print(result.stdout)
    else:
        print("Installation failed.")
        print(result.stderr)



from neo4j import GraphDatabase
uri = "bolt://localhost:7687" 
username = "neo4j" 
password = "password"  
driver = GraphDatabase.driver(uri, auth=(username, password))

def create_person(tx, name, age):
    # Create a node for a person
    tx.run("CREATE (p:Person {name: $name, age: $age})", name=name, age=age)

def create_relationship(tx, person1, person2):
    # Create a 'KNOWS' relationship between two people
    tx.run("""
        MATCH (a:Person {name: $person1}), (b:Person {name: $person2})
        CREATE (a)-[:KNOWS]->(b)
    """, person1=person1, person2=person2)

def get_people(tx):
    # Retrieve all people and their details
    result = tx.run("MATCH (p:Person) RETURN p.name AS name, p.age AS age")
    for record in result:
        print(f"{record['name']} is {record['age']} years old.")


def main():
    start_in_terminal()
    # Create a new session to interact with the database
    with driver.session() as session:
        # Create some Person nodes
        session.write_transaction(create_person, "Alice", 30)
        session.write_transaction(create_person, "Bob", 25)
        
        # Create a relationship
        session.write_transaction(create_relationship, "Alice", "Bob")
        
        # Get and print all people from the graph
        print("People in the graph:")
        session.read_transaction(get_people)

if __name__ == "__main__":
    main()
