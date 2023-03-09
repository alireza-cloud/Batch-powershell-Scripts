# Print out SQL Queries for a certain table for n number of times
n = 1200
for x in range (n):
    Column_1, Column_2, Column_3= input().split()
    #print(f"Update Endpoints set Path = '{lat}' Address='{long}' Name='{long}' Channel='{long}' BaudRate='{long}' WHERE BasestationId = '{x+1}'")
    print(f"INSERT INTO Table_name (Column_1, Column_2, Column_3) VALUES (1, '{Column_1}', {Column_2}, '{Column_3}');")
