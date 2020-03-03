import struct
import pickle

"""Use select python module to handle many selections at once
"""

"""A Key Value Store

Project for the Bradfield of Computer Science school
"""

class KeyValueStore:
    def get(self, key: str) -> str:
        """Loads the value from store and returns the value
        """

        store = pickle.load( open( "store.pickle", "rb" ) )
        return store.get(key, -1)

    def set(self, key: str, value: str) -> None:
        """Sets the key value pair in memory
        """     

        try:
            store = pickle.load( open( "store.pickle", "rb" ) )
        except FileNotFoundError:
            store = {}
        store[key] = value
        pickle.dump( store, open( "store.pickle", "wb" ) )
    
    def validate_input_set(self, user_input: str) -> bool:
        values = user_input.split(" ")
        if len(values) != 2:
            print("Error: Invalid arguments")
            return False
        if "=" not in values[1]:
            print("Error: no equal sign in setter")
            return False
        return True

    def validate_input_get(self, user_input: str) -> bool:
        values = user_input.split(" ")
        if len(values) != 2:
            print("Error: Invalid arguments")
            return False
        return True

if __name__ == "__main__":
    store = KeyValueStore()
    print("Store initiated")
    while True:
        user_input = input()
        inputs = user_input.split(" ")
        if inputs[0].startswith("set"):
            if not store.validate_input_set(user_input):
                continue
            key, val = inputs[1].split("=")
            store.set(key, val)
        elif inputs[0].startswith("get"):
            if not store.validate_input_get(user_input):
                continue            
            result = store.get(inputs[1])
            print(result)
        else:
            print(
                "Invalid input, please " +
                "input a message set foo=bar \n" +
                "or get foo"
            )


