
def calendar_output():
    width = 30
    row = 166
    Day = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    client = ""
    
    print(f"-"*row)
    print(f"""|{Day[0]}{" "*(width+2-len(Day[0]))}|{Day[1]}{" "*(width+2-len(Day[1]))}|{Day[2]}{" "*(width+2-len(Day[2]))}|{Day[3]}{" "*(width+2-len(Day[3]))}|{Day[4]}{" "*(width+2-len(Day[4]))}|""")
    print(f"-"*row)
    print(f"""|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|""")
    print(f"""|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|""")
    print(f"""|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"-"*row)
    print(f"""|{Day[0]}{" "*(width+2-len(Day[0]))}|{Day[1]}{" "*(width+2-len(Day[1]))}|{Day[2]}{" "*(width+2-len(Day[2]))}|{Day[3]}{" "*(width+2-len(Day[3]))}|{Day[4]}{" "*(width+2-len(Day[4]))}|""")
    print(f"-"*row)
    print(f"""|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|""")
    print(f"""|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|""")
    print(f"""|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"-"*row)
    print(f"""|{Day[0]}{" "*(width+2-len(Day[0]))}|{Day[1]}{" "*(width+2-len(Day[1]))}|{Day[2]}{" "*(width+2-len(Day[2]))}|{Day[3]}{" "*(width+2-len(Day[3]))}|{Day[4]}{" "*(width+2-len(Day[4]))}|""")
    print(f"-"*row)
    print(f"""|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|""")
    print(f"""|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|""")
    print(f"""|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"-"*row)
    print(f"""|{Day[0]}{" "*(width+2-len(Day[0]))}|{Day[1]}{" "*(width+2-len(Day[1]))}|{Day[2]}{" "*(width+2-len(Day[2]))}|{Day[3]}{" "*(width+2-len(Day[3]))}|{Day[4]}{" "*(width+2-len(Day[4]))}|""")
    print(f"-"*row)
    print(f"""|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|ID:{" "*(31-2)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|Host:{" "*(31-4)}|""")
    print(f"""|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|{client}{" "*(width+2-len(client))}|""")
    print(f"""|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|Attendee:{" "*(31-8)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|Campus:{" "*(31-6)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|Time:{" "*(31-4)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"""|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|Status:{" "*(31-6)}|""")
    print(f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|",f" "*width,f"|")
    print(f"-"*row)


if __name__ == "__main__":
    calendar_output()