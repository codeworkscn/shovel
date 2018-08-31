
from P4 import P4, P4Exception
from shovel.config import ShovelConfig

def p4integrate():
  p4 = P4()          
  p4Config = ShovelConfig.get_configs_by_section("P4")

  p4.host = p4Config["host"]
  p4.user = p4Config["user"]
  p4.password = p4Config["passwd"]
  p4.client =p4Config["client"]

  try:      
    print("p4 connect start")                       
    p4.connect()           
    print("p4 connect done")

    info = p4.run( "info" )
    print("info : " + str(info))     

    p4.disconnect()       
    print("p4 disconnect")         
  except P4Exception as e:
    print("P4Exception: " + str(e))    
    for e in p4.errors:            
        print(e)
  except Exception  as e:
    print("Exception: " + str(e))       

