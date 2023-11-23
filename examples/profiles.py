import badger2040
import badger_os
import jpegdec
import os

STATE = {
    "file_names": [],
    "no_of_files": 0,
    "file_names_ptr": 0,
    "is_warning_displayed": False
}

badger = badger2040.Badger2040()
jpeg = jpegdec.JPEG(badger.display)

def init_profiles():
    badger.set_update_speed(badger2040.UPDATE_MEDIUM)
    badger_os.state_load("profiles", STATE)
    read_file_names()
    draw_profile_wrapper()

def read_file_names():
    try:
        STATE["file_names"] = [f for f in os.listdir("/profiles") if f.endswith(".txt")]
        STATE["no_of_files"] = len(STATE["file_names"])
    except OSError:
        print("File operation error.")

def get_file_content(file_num):
    file_name = STATE["file_names"][file_num]
    file_obj = open(f"/profiles/{file_name}", "r")
    data_list = file_obj.read().strip().split("\r\n")

    return data_list

def draw_profile_wrapper():
    profile_data = get_file_content(STATE["file_names_ptr"])
    draw_profile(profile_data[0], profile_data[1], int(profile_data[2]), int(profile_data[3]), profile_data[4], int(profile_data[5]), float(profile_data[6]), profile_data[7], int(profile_data[8]), profile_data[9], int(profile_data[10]), profile_data[11], int(profile_data[12]))

def draw_profile(uri, is_qr_code, uri_x, uri_y, name, name_x, name_scale, post, post_x, org, org_x, pronouns, pronouns_x):
    badger.set_pen(15)
    badger.clear()

    if is_qr_code != "True":
        jpeg.open_file(uri)
        jpeg.decode(uri_x, uri_y, dither=True)

    badger.set_pen(0)
    badger.set_font("sans")

    badger.set_thickness(3)
    badger.text(name, name_x, 40, scale=name_scale)
    badger.set_thickness(2)
    badger.text(post, post_x, 60, scale=0.55)
    badger.text(org, org_x, 80, scale=0.55)
    badger.set_thickness(1)
    badger.text(pronouns, pronouns_x, 100, scale=0.55)

    badger.update()

def main():
    init_profiles()

    while True:
        # Sometimes a button press or hold will keep the system powered *through* HALT, so latch the power back on.
        badger.keepalive()

        if badger.pressed(badger2040.BUTTON_UP):
            STATE["is_warning_displayed"] = False

            if STATE["file_names_ptr"] > 0:
                STATE["file_names_ptr"] -= 1
            else:
                STATE["file_names_ptr"] = STATE["no_of_files"] - 1

            draw_profile_wrapper()

        if badger.pressed(badger2040.BUTTON_DOWN):
            STATE["is_warning_displayed"] = False

            if STATE["file_names_ptr"] < (STATE["no_of_files"] - 1):
                STATE["file_names_ptr"] += 1
            else:
                STATE["file_names_ptr"] = 0

            draw_profile_wrapper()

        if badger.pressed(badger2040.BUTTON_B):
            if not STATE["is_warning_displayed"]:
                STATE["is_warning_displayed"] = True
                badger_os.warning(badger, "Press 'UP' and 'DOWN' to loop through profiles. Details at https://github.com/ HarshKapadia2/badger-2040.")
            else:
                STATE["is_warning_displayed"] = False
                draw_profile_wrapper()

        badger_os.state_save("profiles", STATE)

        # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
        badger.halt()

main()
