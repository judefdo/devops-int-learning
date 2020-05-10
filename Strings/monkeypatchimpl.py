import monkeypatch
def printme(self):
    print("fernando")

monkeypatch.Test.meprint=printme
obj=monkeypatch.Test()
obj.meprint()