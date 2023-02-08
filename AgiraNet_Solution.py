class Node:
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type
        self.strength = None
        self.adjacent_nodes = set()

class Network:
    def __init__(self):
        self.devices = {}

    def add_device(self, name, device_type):
        if device_type != "COMPUTER" and device_type != "REPEATER":
            return "Error: Invalid command syntax."
        
        if name in self.devices:
            return f"Error: That name already exists."
        
        self.devices[name] = Node(name, device_type)
        
        return f"Successfully added {name}."
    
    def set_device_strength(self, name, strength):
        
        if name not in self.devices:
            return "Error: Device not found."
            
        if not strength.isdigit():
            return "Error: Invalid command syntax."

        strength = int(strength)
        
        self.devices[name].strength = strength
        
        return "Successfully defined strength."

    def connect(self, name1, name2):
        if name1 not in self.devices or name2 not in self.devices:
            return "Error: Node not found."
        
        if name1 == name2:
            return "Error: Cannot connect device to itself."
        
        if self.devices[name2] in self.devices[name1].adjacent_nodes:
            return "Error: Devices are already connected."
        
        self.devices[name1].adjacent_nodes.add(self.devices[name2])
        self.devices[name2].adjacent_nodes.add(self.devices[name1])
        return "Successfully connected."
    
    def info_route(self, name1, name2):
        if name1 not in self.devices or name2 not in self.devices:
            return "Error: Node not found."
        
        if self.devices[name1].device_type == "REPEATER" or self.devices[name2].device_type == "REPEATER":
            return "Error: Route cannot be calculated with a repeater."
    
        if name1 == name2:
            return f"{name1} -> {name2}"
            
        queue = [(self.devices[name1], [])]
        visited = set()
        while queue:
            node, path = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            path = path + [node.name]
            if node == self.devices[name2]:
                return " -> ".join(path)
            for neighbor in node.adjacent_nodes:
                queue.append((neighbor, path))
        return "Error: Route not found!"
    
        
    
    def parse_command(self, command):

        parts = command
        
        if parts[0] == "ADD":
            type, name = parts[1], parts[2]
            return network.add_device(name, type)
            
        elif parts[0] == "CONNECT":
            c1, c2 = parts[1], parts[2]
            return network.connect(c1, c2)
        
        elif parts[0] == "INFO_ROUTE":
            dev1, dev2 = parts[1], parts[2]
            return network.info_route(dev1, dev2)
        
        elif parts[0] == "SET_DEVICE_STRENGTH":
            name, strength = parts[1], parts[2]
            return network.set_device_strength(name, strength)
            
        else:
            return "Error: Invalid command syntax."
      
                
            
            
if __name__ == '__main__':
    
    network = Network()
    
    while True:
        command = input('> ').strip().split()

        if len(command)==1 and command[0] == 'QUIT' :
            break
        
        if len(command) !=3 :
            print("Error: Invalid command syntax.")
        else :
            result = network.parse_command(command)
            print(result)
        

        
        