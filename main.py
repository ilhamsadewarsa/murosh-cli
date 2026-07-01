import sys , json , random , os
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)
args = sys.argv
sh = "murosh:"
EMPTYLIST = []
EMPTYSTRING = ""
SPACE = " "
donePath = Path('done.json')
undonePath = Path('undone.json')
ongoingPath = Path('ongoing.json')
def config():
    if not donePath.exists():
        donePath.write_text(str(EMPTYLIST))
    if not undonePath.exists():
        undonePath.write_text(str(EMPTYLIST))
    if not ongoingPath.exists():
        ongoingPath.write_text(str(EMPTYLIST))

def load():
    config()
    global done , undone , ongoing
    with open("done.json","r") as f:
        done = json.load(f)
    with open("undone.json","r") as f:
        undone = json.load(f)
    with open("ongoing.json","r") as f:
        ongoing = json.load(f)
    return
def update():
    global done , undone , ongoing
    if undone + ongoing is EMPTYLIST:
        undone = done[:]
        done.clear()
    with open("done.json","w") as f:
        json.dump(done,f)
    with open("undone.json","w") as f:
        json.dump(undone,f)
    with open("ongoing.json","w") as f:
        json.dump(ongoing,f)
    return
    
def add(spec):
    global undone , done , ongoing
    if len(spec) == 0:
        name = None
        while not name is EMPTYSTRING:
            name = input()
            if name in undone or name in done or name in ongoing:
                print(f"{name} already existing")
            if not name is EMPTYSTRING:
                undone.append(name)
        print("titles added to undone group")
        return
    if len(spec) == 1:
        print("enter murosh add to add multiple titles to undone, or murosh add [group] [name] to add a single title to a spesific group")
        return
    group , name = spec[0] , spec[1]
    if name in undone or name in done or name in ongoing:
        print(f"{name} already existing")
        return
    match group:
        case "undone":
            undone.append(name)
        case "done":
            undone.append(name)
        case _:
            print("group not founded")
            return
    print(f"{name} was added to {group}")
    return

    
def remove(spec):
    global done , undone , ongoing
    name = spec[0] if len(spec) > 0 else []
    if name in done:
        done.remove(name)
    elif name in undone:
        undone.remove(name)
    else:
        print(f"{name} not existed")
        return
    print(f"{name} was removed")
    return

def show(spec):
    global done , undone , ongoing 
    group = spec[0] if len(spec) > 0 else []
    if group == "done":
        print("done >", done)
    elif group == "undone":
        print("undone >", undone)
    elif group == "ongoing":
        print("ongoing >", ongoing)
    else:
        print("group not founded")
    return

def check(spec):
    global done , undone , ongoing
    if len(spec) == 0:
        print("interactive check")
        return
    name = spec[0]
    if name in done:
        print(f"{name} was done")
        return
    if name in undone:
        done.append(name)
        undone.remove(name)
    elif name in ongoing:
        done.append(name)
        ongoing.remove(name)
    else:
        print(f"{name} not existed")
        return
    print(f"{name} -> done")
    return
        

def read(spec):
    global done , undone , ongoing
    if len(spec) == 0:
        print("interactive read")
        return
    name = spec[0]
    if name == "random":
        toread = undone[:]
        number = int(spec[1]) if len(spec) > 2 else 1
        number = min(number,len(toread))
        random.shuffle(toread)
        toread = toread[0:number]
        ongoing += toread
        for name in toread:
            undone.remove(name)
        print(toread,"-> on going")
        return
    if name in done:
        print(f"{name} was done")
        return
    elif name in ongoing:
        print(f"{name} was on going")
        return
    elif name in undone:
        ongoing.append(name)
        undone.remove(name)
    else:
        print(f"{name} not existed")
        return
    print(f"{name} -> ongoing")
    return

def main():
    
    load()
    args = sys.argv
    caller = args[0] if len(args) > 0 else EMPTYSTRING
    command = args[1] if len(args) > 1 else EMPTYSTRING 
    spec = args[2:] if len(args) > 1 else EMPTYLIST
    print(sh,end = SPACE)
    if len(args) <= 1:
        print("welcome to murosh")
    else:
        match command:
            case "add":
                add(spec)
            case "remove":
                remove(spec)
            case "show":
                show(spec)
            case "check":
                check(spec)
            case "read":
                read(spec)
            case _:
                print("command not found")
    update()
    exit
        
        
