from P4 import P4,P4Exception    # Import the module
p4 = P4()                        # Create the P4 instance
p4.port = "1666"
p4.user = "fred"
p4.client = "fred-ws"            # Set some environment variables

try:                             # Catch exceptions with try/except
  p4.connect()                   # Connect to the Perforce server
  info = p4.run( "info" )        # Run "p4 info" (returns a dict)
  for key in info[0]:            # and display all key-value pairs
    print key, "=", info[0][key]
  p4.run( "edit", "file.txt" )   # Run "p4 edit file.txt"
  p4.disconnect()                # Disconnect from the server
except P4Exception:
  for e in p4.errors:            # Display errors
      print e

def main():
