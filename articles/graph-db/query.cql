CREATE (p:Person {name: 'Alice', age: 30})
CREATE (p:Person {name: 'Bob', age: 25})


MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
CREATE (a)-[:KNOWS]->(b)

MATCH (p:Person)
RETURN p.name, p.age

MATCH (p:Person {name: 'Alice'})
SET p.age = 31

MATCH (p:Person {name: 'Bob'})
DELETE p

MATCH (p:Person)
WHERE p.age > 30
RETURN p.name, p.age

MATCH (p:Person)
RETURN AVG(p.age) AS average_age

MATCH (a:Person)-[:KNOWS]->(b:Person)
RETURN a.name, b.name


// Creates an index on the name property of Person nodes to improve query performance.
CREATE INDEX ON :Person(name)

