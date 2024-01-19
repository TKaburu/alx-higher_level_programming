#!/usr/bin/python3

"""
Display values in the states table where name matches the provided argument
"""

import MySQLdb
import sys

def display_states(username, password, database, state_name):
    """
    Connects to the database and displays values in the states table
    where the name matches the provided argument.
    """

    # SQL query template with placeholders
    query_template = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"

    # Create a formatted query with user input
    query = query_template.format(state_name)

    # Connect to the database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL command to retrieve states
    cursor.execute(query)
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        sys.exit(1)

    # Get arguments from the command line
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    display_states(username, password, database, state_name)

