from datetime import datetime


def get_tools(database_schema_string: str, database_definitions: str) -> list[dict]:
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_sql_query_response",
                "description": "Use this function to answer user questions about Production data. Input should be a fully formed PostgreSQL query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": f'''Generate a PostgreSQL query to extract information based on a user's question. \
                        
# Parameters: \
- Database Schema: {database_schema_string} \
- Data Definitions: {database_definitions} \

# Instructions: \
- Construct an SQL query using only the tables and columns listed in the provided schema. \
- When comparing string use LIKE to maximise the search. \
- Ensure the query avoids assumptions about non-existent columns. \
- Consider performance and security best practices, such as avoiding SQL injection risks. \
- Format the query in plain text for direct execution in a PostgreSQL database. \
- Current Date: Use today's date as {datetime.now()} where needed in the query. \

# Example Query: \
# If the user asks for the number of employees in each department, the query should look like this: \
# "SELECT department_id, COUNT(*) FROM employees GROUP BY department_id;"'''
                        }
                    },
                    "required": ["query"],
                },
            }
        }
    ]

    return tools
