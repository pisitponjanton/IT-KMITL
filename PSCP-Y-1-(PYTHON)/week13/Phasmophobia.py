"""Phasmophobia"""
def main(a,b,c):
    """Phasmophobia"""
    d = {
        "Banshee": ["EMF Level 5", "Fingerprints", "Freezing Temperatures"],
        "Demon": ["Ghost Writing", "Spirit Box", "Freezing Temperatures"],
        "Jinn": ["EMF Level 5", "Spirit Box", "Ghost Orb"],
        "Mare": ["Spirit Box","Freezing Temperatures", "Ghost Orb"],
        "Oni": ["EMF Level 5", "Ghost Writing", "Spirit Box"],
        "Phantom": ["EMF Level 5", "Freezing Temperatures", "Ghost Orb"],
        "Poltergeist": ["Fingerprints", "Spirit Box", "Ghost Orb"],
        "Revenant": ["EMF Level 5", "Ghost Writing", "Fingerprints"],
        "Shade": ["EMF Level 5", "Ghost Writing", "Ghost Orb"],
        "Spirit": ["Ghost Writing", "Fingerprints", "Spirit Box"],
        "Wraith": ["Fingerprints", "Spirit Box", "Freezing Temperatures"],
        "Yurei": ["Ghost Writing", "Freezing Temperatures", "Ghost Orb"]
    }
    l,s = [i for i in (a,b,c) if i != "No evidence"],0
    for i,j in d.items():
        if all(z in j for z in l):
            s=1
            print(i)
    if not s:
        print("Not yet discovered")
main(input(),input(),input())
