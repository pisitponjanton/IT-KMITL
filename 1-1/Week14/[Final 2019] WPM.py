"""[Final 2019] WPM"""
def ki(a):
    """[Final 2019] WPM"""
    if a<11:
        return "Very Slow"
    if 11<=a<=20:
        return "Slow"
    if 21<=a<=30:
        return "Average"
    if 31<=a<=40:
        return "Fast"
    return "Very Fast"
def ad(a):
    """[Final 2019] WPM"""
    if a<26:
        return "Very Slow"
    if 26<=a<=35:
        return "Slow/Beginner"
    if 36<=a<=45:
        return "Intermediate/Average"
    if 46<=a<=65:
        return "Fast/Advanced"
    if 66<=a<=80:
        return "Very Fast"
    return "Insane"
def main(k,a):
    """[Final 2019] WPM"""
    print(ki(a) if k == "Kids" else ad(a))
main(input(),int(input()))
