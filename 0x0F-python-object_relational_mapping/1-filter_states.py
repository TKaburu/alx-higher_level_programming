#!/usr/bin/python3


"""
List the states in hbtn_0e_0_usa whose name start with N
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    This function connects to database and lists all the states
    """

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL command to retrieve states starting with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        sys.exit(1)

    # Get arguments from command line
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states
    list_states(username, password, database)
