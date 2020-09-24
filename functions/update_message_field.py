

def update_dir_select_message(gv, dir):
    dirLabel = ["x", "y", "z"][dir]
    var_name = "checkbutton_"+dirLabel+"_select"
    if gv.var[var_name].get():
        gv.var["message_field"].set("Data in "+dirLabel+" direction is selected.")
    else:
        gv.var["message_field"].set("Data in "+dirLabel+" direction is deselected.")