import speed_kpi_keywords as spkey
import speed_kpi_categories as sp_categ
import pandas as pd


def assign_speed_kpi(row,data):
    print("S24 allocator start......")
    s24 = s24_allocator(row,data)
    print("S24 allocated ",row.name)
    print("S26 allocator start......")
    s26 = s26_allocator(row, data)
    print("S26 allocated ", row.name)
    # out = allocate_out_kpi(startpoint,endpoint, df)
    return


def s24_allocator(row, df):
    """
    S24 is codes if any row has the following key words: slip & cut, slip and cut, slip drill line.
    S24 is also coded if any row has the following key words: slip & cut, slip and cut, slip drill line and the next row has the keyword 'brake test'.
    S24 is not coded if the row has the keyword 'pre job safety'.
    """
    s24_primary_keyword_present = [True if x in row["Operations: (00:00 - 24:00)"] or
                                           x.lower() in row["Operations: (00:00 - 24:00)"] else False
                                   for x in spkey.s24_primary_keywords]
    s24_secondary_keyword_present = [True if x in row["Operations: (00:00 - 24:00)"] or
                                             x.lower() in row["Operations: (00:00 - 24:00)"] else False
                                     for x in spkey.s24_secondary_keyword]
    s24_exceptional_keyword_present = [True if x in row["Operations: (00:00 - 24:00)"] or
                                               x.lower() in row["Operations: (00:00 - 24:00)"].lower() else False
                                       for x in spkey.s24_exceptional_keyword]

    s24_startpoint = 0
    if any(s24_primary_keyword_present) and not any(s24_exceptional_keyword_present):
        s24_startpoint = row.name
        df.loc[s24_startpoint, "Speed KPI"] = "S24"
        # selecting cell based on row s24_startpoint+1 and column  "Operations: (00:00 - 24:00)", convert it into lowercase,
        # convert string in lowercase and check it present in row s24_startpoint+1 and column  "Operations: (00:00 - 24:00)" not found.
        if (s24_startpoint + 1 < len(df) and spkey.s24_secondary_keyword[0].lower() in df.loc[s24_startpoint + 1, "Operations: (00:00 - 24:00)"].lower()):
            df.loc[s24_startpoint + 1, "Speed KPI"] = "S24"
        print("S24 allocated successfully ", s24_startpoint,row.name+1)
        return
#
###################################################################


# previous_shoe_depth = 715
# def s26_allocator(row, df, previous_shoe_depth):
def s26_allocator(row, df):

    s26_startpoint_found = False
    s26_endpoint_found = False

    if spkey.s26_startrow_tracker > row.name:
        row.name = spkey.s26_startrow_tracker
        spkey.s26_outrow_tracker = row.name
    s26_startpoint_keyword_present = [True if x in df.at[row.name, "Operations: (00:00 - 24:00)"] or
                                              x.lower() in df.at[row.name, "Operations: (00:00 - 24:00)"] else False
                                      for x in spkey.s26_startpoint_keywords]
    s26_endpoint_keyword_present_startrow = [True if x in df.at[row.name, "Operations: (00:00 - 24:00)"] or
                                                     x.lower() in df.at[
                                                         row.name, "Operations: (00:00 - 24:00)"] else False
                                             for x in spkey.s26_endpoint_keywords]
    if (any(s26_startpoint_keyword_present) and not(any(s26_endpoint_keyword_present_startrow)) and int(df.at[row.name, 'Bit Depth (m)']) > int(df.at[row.name - 1, 'Bit Depth (m)'])):
        s26_startpoint = row.name
        # check_end = s26_startpoint
        # df.loc[s26_startpoint, "Speed KPI"] = "S26"
        s26_startpoint_found = True
        print("S26 startpoint found",row.name)
        print("Startpoint ", s26_startpoint)

        # print(row.name, check_end)
        for row_id in range(s26_startpoint,len(df)):
            # print("Row id", row_id)
            print(" endpoint criteria checking loop.....", row_id)
            # if int(df.at[row_id, 'Bit Depth (m)']) == int(df.at[row_id - 1, 'Bit Depth (m)']):
            #     continue
            if int(df.at[row_id, 'Bit Depth (m)']) > int(df.at[row_id - 1, 'Bit Depth (m)']):
                print("Check for endpoint criteria by keywords.....",row_id)
                # check in row id
                s26_rathole_keyword_present = [True if i in df.at[row_id,"Operations: (00:00 - 24:00)"] or
                                                       i.lower() in df.at[row_id,"Operations: (00:00 - 24:00)"] else False
                                               for i in spkey.s26_rathole_keyword]
                print(s26_rathole_keyword_present, row_id)
                s26_endpoint_keyword_present = [True if i in df.at[row_id, "Operations: (00:00 - 24:00)"] or
                                                        i.lower() in df.at[
                                                            row_id, "Operations: (00:00 - 24:00)"] else False
                                                for i in spkey.s26_endpoint_keywords]
                # If rat hole or rathole found, set endpoint and assign S26
                if any(s26_rathole_keyword_present) and not (any(s26_endpoint_keyword_present)):
                    print("Check rathole keyword:", row_id)

                    s26_endpoint_found = True
                    s26_endpoint = row_id
                    # df.loc[row_id, "Speed KPI"] = "S26"
                    spkey.s26_startrow_tracker = s26_endpoint +1
                    print("s26 endpoint rathole keyword present : ", s26_endpoint)
                    break

                s26_special_keyword_present = [True if i in df.at[row_id, "Operations: (00:00 - 24:00)"] or
                                                        i.lower() in df.at[
                                                            row_id, "Operations: (00:00 - 24:00)"] else False
                                                for i in spkey.s26_special_keyword]
                print(s26_endpoint_keyword_present, row_id)
                if any(s26_endpoint_keyword_present) or all(s26_special_keyword_present):
                    print("Endpoint keyword present", s26_endpoint_keyword_present, row_id)
                    print("check endpoint keyword : ", row_id)
                    # If endpoint keyword present, set endpoint and break
                    s26_endpoint_found = True
                    s26_endpoint = row_id - 1
                    spkey.s26_startrow_tracker = s26_endpoint +1
                    print("s26 endpoint keyword present : ", s26_endpoint)
                    break
                print("if endpoint not found by using keyword then look bit depth decreases....")
            if not s26_endpoint_found and int(df.at[row_id, 'Bit Depth (m)']) < int(df.at[row_id - 1, 'Bit Depth (m)']):
                print("Check endpoint criteria by bit depth ......,", row_id)
                current_bit_depth = df.at[row_id-1, "Bit Depth (m)"]
                print("Current bit depth of row : ", current_bit_depth, row_id)
                while current_bit_depth == df.at[row_id-1, "Bit Depth (m)"]:
                    row_id -= 1
                    # If bit depth decreases, set endpoint and break
                    print("while loop, j:", row_id)

                s26_endpoint_found = True
                s26_endpoint = row_id
                spkey.s26_startrow_tracker= s26_endpoint+1
                print("s26 endpoint present by bit depth criteria : ", s26_endpoint)
                break
    else:
        print("S26 startpoint not found", row.name)
        return

    if s26_startpoint_found and s26_endpoint_found:
        # print("Check end value : ", check_end)
        continue_found = False
        print("S26 allocator from : ", s26_startpoint,s26_endpoint)
        print(s26_startpoint, s26_endpoint)
        # if (int(df.at[s26_endpoint, "Bit Depth (m)"]) - int(df.at[s26_startpoint - 1, "Bit Depth (m)"]) <= 60 and
        #         int(df.at[s26_endpoint, "Bit Depth (m)"]) >= previous_shoe_depth):
        if (int(df.at[s26_endpoint, "Bit Depth (m)"]) - int(df.at[s26_startpoint - 1, "Bit Depth (m)"]) <= 60) :
            df.loc[s26_startpoint, "Speed KPI"] = "S26"
            for i in range(s26_startpoint+1, s26_endpoint+1):

                # df.loc[s26_startpoint, "Speed KPI"] = "S26"
                print("Startpoint previous row bit depth: ",df.at[s26_startpoint-1, "Bit Depth (m)"])
                print("endpoint row bit depth: ", int(df.at[s26_endpoint, "Bit Depth (m)"]))


                s26_continue_keyword_present = [True if x in df.at[i,"Operations: (00:00 - 24:00)"] or
                                                        x.lower() in df.at[i,"Operations: (00:00 - 24:00)"] else False
                                                for x in spkey.s26_continue_keywords]
                # s26_endpoint_keyword_present_cont = [True if x in df.at[i, "Operations: (00:00 - 24:00)"] or
                #                                         x.lower() in df.at[i, "Operations: (00:00 - 24:00)"] else False
                #                                 for x in spkey.s26_endpoint_keywords]
                # s26_special_keyword_present_cont= [True if x in df.at[i, "Operations: (00:00 - 24:00)"] or
                #                                        x.lower() in df.at[
                #                                            i, "Operations: (00:00 - 24:00)"] else False
                #                                for x in spkey.s26_special_keyword]
                print("check s26 continue keyword present: ")
                # spkey.s26_outstart_tracker.append(s26_startpoint)

                if (any(s26_continue_keyword_present) and df.at[i, "Bit Depth (m)"] > df.at[i-1, "Bit Depth (m)"]):
                    print(s26_continue_keyword_present, i)
                    continue_found = True
                    df.loc[i, "Speed KPI"] = "S26"
                    print("S26 allocation done ", s26_startpoint, i)
                    out_endpoint_row = df[df['Speed KPI'] == 'S26'].index[-1]
                    spkey.s26_outrow_tracker = out_endpoint_row
                    # print("updated out endpoint-----------", spkey.s26_outrow_tracker)
                    # print("Endpoint row : ", endpoint_row)
                    # return spkey.s26_outrow_tracker
                s26_rathole_keyword_present_end = [True if x in df.at[i, "Operations: (00:00 - 24:00)"] or
                                                       x.lower() in df.at[i, "Operations: (00:00 - 24:00)"] else False
                                               for x in spkey.s26_rathole_keyword]

                if any(s26_rathole_keyword_present_end) and df.at[i, "Bit Depth (m)"] > df.at[i-1, "Bit Depth (m)"]:
                    df.loc[i, "Speed KPI"] = "S26"
                    out_endpoint_row = df[df['Speed KPI'] == 'S26'].index[-1]
                    spkey.s26_outrow_tracker = out_endpoint_row
                    continue_found = True

                print("check Bit depth same as previous")

            for x in range(s26_startpoint+1, spkey.s26_outrow_tracker):
                if int(df.at[x, "Bit Depth (m)"]) == int(df.at[x - 1, "Bit Depth (m)"]) and x < s26_endpoint:
                    print("Row id for out ", x)
                    print("Bit depth same as : ", x, "and ", x - 1)
                    df.loc[x, "Speed KPI"] = "OUT"
                    print("OUT Allocated : ", x)

            if spkey.s26_outrow_tracker <= s26_endpoint:
                spkey.s26_outrow_tracker = df[df['Speed KPI'] == 'S26'].index[-1]
                print("updated out endpoint-----------", spkey.s26_outrow_tracker)
                return spkey.s26_outrow_tracker

        else:
            print("Do not allocate S26, because difference is > 50m or endpoint bit depth < previous shoe depth")
            return
    if s26_endpoint_found :
        spkey.s26_startrow_tracker = s26_endpoint + 1
        print("updated s26_startpoint check from ---------------", spkey.s26_startrow_tracker)
        return spkey.s26_startrow_tracker

    # return
##################################################33