import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Credits to Harry")
    # command = f"say {x} "
    while(1):
        x = input("Enter what do you want me to pronounce : ")
        if(x != "q"):
            command = f"espeak {x} "
            os.system(command)
        else:
            print("Exiting...")
            os.system(" espeak 'bye bye friend'")
            break;
