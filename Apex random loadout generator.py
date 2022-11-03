from cProfile import label
from curses import window
from decimal import HAVE_CONTEXTVAR
from glob import glob
from multiprocessing.sharedctypes import Value
import random as random
from sqlite3 import Row
import string
import tkinter as tkinter
from tkinter import *
from tkinter.tix import COLUMN
from tokenize import group


Window = tkinter.Tk()
Window.geometry("800x500")
Window.title("Apex Loadout Randommiser")


Gun_Attachments_Mags = [
    "Mag Level 1", 
    "Mag Level 2", 
    "Mag Level 3",
    "Mag Level 4"
]

Gun_Attachments_AR_Optics = [
    "1x HCOG",
    "1x Holo",
    "1x-2x Holo",
    "2x HCOG",
    "2x-4x AOG",
    "3x HCOG"
]

Gun_Attachments_SMG_Optics = [
    "1x HCOG",
    "1x Holo",
    "1x-2x Holo",
    "2x HCOG",
    "1x Digi Threat"
]

Gun_Attachments_Stock = [
    "Stock Level 1",
    "Stock Level 2",
    "Stock Level 3"
]

Gun_Attachments_Barrel_Stabilizer = [
    "Barrel Stabilizer Level 1",
    "Barrel Stabilizer Level 2",
    "Barrel Stabilizer Level 3"
]

Gun_Attachments_Laser_Sight = [
    "Laser Sight Level 1",
    "Laser Sight Level 2",
    "Laser Sight Level 3"
]

Gun_Attachments_Turbocharger = [
    "None",
    "Turbocharger"
]

Gun_Attachments_Boosted_Loader = [
    "None",
    "Boosted Loader"
]

Gun_attachments_Double_Tap = [
    "None",
    "Douple Tap"
]

Apex_Wapons = [
    "Havoc",
    "Flatline",
    "Hemlock",
    "R-301",
    "Alternator",
    "Prowler",
    "R_99",
    "Volt",
    "Car",
    "Devotion",
    "L-Star",
    "Spitfire",
    "Scout",
    "Triple Take",
    "30-30",
    "Charge Rifle",
    "Longbow",
    "Senttinel",
    "Eva-8",
    "Mozambique",
    "Peacekeeper",
    "Re-45",
    "P2020",
    "Wingman"
]

Apex_Wapons_Test = [
    "Havoc",
    "Flatline",
    "Hemlock",
    "R-301"
]

Apex_Wapons_Red = [
    "Havoc",
    "Flatline",
    "Hemlock",
    "R-301",
    "Alternator",
    "Prowler",
    "R-99",
    "Volt",
    "Car",
    "Devotion",
    "L-Star",
    "Spitfire",
    "Scout",
    "Triple Take",
    "30-30",
    "Charge Rifle",
    "Longbow",
    "Senttinel",
    "Eva-8",
    "Mozambique",
    "Peacekeeper",
    "Re-45",
    "P2020",
    "Wingman",
    "Rampage",
    "Bocek",
    "Kraber",
    "Mastiff",
    "Knife"
]

Assault_Rifles = [
    "Havoc",
    "Flatline",
    "Hemlock",
    "R-301"
]

Sub_Machine_Guns = [
    "Alternator",
    "Prowler",
    "R-99",
    "Volt",
    "Car"
]

Light_Machine_Guns = [
    "Devotion",
    "L-Star",
    "Spitfire"
]

Marksman_Wapons = [
    "Scout",
    "Triple Take",
    "30-30"
]

Sniper_Rifles = [
    "Charge Rifle",
    "Longbow",
    "Senttinel"
]

Shotguns = [
    "Eva-8",
    "Mozambique",
    "Peacekeeper"
]

Pistols = [
    "Re-45",
    "P2020",
    "Wingman"
]

Red_Wapons = [
    "Rampage",
    "Bocek",
    "Kraber",
    "Mastiff",
    "Knife"
]

Apex_Legends = [
    "Ash",
    "Bangalore",
    "Fuse",
    "Horizon",
    "Mad Maggie",
    "Mirage",
    "Octane",
    "Revenant",
    "Wraith",
    "Caustic",
    "Gibraltar",
    "Newcastle",
    "Rampart",
    "Wattson",
    "Lifeline",
    "Loba",
    "Bloodhound",
    "Crypto",
    "Pathfinder",
    "Seer",
    "Valkyrie",
    "Vantage"
]

barrel_stabs = ["none", "1", "2", "3", "4"]
hop_ups = [["none", "doubletap"], ["none", "choke"], [
    "none", "hammerpoint"], ["none", "selectfire"], ["none", "skullpiercer"]]
mags_bolts_stocks = ["none", "1", "2", "3"]
optics = {
    "sniper":
     ["none", "1xholo", "classic", "1x2xvar", "bruiser", "6x", "ranger", "2x4xaog", "4x8x", "digi"],
    "lmg_ar": [
    "none", "1xholo", "classic", "1x2xvar", "bruiser", "ranger", "2x4xaog"],
    "sg_smg_pist": 
    ["none", "1xholo", "classic", "1x2xvar", "bruiser", "digi"]}


def Havoc(event):
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_AR_Optics)
    random.choice(Gun_Attachments_Stock)
    random.choice(Gun_Attachments_Turbocharger)

Havoc_Attachments = [Gun_Attachments_Mags, Gun_Attachments_AR_Optics, Gun_Attachments_Stock, Gun_Attachments_Turbocharger]

def Flatline(event):
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_AR_Optics)
    random.choice(Gun_Attachments_Stock)

Flatline_Attachments = [Gun_Attachments_Mags, Gun_Attachments_AR_Optics, Gun_Attachments_Stock]

def Hemlock(event):
    random.choice(Gun_Attachments_Barrel_Stabilizer)
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_AR_Optics)
    random.choice(Gun_Attachments_Stock)
    random.choice(Gun_Attachments_Boosted_Loader)

Hemlock_Attachments = [Gun_Attachments_Barrel_Stabilizer, Gun_Attachments_Mags, Gun_Attachments_AR_Optics, Gun_Attachments_Stock, Gun_Attachments_Boosted_Loader]

def R_301(event):
    random.choice(Gun_Attachments_Barrel_Stabilizer)
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_AR_Optics)
    random.choice(Gun_Attachments_Stock)

R_301_Attachments = [Gun_Attachments_Barrel_Stabilizer, Gun_Attachments_Mags, Gun_Attachments_AR_Optics, Gun_Attachments_Stock]

def Alternator(event):
    random.choice(Gun_Attachments_Laser_Sight)
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_SMG_Optics)
    random.choice(Gun_Attachments_Stock)

Alternator_Attachments = [Gun_Attachments_Laser_Sight, Gun_Attachments_Mags, Gun_Attachments_SMG_Optics, Gun_Attachments_Stock]

def Prowler(event):
    random.choice(Gun_Attachments_Laser_Sight)
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_SMG_Optics)
    random.choice(Gun_Attachments_Stock)

Prowler_Attachments = [Gun_Attachments_Laser_Sight, Gun_Attachments_Mags, Gun_Attachments_SMG_Optics, Gun_Attachments_Stock]

def R_99(event):
    random.choice(Gun_Attachments_Laser_Sight)
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_SMG_Optics)
    random.choice(Gun_Attachments_Stock)

R_99_Attachments = [Gun_Attachments_Laser_Sight, Gun_Attachments_Mags, Gun_Attachments_SMG_Optics, Gun_Attachments_Stock]

def Volt(event):
    random.choice(Gun_Attachments_Laser_Sight)
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_SMG_Optics)
    random.choice(Gun_Attachments_Stock)

Volt_Attachments = [Gun_Attachments_Laser_Sight, Gun_Attachments_Mags, Gun_Attachments_SMG_Optics, Gun_Attachments_Stock]

def Car(event):
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_SMG_Optics)
    random.choice(Gun_Attachments_Stock)

Car_Attachments = [Gun_Attachments_Mags, Gun_Attachments_SMG_Optics, Gun_Attachments_Stock]

def Devotion(event):
    random.choice(Gun_Attachments_Barrel_Stabilizer)
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_AR_Optics)
    random.choice(Gun_Attachments_Stock)
    random.choice(Gun_Attachments_Turbocharger)

Devotion_Attachments = [Gun_Attachments_Barrel_Stabilizer, Gun_Attachments_Mags, Gun_Attachments_AR_Optics, Gun_Attachments_Stock, Gun_Attachments_Turbocharger]

def L_Star(event):
    random.choice(Gun_Attachments_Barrel_Stabilizer)
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_AR_Optics)
    random.choice(Gun_Attachments_Stock)

L_Star_Attachments = [Gun_Attachments_Barrel_Stabilizer, Gun_Attachments_Mags, Gun_Attachments_AR_Optics, Gun_Attachments_Stock]

def Spitfire(event):
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_AR_Optics)
    random.choice(Gun_Attachments_Stock)

Spitfire_Attachments = [Gun_Attachments_Mags, Gun_Attachments_AR_Optics, Gun_Attachments_Stock]

def Scout(event):
    random.choice(Gun_Attachments_Barrel_Stabilizer)
    random.choice(Gun_Attachments_Mags)
    random.choice(Gun_Attachments_AR_Optics)
    random.choice(Gun_Attachments_Stock)
    random.choice(Gun_attachments_Double_Tap)

Scout_Attachments = [Gun_Attachments_Barrel_Stabilizer, Gun_Attachments_Mags, Gun_Attachments_AR_Optics, Gun_Attachments_Stock, Gun_attachments_Double_Tap]

#Batts
Window_Content_Batts_Min = tkinter.Scale(Window,label="Min Batts", from_=0, to=48, orient=HORIZONTAL)
Window_Content_Batts_Max = tkinter.Scale(Window,label="Max Batts" ,from_=0, to=48, orient=HORIZONTAL)
Window_Content_Batts_Min.set(0)
Window_Content_Batts_Max.set(12)
Window_Content_Batts_Min.grid()
Window_Content_Batts_Max.grid()

def Rand_Batts(event):
    Batts_Min = Window_Content_Batts_Min.get()
    Batts_Max = Window_Content_Batts_Max.get()
    Batts_Rand_Value =random.randrange(Batts_Min, Batts_Max+1)
    Value = ("Batt Amount: " + (str(Batts_Rand_Value)))
    Batts_Value.set(Value)

Button_Batts = Button(Window, text="Generate Battery Values")
Button_Batts.bind("<Button-1>", Rand_Batts)
Button_Batts.grid()
Batts_Value = StringVar()
Batts_Display = Label(Window, textvariable=Batts_Value)
Batts_Display.grid()



#Cells
Window_Content_Cells_Min = tkinter.Scale(Window,label="Min Cells" ,from_=0, to=48, orient=HORIZONTAL)
Window_Content_Cells_Max = tkinter.Scale(Window,label="Max Cells" ,from_=0, to=48, orient=HORIZONTAL)
Window_Content_Cells_Min.set(0)
Window_Content_Cells_Max.set(16)
Window_Content_Cells_Min.grid()
Window_Content_Cells_Max.grid()

def Rand_Cells(event):
    Cells_Min = Window_Content_Cells_Min.get()
    Cells_Max = Window_Content_Cells_Max.get()
    Cells_Rand_Value =random.randrange(Cells_Min, Cells_Max+1)
    Value = ("Cell Amount: " + (str(Cells_Rand_Value)))
    Cells_Value.set(Value)

Button_Cells = Button(Window, text="Generate Cell Values")
Button_Cells.bind("<Button-1>", Rand_Cells)
Button_Cells.grid()
Cells_Value = StringVar()
Cells_Display = Label(Window, textvariable=Cells_Value)
Cells_Display.grid()



#Phoenix
Window_Content_Phoenix_Min = tkinter.Scale(Window,label="Min Phoenix" ,from_=0, to=32, orient=HORIZONTAL)
Window_Content_Phoenix_Max = tkinter.Scale(Window,label="Max Phoenix" ,from_=0, to=32, orient=HORIZONTAL)
Window_Content_Phoenix_Min.set(0)
Window_Content_Phoenix_Max.set(2)
Window_Content_Phoenix_Min.grid()
Window_Content_Phoenix_Max.grid()

def Rand_Phoenix(event):
    Phoenix_Min = Window_Content_Phoenix_Min.get()
    Phoenix_Max = Window_Content_Phoenix_Max.get()
    Phoenix_Rand_Value =random.randrange(Phoenix_Min, Phoenix_Max+1)
    Value = ("Phoenix Amount: " + (str(Phoenix_Rand_Value)))
    Phoenix_Value.set(Value)

Button_Phoenix = Button(Window, text="Generate Phoenix Values")
Button_Phoenix.bind("<Button-1>", Rand_Phoenix)
Button_Phoenix.grid()
Phoenix_Value = StringVar()
Phoenix_Display = Label(Window, textvariable=Phoenix_Value)
Phoenix_Display.grid()



#Medis
Window_Content_Medis_Min = tkinter.Scale(Window,label="Min Medis", from_=0, to=64, orient=HORIZONTAL)
Window_Content_Medis_Max = tkinter.Scale(Window,label="Max Medis" ,from_=0, to=64, orient=HORIZONTAL)
Window_Content_Medis_Min.set(0)
Window_Content_Medis_Max.set(12)
Window_Content_Medis_Min.grid(row=0, column=1)
Window_Content_Medis_Max.grid(row=1, column=1)

def Rand_Medis(event):
    Medis_Min = Window_Content_Medis_Min.get()
    Medis_Max = Window_Content_Medis_Max.get()
    Medis_Rand_Value =random.randrange(Medis_Min, Medis_Max+1)
    Value = ("Medi Amount: " + (str(Medis_Rand_Value)))
    Medis_Value.set(Value)

Button_Medis = Button(Window, text="Generate Medi Values")
Button_Medis.bind("<Button-1>", Rand_Medis)
Button_Medis.grid(row=2, column=1)
Medis_Value = StringVar()
Medis_Display = Label(Window, textvariable=Medis_Value)
Medis_Display.grid(row=3, column=1)



#Syringe
Window_Content_Syringe_Min = tkinter.Scale(Window,label="Min Syringe" ,from_=0, to=48, orient=HORIZONTAL)
Window_Content_Syringe_Max = tkinter.Scale(Window,label="Max Syringe" ,from_=0, to=48, orient=HORIZONTAL)
Window_Content_Syringe_Min.set(0)
Window_Content_Syringe_Max.set(16)
Window_Content_Syringe_Min.grid(row=4, column=1)
Window_Content_Syringe_Max.grid(row=5, column=1)

def Rand_Syringe(event):
    Syringe_Min = Window_Content_Syringe_Min.get()
    Syringe_Max = Window_Content_Syringe_Max.get()
    Syringe_Rand_Value =random.randrange(Syringe_Min, Syringe_Max+1)
    Value = ("Syringe Amount: " + (str(Syringe_Rand_Value)))
    Syringe_Value.set(Value)

Button_Syringe = Button(Window, text="Generate Syringe Values")
Button_Syringe.bind("<Button-1>", Rand_Syringe)
Button_Syringe.grid(row=6, column=1)
Syringe_Value = StringVar()
Syringe_Display = Label(Window, textvariable=Syringe_Value)
Syringe_Display.grid(row=7, column=1)



#Gear
Window_Content_Gear_Min = tkinter.Scale(Window, label="Min Gear level", from_=0, to=4, orient=HORIZONTAL)
Window_Content_Gear_Max = tkinter.Scale(Window, label="Max Gear level", from_=0, to=4, orient=HORIZONTAL)
Window_Content_Gear_Min.set(1)
Window_Content_Gear_Max.set(4)
Window_Content_Gear_Min.grid(row=0, column=2)
Window_Content_Gear_Max.grid(row=1, column=2)

def Rand_Gear_Helmet(event):
    Gear_Min = Window_Content_Gear_Min.get()
    Gear_Max = Window_Content_Gear_Max.get()
    Gear_Rand_Value_Helmet = random.randrange(Gear_Min, Gear_Max+1)
    Value = ("Helmet Level: " + (str(Gear_Rand_Value_Helmet)))
    Gear_Value_Helmet.set(Value)


def Rand_Gear_Armor(event):
    Gear_Min = Window_Content_Gear_Min.get()
    Gear_Max = Window_Content_Gear_Max.get()
    Gear_Rand_Value_Armor = random.randrange(Gear_Min, Gear_Max+1)
    Value = ("Armor Level: " + (str(Gear_Rand_Value_Armor)))
    Gear_Value_Armor.set(Value)
    

def Rand_Gear_Shield(event):
    Gear_Min = Window_Content_Gear_Min.get()
    Gear_Max = Window_Content_Gear_Max.get()
    Gear_Rand_Value_Shield = random.randrange(Gear_Min, Gear_Max+1)
    Value = ("Shield Level: " + (str(Gear_Rand_Value_Shield)))
    Gear_Value_Shield.set(Value)

def Rand_Gear_Backpack(event):
    Gear_Min = Window_Content_Gear_Min.get()
    Gear_Max = Window_Content_Gear_Max.get()
    Gear_Rand_Value_Backpack = random.randrange(Gear_Min, Gear_Max+1)
    Value = ("Backpack Level: " + (str(Gear_Rand_Value_Backpack)))
    Gear_Value_Backpack.set(Value)



Button_Gear = Button(Window, text="Generate Gear Level")
Button_Gear.bind("<Button-1>", Rand_Gear_Helmet, add="+")
Button_Gear.bind("<Button-1>", Rand_Gear_Armor, add="+")
Button_Gear.bind("<Button-1>", Rand_Gear_Shield, add="+")
Button_Gear.bind("<Button-1>", Rand_Gear_Backpack, add="+")
Button_Gear.grid(row=2, column=2)
Gear_Value_Helmet = StringVar()
Gear_Value_Armor = StringVar()
Gear_Value_Shield = StringVar()           
Gear_Value_Backpack = StringVar()
Gear_Display_Helmet = Label(Window, textvariable=Gear_Value_Helmet)
Gear_Display_Armor = Label(Window, textvariable=Gear_Value_Armor)
Gear_Display_Shield = Label(Window, textvariable=Gear_Value_Shield)
Gear_Display_Backpack = Label(Window, textvariable=Gear_Value_Backpack)
Gear_Display_Helmet.grid(row=3, column=2)
Gear_Display_Armor.grid(row=4, column=2)
Gear_Display_Shield.grid(row=5, column=2)
Gear_Display_Backpack.grid(row=6, column=2)



#Legends
def Rand_Legend(event):
    Legend_Rand_Value = random.choice(Apex_Legends)
    Value = ("Legend: " + (str(Legend_Rand_Value)))
    Legend_Value.set(Value)

Legend_Value = StringVar()
Legend_Display = Label(Window, textvariable=Legend_Value)
Legend_Button = Button(Window, text= "Generate Legend")
Legend_Button.bind("<Button-1>", Rand_Legend)
Legend_Button.grid(row=8, column=1)
Legend_Display.grid(row=9, column=1)



#Guns
def Rand_Gun(event):
    Gun_Rand_Value_1 = random.choice(Apex_Wapons)
    Gun_Rand_Value_2 = random.choice(Apex_Wapons)
    Value_1 = ("Wapon 1: " + (str(Gun_Rand_Value_1)))
    Value_2 = ("Wapon 2: " + (str(Gun_Rand_Value_2)))
    Gun_Value_1.set(Value_1)
    Gun_Value_2.set(Value_2)  

    Attachment_Min = Window_Content_Attachment_Min.get()
    Attachment_Max = Window_Content_Attachment_Max.get()
    Attachment_Rand_Value =random.randrange(Attachment_Min, Attachment_Max+1)
    Value = ("Attachment Level: " + (str(Attachment_Rand_Value)))
    #Value = ("Attachment Level: " + (str(Attachment_Rand_Value)))
    #alue = ("Attachment Level: " + (str(Attachment_Rand_Value)))
    #Value = ("Attachment Level: " + (str(Attachment_Rand_Value)))
    #Value = ("Attachment Level: " + (str(Attachment_Rand_Value)))
    Attachment_Value.set(Value)

Attachment_Value = StringVar()



Gun_Value_1 = StringVar()
Gun_Display_1 = Label(Window, textvariable=Gun_Value_1)
Gun_Value_2 = StringVar()
Gun_Display_2 = Label(Window, textvariable=Gun_Value_2)
Gun_Button = Button(Window, text= "Generate Guns")
Gun_Button.bind("<Button-1>", Rand_Gun)
Gun_Button.grid(row=0, column=3)
Gun_Display_1.grid(row=1, column=3) 
Gun_Display_2.grid(row=2, column=3)

Gun_Attachments_Value_1 = StringVar()
Gun_Attachments_Value_2 = StringVar()
Gun_Attachments_Display_1 = Label(Window, textvariable=Gun_Attachments_Value_1)
Gun_Attachments_Display_2 = Label(Window, textvariable=Gun_Attachments_Value_2)

Window_Content_Attachment_Min = tkinter.Scale(Window,label="Min Attachments" ,from_=0, to=4, orient=HORIZONTAL)
Window_Content_Attachment_Max = tkinter.Scale(Window,label="Max Attachments" ,from_=0, to=4, orient=HORIZONTAL)
Window_Content_Attachment_Min.set(1)
Window_Content_Attachment_Max.set(4)
Window_Content_Attachment_Min.grid(row=4, column=3)
Window_Content_Attachment_Max.grid(row=5, column=3)


Attachment_Value = StringVar()
Attachment_Display = Label(Window, textvariable=Attachment_Value)
Attachment_Display.grid(row=6, column=3)





mainloop()