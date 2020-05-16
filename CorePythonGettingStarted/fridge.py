from contextlib import closing

class RefrigeratorRaider:

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print(f"Find {food}...")
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print(f"Taking {food}")

    def close(self):
        print("Close fridge door.")

def raid(food):
    # r = RefrigeratorRaider()
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        # r.close()

# from fridge import raid
# raid('bacon')
# raid('deep fried pizza')

# from fridge import raid
# raid('spam')