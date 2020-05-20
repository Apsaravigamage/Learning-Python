class pycham: # Duck typing in Polymorphism
    def execute(self):
        print("compiling")
        print("Running")

class Myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("Running")

class laptop:
    def code(self,ide):
        ide.execute()

ide=n=Myeditor()
lap1=laptop()
lap1.code(ide)

