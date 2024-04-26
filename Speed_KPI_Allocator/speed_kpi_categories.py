
#====================================== S24 =================================================
def s24_category(s24_startpoint,df):
    slip_cut = s24_slip_cut_category(s24_startpoint,df)
    print("Slip & cut cat output : ",slip_cut)
    if slip_cut:
        print("Slip & Cut cut output is True")
        slip_and_cut = df.loc[s24_startpoint, "Speed KPI Cat"] = "Slip & Cut"
        return

def s24_slip_cut_category(s24_startpoint,df):
    # keyword = ["Slip & Cut", "Slip and cut", "Slip drill line", " Slip & Cut Drill"]
    s24_present = [True if "S24" in df.loc[s24_startpoint, "Speed KPI"] else False]
    # [True if k in df.loc[s24_assignpoint, 'Operations: (00:00 - 24:00)'] else False for k in keyword]
    if any(s24_present):
        return True
    return False
#=======================================================================================

