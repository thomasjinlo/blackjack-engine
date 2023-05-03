import pickle


class MyClass:

    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2


my_object = MyClass("value1", "value2")

# Serialize the object to a byte stream
serialized = pickle.dumps(my_object)

# Unserialize the byte stream to recreate the object
unserialized = pickle.loads(serialized)

print(unserialized.attribute1)  # Output: "value1"
print(unserialized.attribute2)  # Output: "value2"
