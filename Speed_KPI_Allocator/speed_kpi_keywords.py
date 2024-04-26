
#====================================== S24 =================================================

s24_primary_keywords = ["Slip & Cut", "Slip and cut", "Slip drill line", " Slip & Cut Drill","Cut & Slip", "Cut and Slip"]
s24_secondary_keyword = ["Brake Test"]
s24_exceptional_keyword = ["Pre-Job Safety","Pre job safety"]
#=============================================================================================


#====================================== S25 =================================================

s25_startrow_tracker = 0

s25_startpoint_keywords = [ "Shoetrack", "Shoe track", "Casing Shoe", " Float Shoe", "Float Collar", "Float collar",
                           "Float shoe", "Casing shoe"]

# bit depth of previous row should be zero
# difference between bit depth of previous row of startpoint and startpoint <=50 then code KPI.


s25_endpoint_keywords = ["Run Casing", "Run casing"]

s25_special_keyword = ["RIH", "Casing"]  # if not endpoint keyword then both special keyword must be there.




# s25_startpoint_keywords = ["P/up", "P/Up", "M/up", "M/Up", "M/U", "P/U", "Shoetrack",
#                            "Shoe track", "Casing Shoe", " Float Shoe", "Float Collar", "Float collar",
#                            "Float shoe", "Casing shoe"]



#====================================== S26 =================================================

s26_startrow_tracker = 0
s26_outrow_tracker = 0
td5_occurrence = False
s26_shoe_depth_treacker = (0,0)  #(kpi, shoedepth)
s26_startpoint_keywords = ["Drillout  Shoetrack" , "Cleanout Shoetrack", "Drill out shoetrack", "Drilling out shoetrack", "Clean Out Shoetrack",
                           "Drill out float collar","Drill float collar", "Drill out wiper plugs", "Clean Out Shoe Track", "Drill Out Shoe Track",
                           "Drill out cement","Drill out shoe track","Drill float","Drill shoe track","Drill Shoe track", "Drilling out cement"]

s26_continue_keywords = ["Drillout  Shoetrack" , "Cleanout Shoetrack", "Drill out shoetrack", "Drilling out shoetrack", "Clean Out Shoetrack",
                           "Drill out float collar","Drill float collar", "Drill out wiper plugs", "Clean Out Shoe Track", "Drill Out Shoe Track",
                         "Drill Shoe","Drill shoe", "Drill out shoe", "Drill out cement", "Drill cmt", "Drill Cement","Drill cement"]


#  Note :  if "rat hole", "rathole" found with any of the above then S26 ends in that row.
s26_rathole_keyword = ["Rat hole", "Rathole", "rathole", "rat hole"]

# Note : if no rathole or rat hole present then S26 stops the row before the following keywords are found

s26_endpoint_keywords = ["Drill new formation", "Drill Ahead", "drill ahead", "Drilling Ahead", "Drill Formation", "Drill Section",
                         "Drilling new formation","Drilling New Formation"]
s26_special_keyword= ["Drill", "section"]


