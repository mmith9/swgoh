def LetsFaceIt\
    (gender, ethnicity):
    try:
        if (gender!="Male"):
            chanceOfSTEMJob="24%"
            if (ethnicity!="White" and ethnicity!="Asian"):
                chanceOfSTEMJob="5%"
    except:
        logging.error("This is the STEM gap")
    return chanceOfSTEMJob

